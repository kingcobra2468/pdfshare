from mongoengine import connect

from pdfshare.common.models.pdf import PDF


class PDFLibrary:
    """Wrapper on top of mongoengine for PDFs.
    """

    def __init__(self, host, port):
        """Constructor.

        Args:
            host (str): Hostname of the MongoDB server.
            port (int): Port of the MongoDB server.
        """
        self._connect(host, port)

    def _connect(self, host, port):
        """Establishes a connection with the MongoDB server.

        Args:
            host (str): Hostname of the MongoDB server.
            port (int): Port of the MongoDB server.
        """
        self.client = connect(host=host, port=port, db='pdfshare')

    def get_all_pdfs(self, size=None, offset=None):
        """Fetches all of the pdfs in the database. The set of returned PDFs
        can be filtered if pagination is active.

        Args:
            size (int, optional): Number of PDFs in the pagination. Defaults to None if pagination
            is not used.
            offset (int, optional): Offset of the current pagination. Defaults to None if pagination
            is not used.

        Returns:
            list(pdfshare.common.models.pdf.PDF): List of returned PDF documents.
        """
        if None in [size, offset]:
            return PDF.objects.exclude('id')

        return PDF.objects.skip(offset).limit(size).exclude('id')

    def get_pdf_count(self):
        """Retrieves the number of PDFs in the database.

        Returns:
            int: Number of PDFs.
        """
        return PDF.objects.count()

    def check_pdf_exists(self, **query):
        """Checks if a given PDF exists based on query criteria.

        Returns:
            bool: True if PDF exists, false otherwise.
        """
        result = PDF.objects(**query).count()
        return bool(result)

    def get_pdf(self, **query):
        """Gets a given PDF based on query criteria.

        Returns:
            pdfshare.common.models.pdf.PDF|None: Fetched PDF if exists.
        """
        return PDF.objects(**query).first()

    def insert_pdf(self, title, fingerprint, **fields):
        """Inserts a given PDF into the database.

        Args:
            title (str): Title of the PDF.
            fingerprint (str): SHA256 fingerprint of the PDF.
        """
        if self.check_pdf_exists(title=title, fingerprint=fingerprint):
            return

        pdf = PDF(title=title, fingerprint=fingerprint, **fields)
        pdf.save()
