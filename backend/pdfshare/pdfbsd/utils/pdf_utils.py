from os import system
import os.path

from PIL import Image
import shlex


def create_pdf_cover(pdf_dir, covers_dir, pdf_name):
    """Generates a cover for a book by using the first page of the pdf.

     Args:
        pdf_dir (str): Directory where the books are located.
        covers_dir (str): Directory where the book covers are located.
        pdf_name (str): Name of the PDF file.

     Returns:
        int: Result of the internal system subprocess.
        0 if no errors and non-zero value upon failure.
    """
    pdf_cover_path_png = os.path.join(covers_dir, f'{pdf_name}.png')
    pdf_cover_path_jpeg = os.path.join(covers_dir, f'{pdf_name}.jpeg')

    status = system(f'pdftoppm -f 1 -l 1 -png {shlex.quote(os.path.join(pdf_dir, f"{pdf_name}.pdf"))} > {shlex.quote(pdf_cover_path_png)}')

    if status:
        return status

    img = Image.open(pdf_cover_path_png)
    img.save(pdf_cover_path_jpeg, optimize=True, quality=70)

    os.remove(pdf_cover_path_png)

def extract_pdf_name(path):
    """Extracts the pdf filename from a given input path.

    Args:
        path (str): Path including the pdf file.

    Returns:
        str: Name of the pdf.
    """
    title = os.path.basename(path)
    if '.pdf' != title[-4:]:
        return None

    return title[:-4]
