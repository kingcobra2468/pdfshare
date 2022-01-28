import os
import logging

from watchdog.events import FileSystemEventHandler

from pdfshare.app.config import BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM
from pdfshare.common.clients.pdf_library import PDFLibrary
from pdfshare.common.utils.pdf_utils import compute_pdf_hash
from pdfshare.pdfbsd.utils.pdf_utils import create_pdf_cover

logger = logging.getLogger(__name__)


class PDFScanner(FileSystemEventHandler):
    """Service for automatically loading existing and new pdfs
    into MongoDB mappings collection while also generating a cover
    if necessary. Listens to filesystem events in the selected
    pdfs directory.
    """

    def __init__(self, mongo_host, mongo_port):
        """Constructor.

        Args:
            mongo_host (str): Hostname of the mongoDB server.
            mongo_port (int): Port of the mongoDB server.
        """
        super().__init__()

        self.pdf_library = PDFLibrary(mongo_host, mongo_port)
        self.process_existing_pdfs()

    def process_existing_pdfs(self):
        """Processes the existing pdf which sit in the pdfs dir.
        """
        titles = [pdf[:-4] for pdf in os.listdir(
            BOOKS_DIR_SYSTEM) if '.pdf' == pdf[-4:]]  # loads in all pdfs

        for title in titles:
            logger.info(f'Found existing pdf "{title}".')
            fingerprint = compute_pdf_hash(BOOKS_DIR_SYSTEM, title)
            if self.pdf_library.check_pdf_exists(title=title, fingerprint=fingerprint):
                continue

            self._insert_pdf(title, fingerprint)

    def on_created(self, event):
        """Event callback for when new pdfs are detected in the pdfs dir.

        Args:
            event (watchdog.events.FileCreatedEvent): Callback event from watchdog.
        """
        if event.is_directory:  # ignore the creation of new directories
            return

        title = os.path.basename(event.src_path)
        if '.pdf' != title[-4:]:
            return

        title = title[:-4]
        logger.info(f'New pdf detected -> {title}.')

        self._insert_pdf(title)

    def _insert_pdf(self, title, fingerprint):
        """Adaptively insert a new pdf into the pdfs db. Attempts to generate a cover and use
        it, yet it failure occurs, resort to the default cover.

        Args:
            title (str): The name of the pdf.
        """
        cover_generated = True
        # failed to generate cover
        if create_pdf_cover(BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM, title):
            cover_generated = False
        
        self.pdf_library.insert_pdf(title, fingerprint, cover_generated=cover_generated)
