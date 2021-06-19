
from pdfshare.app.config import MONGO_HOST, MONGO_PORT, BOOKS_DIR_SYSTEM
from pdfshare.pdfbsd.scanners.book_scanner import BookScanner
from watchdog.observers import Observer
import daemon
import time
import logging

with daemon.DaemonContext(working_directory='.'):
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("pdfbsd.log", mode='a'),
        ]
    )

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