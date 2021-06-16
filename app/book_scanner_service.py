from config import BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM, DEFAULT_COVER_FILE
from watchdog.events import FileSystemEventHandler
from urllib.parse import quote
from utils.book_utils import pdf_cover_to_png
from clients.book_client import BookClient
from re import sub
import os

class BookScanner(FileSystemEventHandler):
    """Service for automatically loading existing and new books
    into MongoDB mappings collection while also generating a cover
    if necessary. Listens to filesystem events in the selected
     books directory.
    """
    def __init__(self, mongo_host, mongo_port):
        """Constructor.

        Args:
            mongo_host (str): Hostname of the mongoDB server.
            mongo_port (int): Port of the mongoDB server.
        """
        super().__init__()
        
        self.book_db_client = BookClient(mongo_host, mongo_port)
        self.process_existing_books()

    def process_existing_books(self):
        """Processes the existing books which sit in the books dir.
        """
        book_names = [sub('.pdf', '', book) for book in os.listdir(
            BOOKS_DIR_SYSTEM) if book.find('.pdf') > -1] # loads in all pdfs

        for book_name in book_names:
            if self.book_db_client.check_book_exists(book_name): # cover exists
                continue

            self._adaptive_insert_book(book_name)

    def on_created(self, event):
        """Event callback for when new books are detected in the books dir.

        Args:
            event (watchdog.events.FileCreatedEvent): Callback event from watchdog.
        """
        if event.is_directory: # ignore the creation of new directories
            return

        book_name = os.path.basename(event.src_path)
        if '.pdf' not in book_name:
            return
    
        book_name = sub('.pdf', '', book_name)
        self._adaptive_insert_book(book_name)

    def _adaptive_insert_book(self, book_name):
        """Adaptively insert a new book into the books db. Attempts to generate a cover and use
        it, yet it failure occurs, resort to the default cover.

        Args:
            book_name (str): The name of the book.
        """
        cover_filename = f'{book_name}.png' # book name with png extension
        book_filename = quote(f'{book_name}.pdf')

        if pdf_cover_to_png(BOOKS_DIR_SYSTEM, COVERS_DIR_SYSTEM, book_name): # failed to generate cover
            cover_filename = DEFAULT_COVER_FILE

        self.book_db_client.insert_book(book_name, book_filename, cover_filename, True)

if __name__ == "__main__":
    from watchdog.observers import Observer
    from config import MONGO_HOST, MONGO_PORT
    import time

    observer = Observer()
    new_book_handler = BookScanner(MONGO_HOST, MONGO_PORT)

    observer.schedule(new_book_handler, BOOKS_DIR_SYSTEM)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()