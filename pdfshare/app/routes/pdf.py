from flask import Blueprint, request
from flask_cors import cross_origin

from pdfshare.app.models.pdf_library_client import pdf_library_client

pdf_blueprint = Blueprint('pdf', __name__)


@pdf_blueprint.route('/pdfs', methods=['GET'])
@cross_origin()
def library_feed():
    """Generates the gallery page.
    """
    page_size = request.args.get('size', None, int)
    offset = request.args.get('offset', None, int)

    pdfs = pdf_library_client.get_pdf_pagination(page_size, offset)

    return pdfs.to_json()
