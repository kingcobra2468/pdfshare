from flask import Flask

from pdfshare.app.models.pdf_library_client import pdf_library_client
from pdfshare.app.routes import pdf_blueprint#, download_blueprint

app = Flask(__name__)

app.config.from_pyfile('config.py')

pdf_library_client.init_app(app)
app.register_blueprint(pdf_blueprint, url_prefix='/v1')
#app.register_blueprint(download_blueprint, url_prefix='/library')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = app.config['PORT'], debug = False)
