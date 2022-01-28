from mongoengine import connect

from pdfshare.common.models.pdf import PDF


class PDFLibrary:
    """Wrapper for for MongoDB mappings collection. Used for 
    storing metadata on path location for pdfs.
    """

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
        self.client = connect(host=host, port=port, db='pdfshare')

    def get_all_pdfs(self, size=None, offset=None):
        """Fetches all of the pdfs in the pdfs collection.

        Returns:
            pymongo.cursor.Cursor | list(pymongo.cursor.Cursor): Cursor of list depending on input args.
        """
        if None in [size, offset]:
            return PDF.objects.exclude('id')

        return PDF.objects.skip(offset).limit(size).exclude('id')
        
    def get_pdf_count(self):
        """Fetches the number of pdfs in the pdfs collection

        Returns:
            list: The number of pdfs in the collection.
        """
        return PDF.objects.count()

    def check_pdf_exists(self, **query):
        result = PDF.objects(**query).count()
        return bool(result)

    def insert_pdf(self, title, fingerprint, **fields):
        if self.check_pdf_exists(title=title, fingerprint=fingerprint):
            return

        pdf = PDF(title=title, fingerprint=fingerprint, **fields)
        pdf.save()
