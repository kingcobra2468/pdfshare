import os
import logging

from watchdog.events import FileSystemEventHandler

from pdfshare.app.config import BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM
from pdfshare.common.clients.pdf_library import PDFLibrary
from pdfshare.common.utils.pdf_utils import compute_pdf_hash
from pdfshare.pdfbsd.utils.pdf_utils import create_pdf_cover, extract_pdf_name

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

            self._insert_pdf(title, fingerprint)

    def on_created(self, event):
        """Event callback for when new pdf is detected in the pdfs dir.

        Args:
            event (watchdog.events.FileCreatedEvent): Callback event from watchdog.
        """
        if event.is_directory:  # ignore the creation of new directories
            return

        title = extract_pdf_name(event.src_path)
        if not title:
            return

        fingerprint = compute_pdf_hash(BOOKS_DIR_SYSTEM, title)
        logger.info(f'New pdf detected -> {title}.')

        self._insert_pdf(title, fingerprint)

    def on_deleted(self, event):
        """Event callback for when a pdf is deleted in the pdfs dir.

        Args:
            event (watchdog.events.FileCreatedEvent): Callback event from watchdog.
        """
        if event.is_directory:  # ignore the deletion of directories
            return

        title = extract_pdf_name(event.src_path)
        if not title:
            return

        logger.info(f'The pdf "{title}" has marked for deletion.')

        self._delete_pdf(title)

    def on_moved(self, event):
        """Event callback for when a pdf is renamed in the pdfs dir.

        Args:
            event (watchdog.events.FileCreatedEvent): Callback event from watchdog.
        """
        if event.is_directory:  # ignore the creation of new directories
            return

        old_title = extract_pdf_name(event.src_path)
        new_title = extract_pdf_name(event.dest_path)
        if not old_title or not new_title:
            return

        logger.info(
            f'The pdf "{old_title}" has been renamed into "{new_title}".')

        self._rename_pdf(old_title, new_title)

    def _insert_pdf(self, title, fingerprint):
        """Adaptively insert a new pdf into the pdfs db. Attempts to generate a cover and use
        it, yet it failure occurs, resort to the default cover.

        Args:
            title (str): The name of the pdf.
            fingerprint (str): The fingerprint of the pdf.
        """
        cover_generated = True
        if self.pdf_library.check_pdf_exists(title=title, fingerprint=fingerprint):
            return

        # failed to generate cover
        if create_pdf_cover(BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM, title):
            cover_generated = False

        self.pdf_library.insert_pdf(
            title, fingerprint, cover_generated=cover_generated)

    def _delete_pdf(self, title):
        """Deletes a given pdf from the database and its corresponding cover image.

        Args:
            title (str): The name of the pdf.
        """
        if not self.pdf_library.check_pdf_exists(title=title):
            return

        pdf = self.pdf_library.get_pdf(title=title)

        os.remove(os.path.join(COVERS_DIR_SYSTEM, f"{pdf.title}.jpeg"))
        pdf.delete()

    def _rename_pdf(self, old_title, new_title):
        """Updates the given pdf database entry and cover image to reflect on the
        pdf's new title.

        Args:
            title (str): The name of the pdf.
        """
        if not self.pdf_library.check_pdf_exists(title=old_title):
            return

        pdf = self.pdf_library.get_pdf(title=old_title)
        pdf.title = new_title

        os.rename(os.path.join(COVERS_DIR_SYSTEM, f"{old_title}.jpeg"), os.path.join(
            COVERS_DIR_SYSTEM, f"{new_title}.jpeg"))
        pdf.save()
