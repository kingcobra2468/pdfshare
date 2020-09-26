from os import system, listdir
from urllib.parse import quote
from re import sub

class BooksDB:
    
    """ Constructor

    Initializes Books worker class & book containers
    """
    
    def __init__(self, app = None, config_prefix="BooksDB"):
        
        self.__books = [] #books stored as tuples (<book-name>, <book-name.png>, <book-tag-encoded>)
        self.__books_lite = [] #books stored as tuples (<book-name>, <book-tag-encoded>) OMITS cover
        self.__config_prefix = config_prefix
    
    def init_app(self, app):
        
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.__config_prefix.lower()] = self

        self.__load_config(app)

    #TODO: Add exception handling
    def __load_config(self, app):
        
        self.__BOOKS_DIR_SYSTEM = app.config['BOOKS_DIR_SYSTEM']
        self.__COVERS_DIR_SYSTEM = app.config['COVERS_DIR_SYSTEM']
        self.__DEFAULT_COVER_FILE = app.config['DEFAULT_COVER_FILE']

    """Raw Book Data Collections 
    
    Load raw book data(book name & web encodeded book file name) to be used for processing
    by secondary methods
    """
    def __load_books_data(self):

        self.__book_names = [sub('.pdf', '', book) for book in listdir(self.__BOOKS_DIR_SYSTEM) if book.find('.pdf') > -1]
        self.__encoded_book_tags = [quote(f'{book}.pdf') for book in self.__book_names]

    """Populating __books 
    
    Processing raw book data and fetching cover data and populating __books container
    """

    def load_books(self):

        self.__load_books_data()
        self.__books.clear()

        book_covers = listdir(self.__COVERS_DIR_SYSTEM)

        for book_name, encoded_book_tag in zip(self.__book_names, self.__encoded_book_tags):
            #print (book_name, ' ', encoded_book_tag)
            try:
                #check if cover exists for a pdf
                book_covers.index(f'{book_name}.png') #if cover exists returns index(useless) else ValueError thrown indicating cover doesnt exist for book
                self.__books.append((book_name, f'{book_name}.png', encoded_book_tag))
            except ValueError:
                if self.pdf_cover_to_png(book_name):
                    print('here')
                    self.__books.append((book_name, self.__DEFAULT_COVER_FILE, encoded_book_tag))
                else:
                    self.__books.append((book_name, f'{book_name}.png', encoded_book_tag))
    
    """Populating __books_lite
    
    Processing raw book data and populating __books container
    """

    def __load_books_lite(self):

        self.__load_books_data()
        self.__books_lite = [(book_name, book_tag) for book_name, book_tag in zip(self.__book_names, self.__encoded_book_tags)]
    
    """Get __books 
    
    Public method for getting __books container's data
    :param refresh: weather to refresh __books container before fetching it
    """

    def get_books(self, refresh = False):

        if refresh or len(self.__books) == 0:
            self.load_books()
        #print(self.__books)
        return self.__books # paly around with yield
    
    """Get __books_lite
    
    Public method for getting __books container's data
    :param refresh: weather to refresh __books_lite container before fetching it
    """

    def get_book_names(self, refresh = False):

        if refresh or len(self.__books) == 0:
            self.__load_books_lite()

        return self.__books_lite

    def pdf_cover_to_png(self, pdf_name):

        try:
            if pdf_name.index('.pdf'):
                pdf_name = pdf_name.strip('.pdf')
        except ValueError:
            pass

        return system(f'pdftoppm -f 1 -l 1 -png "{self.__BOOKS_DIR_SYSTEM}/{pdf_name}.pdf" > "{self.__COVERS_DIR_SYSTEM}/{pdf_name}.png"') #returns 0 if no errors else there are errors
