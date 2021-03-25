from os import system, listdir
from urllib.parse import quote
from re import sub

class BooksDB:
    """ BooksDB Flask extension for loading
    """
    
    def __init__(self, app = None, config_prefix="BooksDB"):
        """Constructor

        Args:
            app (Flask, optional): Instance of Flask app. Defaults to None.
            config_prefix (str, optional): Name of extension to be
                registered by flask. Defaults to "BooksDB".
        """
        self.__books = [] #books stored as tuples (<book-name>, <book-name.png>, <book-tag-encoded>)
        self.__books_lite = [] #books stored as tuples (<book-name>, <book-tag-encoded>) OMITS cover
        self.__config_prefix = config_prefix
    
    def init_app(self, app):
        """Initialized and registers the extension with Flask

        Args:
            app (Flask): Instance of Flask app.
        """
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.__config_prefix.lower()] = self

        self.__load_config(app)

    def __load_config(self, app):
        """Loads and applies server config

        Args:
            app (Flask): Instance of Flask app.
        """
        self.__BOOKS_DIR_SYSTEM = app.config['BOOKS_DIR_SYSTEM']
        self.__COVERS_DIR_SYSTEM = app.config['COVERS_DIR_SYSTEM']
        self.__DEFAULT_COVER_FILE = app.config['DEFAULT_COVER_FILE']

    def __load_books_data(self):
        """Loads in book data
        """
        self.__book_names = [sub('.pdf', '', book) for book in listdir(
            self.__BOOKS_DIR_SYSTEM) if book.find('.pdf') > -1] # loads in all pds

        # enoding of book name along w/ .pdf
        self.__encoded_book_tags = [quote(f'{book}.pdf') for book in self.__book_names]

    def load_books(self):
        """Loads in books into memory and generates cover snapshots if none exist.
        """
        self.__load_books_data()
        self.__books.clear()

        book_covers = listdir(self.__COVERS_DIR_SYSTEM)

        for book_name, encoded_book_tag in zip(self.__book_names, self.__encoded_book_tags):

            cover_tag = f'{book_name}.png' # book name with png extension

            if cover_tag in book_covers: # cover exists
                self.__books.append((book_name, cover_tag, encoded_book_tag))
                continue
            
            if self.pdf_cover_to_png(book_name): # failed to generate cover
                self.__books.append((book_name, self.__DEFAULT_COVER_FILE, encoded_book_tag))
            else:
                self.__books.append((book_name, cover_tag, encoded_book_tag))
    
    def __load_books_lite(self):
        """Loads books into memory without checking/generating covers
        """
        self.__load_books_data()
        self.__books_lite = [(book_name, book_tag) for book_name, book_tag in \
            zip(self.__book_names, self.__encoded_book_tags)]
    
    def get_books(self, refresh = False):
        """Fetches all the book instances

        Args:
            refresh (bool, optional): Whether to refresh db and check if new
                books were added. Defaults to False.

        Returns:
            [type]: [description]
        """
        if refresh or not len(self.__books):
            self.load_books()
    
        return self.__books

    def get_book_names(self, refresh = False):
        """Get the name of all of the book

        Args:
            refresh (bool, optional): Whether to refresh db and check if new
                books were added. Defaults to False.

        Returns:
            list(str): list of all of the book names
        """
        if refresh or not len(self.__books):
            self.__load_books_lite()

        return self.__books_lite

    def pdf_cover_to_png(self, pdf_name):
        """Generates a cover for 

        Args:
            pdf_name (str): Name of the PDF.

        Returns:
            int: Result of the internal system subprocess. 0 if no errors and non-zero value upon failure.
        """

        pdf_name = pdf_name.strip('.pdf')

        return system(f'pdftoppm -f 1 -l 1 -png "{self.__BOOKS_DIR_SYSTEM}/{pdf_name}.pdf" >' + \
            f'"{self.__COVERS_DIR_SYSTEM}/{pdf_name}.png"')