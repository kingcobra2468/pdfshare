from flask import Blueprint, render_template, current_app
from models.book_db_client import books_db_client 

feed_blueprint = Blueprint('books', __name__)

@feed_blueprint.route('/gallary-view', methods=['GET'])
def library_feed():

    return render_template('gallary-view.html', books = books_db_client.get_books(refresh = True),
        covers_dir_site = '/static/covers', books_dir_site = '/static/books') 

@feed_blueprint.route('/list-view', methods=['GET'])
def library_list():

    return render_template('list-view.html', books = books_db_client.get_book_names(refresh = True))