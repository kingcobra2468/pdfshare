from os import system, listdir
from settings import COVERS_DIR, BOOKS_DIR, DEFAULT_COVER_FILE

def pdf_cover_to_png (pdf_name):

    try:
        
        if pdf_name.index('.pdf'):
            pdf_name = pdf_name.strip('.pdf')
    except ValueError:

        pass

    return system(f'pdftoppm -f 1 -l 1 -png {BOOKS_DIR}/{pdf_name}.pdf > {COVERS_DIR}/{pdf_name}.png') #returns 0 if no errors else there are errors