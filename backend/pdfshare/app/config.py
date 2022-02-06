from os.path import abspath, dirname
from os import getenv

# ---- Environment Config ------- #
APP_PARENT_DIR = dirname(abspath(__file__))  # project directory
BOOKS_DIR_SYSTEM = getenv(
    'BOOKS_DIR_SYSTEM', f'{APP_PARENT_DIR}/static/books')  # pdf directory
COVERS_DIR_SYSTEM = getenv(
    'COVERS_DIR_SYSTEM', f'{APP_PARENT_DIR}/static/covers')  # cover directory
# ---- Environment Config Ends -- #

# ---- Server Config ------------ #
PORT = 9000  # Port of the Server
# ---- Server Config Ends ------- #

# ---- MongoDB Config ------------#
MONGO_HOST = getenv('MONGO_HOST', 'localhost')  # mongodb host address
MONGO_PORT = getenv('MONGO_PORT', 27017)  # mongodb port
# ---- MongoDB Config Ends -------#
