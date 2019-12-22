from flask import Blueprint, request, Response, render_template, make_response, send_from_directory
from utils import BOOKS_DIR_SYSTEM
from os.path import isfile

download_blueprint = Blueprint('download_books', __name__)

@download_blueprint.route('/download', methods=['GET'])
def download_book():

    book_name = None

    try:

        book_name = request.args.get('book')
    except ValueError:
        pass
    #query arguement doesnt exist
    if not book_name:

        response = make_response(('book query arg missing', 400))
        return response

    elif not isfile(f'{BOOKS_DIR_SYSTEM}/{book_name}'):

        response = make_response((f'book {book_name} doesnt exist', 400))
        return response

    else:

        print(f"{Blueprint}/{book_name}")
        return send_from_directory(directory = BOOKS_DIR_SYSTEM, filename = book_name, as_attachment=True, attachment_filename = book_name) #static/books