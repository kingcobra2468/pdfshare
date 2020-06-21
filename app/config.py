from os.path import abspath, dirname
from os import getenv
from re import findall, sub, match
from json import loads

APP_PARENT_DIR = dirname(abspath(__file__))

class Config:
    BOOKS_DIR_SYSTEM = getenv('BOOKS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None else f'{APP_PARENT_DIR}/static/books'
    COVERS_DIR_SYSTEM = getenv('COVERS_DIR_SYSTEM') if getenv('BOOKS_DIR_SYSTEM') is not None else f'{APP_PARENT_DIR}/static/covers'
    DEFAULT_COVER_FILE = f'{APP_PARENT_DIR}/static/covers/no_picture.png'
    PORT=9000
