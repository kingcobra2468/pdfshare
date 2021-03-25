from flask import Blueprint, render_template, current_app
from models.book_db_client import books_db_client 

feed_blueprint = Blueprint('books', __name__)

@feed_blueprint.route('/gallary-view', methods=['GET'])
def library_feed():
    """Generates the gallery page
    """
    row_size = current_app.config['BOOKS_PER_ROW']
    row_size = row_size if row_size <= 3 and row_size >= 1 else 1 # validation

    books = books_db_client.get_books(refresh = True)

    # build the sets of books per row
    book_groups = [books[i:i + row_size] for i in range(0, len(books), row_size)]

    return render_template('gallary-view.jinja2', row_size = row_size, book_groups = book_groups,
        covers_dir_site = '/static/covers', books_dir_site = '/static/books') 

@feed_blueprint.route('/list-view', methods=['GET'])
def library_list():
    """Generates the list page
    """
    return render_template('list-view.jinja2', books = books_db_client.get_book_names(refresh = True))