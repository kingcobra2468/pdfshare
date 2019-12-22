from flask import Blueprint, render_template
from models import Books
from settings import BOOKS_DIR_SITE, COVERS_DIR_SITE

books_worker = Books()
feed_blueprint = Blueprint('books', __name__)

@feed_blueprint.route('/library', methods=['GET'])
def library_feed():

    return render_template('library.html', books = books_worker.get_books(refresh = True), covers_dir_site = COVERS_DIR_SITE, books_dir_site = BOOKS_DIR_SITE) 

@feed_blueprint.route('/list', methods=['GET'])
def library_list():

    return render_template('library-list.html', books = books_worker.get_book_names(refresh = True))