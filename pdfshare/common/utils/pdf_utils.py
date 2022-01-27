import os.path
import hashlib


def compute_pdf_hash(pdf_dir, pdf_name):
    sha256_hash = hashlib.sha256()

    with open(os.path.join(pdf_dir, f'{pdf_name}.pdf') , 'rb') as f:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256_hash.update(byte_block)

        return sha256_hash.hexdigest()
