from flask import Flask, redirect, url_for
from models.book_db_client import books_db_client
from routes import feed_blueprint, download_blueprint

app = Flask(__name__)
app.config.from_object('config.Config')
books_db_client.init_app(app)

app.register_blueprint(feed_blueprint, url_prefix='/library')
app.register_blueprint(download_blueprint, url_prefix='/library')


@app.before_first_request
def before_first_request():
    books_db_client.load_books()

@app.route('/')
def home(): #root will be redirected to library page
    return redirect('/library/gallary-view')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=app.config['PORT'], debug=False)
