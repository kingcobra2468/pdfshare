from os import system
import os.path

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
    pdf_name = shlex.quote(pdf_name)  # sanitize name
    return system(f'pdftoppm -f 1 -l 1 -png {os.path.join(pdf_dir, f"{pdf_name}.pdf")} >' +
                  f'{os.path.join(covers_dir, f"{pdf_name}.png")}')


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
