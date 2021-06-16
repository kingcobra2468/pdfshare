from os.path import abspath, dirname
from os import getenv
from re import findall, sub, match
from json import loads

# ---- Enviornment Config ------- #
APP_PARENT_DIR = dirname(abspath(__file__)) # Project Directory
BOOKS_DIR_SYSTEM = getenv('BOOKS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None \
    else f'{APP_PARENT_DIR}/static/books' # Book directory
COVERS_DIR_SYSTEM = getenv('COVERS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None \
    else f'{APP_PARENT_DIR}/static/covers' # Cover directory
DEFAULT_COVER_FILE = f'{APP_PARENT_DIR}/static/covers/no_picture.png' # default photo for cover
# ---- Enviornment Config Ends -- #

# ---- Server Config ------------ #
PORT = 9000 # Port of the Server
# ---- Server Config Ends ------- #

# ---- Site Config  ------------- #
BOOKS_PER_ROW = 3 # Number of books per row when in gallery view
# ---- Site config Ends --------- #

# ---- MongoDB Config ------------#
MONGO_HOST = 'localhost'
MONGO_PORT = 27018
# ---- MongoDB Config Ends -------#