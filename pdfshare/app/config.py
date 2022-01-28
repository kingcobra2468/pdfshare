from os.path import abspath, dirname
from os import getenv

# ---- Enviornment Config ------- #
APP_PARENT_DIR = dirname(abspath(__file__)) # Project Directory
BOOKS_DIR_SYSTEM = getenv('BOOKS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None \
    else f'{APP_PARENT_DIR}/static/books' # Book directory
COVERS_DIR_SYSTEM = getenv('COVERS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None \
    else f'{APP_PARENT_DIR}/static/covers' # Cover directory
DEFAULT_COVER_FILE = 'no_picture.png' # default photo for cover
# ---- Enviornment Config Ends -- #

# ---- Server Config ------------ #
PORT = 9000 # Port of the Server
# ---- Server Config Ends ------- #

# ---- Site Config  ------------- #
BOOKS_PER_ROW = 3 # Number of books per row when in gallery view
# ---- Site config Ends --------- #

# ---- MongoDB Config ------------#
MONGO_HOST = getenv('MONGO_HOST') if getenv('MONGO_HOST') is not None \
    else 'localhost' # mongodb host address
MONGO_PORT = getenv('MONGO_PORT') if getenv('MONGO_PORT') is not None \
    else 27017 # mongodb port
# ---- MongoDB Config Ends -------#