from os import system, listdir
from utils.library_utils import pdf_cover_to_png, BOOKS_DIR, COVERS_DIR, DEFAULT_COVER_FILE
from urllib.parse import quote

class Books:
    
    """ Constructor

    Initializes Books worker class & book containers
    """
    
    def __init__ (self):
        
        self.__books = [] #books stored as tuples (<book-name>, <book-name.png>, <book-tag-encoded>)
        self.__books_lite = [] #books stored as tuples (<book-name>, <book-tag-encoded>) OMITS cover

    """Raw Book Data Collections 
    
    Load raw book data(book name & web encodeded book file name) to be used for processing
    by secondary methods
    """

    def __load_books_data (self):

        self.__book_names = [book.rstrip('.pdf') for book in listdir(BOOKS_DIR)]
        self.__encoded_book_tags = [quote(f'{book}.pdf') for book in self.__book_names]

    """Populating __books 
    
    Processing raw book data and fetching cover data and populating __books container
    """

    def __load_books (self):

        self.__load_books_data()
        self.__books.clear()

        book_covers = listdir(COVERS_DIR)

        for book_name, encoded_book_tag in zip(self.__book_names, self.__encoded_book_tags):
            print (book_name, ' ', encoded_book_tag)
            try:
                #check if cover exists for a pdf
                book_covers.index(f'{book_name}.png') #if cover exists returns index(useless) else ValueError thrown indicating cover doesnt exist for book
                self.__books.append((book_name, f'{book_name}.png', encoded_book_tag))
            except ValueError:
                
                if pdf_cover_to_png(book_name):
                    self.__books.append((book_name, DEFAULT_COVER_FILE, encoded_book_tag))
                else:
                    self.__books.append((book_name, f'{book_name}.png', encoded_book_tag))
    
    """Populating __books_lite
    
    Processing raw book data and populating __books container
    """

    def __load_books_lite (self):

        self.__load_books_data()
        self.__books_lite = [(book_name, book_tag) for book_name, book_tag in zip(self.__book_names, self.__encoded_book_tags)]
    
    """Get __books 
    
    Public method for getting __books container's data
    :param refresh: weather to refresh __books container before fetching it
    """

    def get_books (self, refresh = False):

        if refresh or len(self.__books) == 0:
            self.__load_books()
        print(self.__books)
        return self.__books # paly around with yield
    
    """Get __books_lite
    
    Public method for getting __books container's data
    :param refresh: weather to refresh __books_lite container before fetching it
    """

    def get_book_names (self, refresh = False):

        if refresh or len(self.__books) == 0:
            self.__load_books_lite()

        return self.__books_lite