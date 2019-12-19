from flask import Blueprint, render_template
from models import Books

books_worker = Books()
feed_blueprint = Blueprint('books', __name__)

@feed_blueprint.route('/library', methods=['GET'])
def library_feed():

    return render_template('library.html', books = books_worker.get_books(refresh = True)) 

@feed_blueprint.route('/list', methods=['GET'])
def library_list():

    return render_template('library-list.html', books = books_worker.get_book_names(refresh = True))