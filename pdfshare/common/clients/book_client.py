from pymongo import MongoClient

class BookClient:
    """Wrapper for for MongoDB mappings collection. Used for 
    storing metadata on path location for books.
    """
    # fields inside of the books collection
    BOOK_NAME_FIELD = 'bookName'
    BOOK_FILENAME_FIELD = 'filename'
    COVER_FILENAME_FIELD = 'cover'

    def __init__(self, host, port):
        """Constructor

        Args:
            host (str): Hostname of the mongoDB server.
            port (int): Port of the mongoDB server.
        """
        self._connect(host, port)
    
    def _connect(self, host, port):
        """Establishes a connection with the mongoDB server.

        Args:
            host (str): Hostname of the mongoDB server.
            port (int): Port of the mongoDB server.
        """
        client = MongoClient(host, port)
        self.db = client.books
        self.mappings = self.db.mappings

    def get_book(self, book_name):
        """Fetches a book's metadata given its names.

        Args:
            book_name (str): Name of the book.

        Returns:
            dict: The result of the mongodb find query.
        """
        book = self.db.mappings.find({self.BOOK_NAME_FIELD : book_name})
        return book

    def get_all_books(self, as_list=False):
        """Fetches all of the books in the books collection.

        Args:
            as_list (bool, optional): Whether to return books as a list 
            instead of the default iterator cursor. Defaults to False.

        Returns:
            pymongo.cursor.Cursor | list(pymongo.cursor.Cursor): Cursor of list depending on input args.
        """
        books = self.db.mappings.find({})
        return list(books) if as_list else books

    def get_num_books(self):
        """Fetches the number of books in the books collection

        Returns:
            list: The number of books in the collection.
        """
        return self.db.mappings.count()

    def get_all_by_fields(self, fields, w_id=False, as_list=False):
        """Fetches a filtered query to return only select fields.

        Args:
            fields (list(str)): The fields to query
            w_id (bool, optional): Whether to return the _id index along with
            each record. Defaults to False.
            as_list (bool, optional): Whether to return books as a list 
            instead of the default iterator cursor. Defaults to False.

        Raises:
            ValueError: Thrown if one of the request fields is not valid.

        Returns:
            pymongo.cursor.Cursor | list(pymongo.cursor.Cursor): Cursor of list depending on input args.
        """
        for field in fields:
            if field not in [self.BOOK_FILENAME_FIELD, self.BOOK_NAME_FIELD, self.COVER_FILENAME_FIELD]:
                raise ValueError(f'Field "{field}" is not a valid field for the query.')

        # construct the query
        query = dict(zip(fields, [1 for _ in range(len(fields))]))
        if w_id:
            query['_id'] = 1
        else:
            query['_id'] = 0

        result = self.db.mappings.find({}, query)
        return list(result) if as_list else result

    def check_book_exists(self, book_name):
        """Checks if metadata for a book exists given its name.

        Args:
            book_name (str): Name of the book to check.

        Returns:
            bool: Result on whether the book exists.
        """
        result = self.db.mappings.find_one({self.BOOK_NAME_FIELD: book_name})
        return True if result else False
    
    def insert_book(self, book_name, book_filename, cover_filename, data_race_safe=False):
        """Inserts a new book into the books collection.

        Args:
            book_name (str): Name of the book
            book_filename (str): Filename of the book
            cover_filename (str): Cover filename for the book .png cover.
            data_race_safe (bool, optional): Whether to insert book via a method to avoid data race 
            conditions. Defaults to False.
        """
        record = {self.BOOK_NAME_FIELD: book_name, self.BOOK_FILENAME_FIELD: book_filename,
            self.COVER_FILENAME_FIELD: cover_filename}

        if data_race_safe:
            self.db.mappings.update(record, record, upsert=True)
        else:
            self.db.mappings.insert_one(record)