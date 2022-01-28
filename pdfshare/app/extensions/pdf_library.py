from pdfshare.common.clients.pdf_library import PDFLibrary as PDFLibraryClient


class PDFLibrary:
    """Flask extension for interacting with PDF library.
    """
    
    def __init__(self, app = None, config_prefix="PDFLibrary"):
        """Constructor.

        Args:
            app (Flask, optional): Instance of Flask app. Defaults to None.
            config_prefix (str, optional): Name of extension to be
                registered by flask. Defaults to "BooksDB".
        """
        self.__config_prefix = config_prefix
        self.client = None

        if app is not None:
            self.client = PDFLibraryClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])

    def init_app(self, app):
        """Initialized and registers the extension with Flask.

        Args:
            app (Flask): Instance of Flask app.
        """
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions[self.__config_prefix.lower()] = self
        
        if not self.client:
            self.client = PDFLibraryClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'])
    
    def get_pdf_pagination(self, size=None, offset=None):
        return self.client.get_all_pdfs(size, offset)
