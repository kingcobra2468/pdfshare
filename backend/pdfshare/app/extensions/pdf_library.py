from pdfshare.common.clients.pdf_library import PDFLibrary as PDFLibraryClient


class PDFLibrary:
    """Flask extension for interacting with PDF library.
    """

    def __init__(self, app=None, config_prefix="PDFLibrary"):
        """Constructor.

        Args:
            app (Flask, optional): Instance of Flask app. Defaults to None.
            config_prefix (str, optional): Name of extension to be
                registered by flask. Defaults to "PDFLibrary".
        """
        self.__config_prefix = config_prefix
        self.client = None

        if app is not None:
            self.client = PDFLibraryClient(
                app.config['MONGO_HOST'], app.config['MONGO_PORT'])

    def init_app(self, app):
        """Initializes and registers the extension with Flask.

        Args:
            app (Flask): Instance of Flask app.
        """
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.__config_prefix.lower()] = self

        if not self.client:
            self.client = PDFLibraryClient(
                app.config['MONGO_HOST'], app.config['MONGO_PORT'])

    def get_pdf_pagination(self, size, offset):
        """Fetches new PDFs relative to the path of the client. 

        Args:
            size (int, optional): Number of PDFs in the pagination.
            offset (int, optional): Offset of the current pagination.

        Returns:
            list(pdfshare.common.models.pdf.PDF): List of returned PDF documents.
        """
        return self.client.get_all_pdfs(size, offset)

    def get_pdf_by_title(self, title):
        """Retrieves a given PDF by its title.

        Args:
            title (str): Title of the PDF.

        Returns:
            pdfshare.common.models.pdf.PDF|None: PDF if it exists.
        """
        if not self.client.check_pdf_exists(title=title):
            return None

        return self.client.get_pdf(title=title)
