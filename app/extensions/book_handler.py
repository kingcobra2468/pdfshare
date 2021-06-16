from os import listdir
from typing import Mapping
from urllib.parse import quote
from pymongo import MongoClient
from clients.book_client import BookClient

class BookHandler:
    """ BooksDB Flask extension for loading
    """
    
    def __init__(self, app = None, config_prefix="BooksDB"):
        """Constructor.

        Args:
            app (Flask, optional): Instance of Flask app. Defaults to None.
            config_prefix (str, optional): Name of extension to be
                registered by flask. Defaults to "BooksDB".
        """
        self.__config_prefix = config_prefix
        self.client = None

        if app is not None:
            self.client = BookClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])

    def init_app(self, app):
        """Initialized and registers the extension with Flask.

        Args:
            app (Flask): Instance of Flask app.
        """
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.__config_prefix.lower()] = self
        
        if not self.client:
            self.client = BookClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])
    
    def get_books(self):
        """Fetches all the book instances.

        Returns:
            list(str): list of all of the books.
        """
        books = self.client.get_all_books(True)
        return books

    def get_book_names(self):
        """Get the name of all of the book.

        Returns:
            list(str): list of all of the book names
        """
        book_names = self.client.get_all_by_fields([BookClient.BOOK_NAME_FIELD,
            BookClient.BOOK_FILENAME_FIELD],True, True)
        return book_names