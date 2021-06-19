from pdfshare.app.models.book_db_client import books_db_client
from pdfshare.app.routes import feed_blueprint, download_blueprint
from flask import Flask, redirect, url_for

app = Flask(__name__)

app.config.from_pyfile('config.py')
books_db_client.init_app(app)

app.register_blueprint(feed_blueprint, url_prefix='/library')
app.register_blueprint(download_blueprint, url_prefix='/library')

@app.route('/')
def home(): #root will be redirected to library page
    return redirect(url_for('books.library_feed'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = app.config['PORT'], debug = False)
