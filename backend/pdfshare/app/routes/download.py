from os.path import isfile, join

from flask import Blueprint, request, make_response, send_from_directory, \
    current_app

from pdfshare.app.models.pdf_library_client import pdf_library_client

download_blueprint = Blueprint('download_books', __name__)


@download_blueprint.route('/download', methods=['GET'])
def download_book():
    """Downloads a given pdf by its title.
    """
    # get pdf title
    title = request.args.get('pdfTitle', None)

    # query argument doesn't exist
    if not title:
        return make_response(('pdf query argument pdfTitle is missing', 400))

    pdf = pdf_library_client.get_pdf_by_title(title)
    if not pdf:
        return make_response(('pdf not found', 400))

    pdf_file = f'{pdf.title}.pdf'
    pdf_path = join(current_app.config['BOOKS_DIR_SYSTEM'], pdf_file)
    print(pdf_file, pdf_path, isfile(pdf_path))
    if not isfile(pdf_path):
        return make_response((f'pdf "{pdf.title}" does not exist', 400))

    return send_from_directory(directory=current_app.config['BOOKS_DIR_SYSTEM'], path=pdf_file,
                               as_attachment=True, attachment_filename=pdf.title)
