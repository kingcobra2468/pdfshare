from os.path import abspath, expanduser, isdir, isfile
from re import findall, sub, match
from json import loads

SETTINGS_FILE_PATH = './settings/settings.json' #relative to run.py

class ConfigParser:

    def __init__(self):
        
        self.__load_json_file()
        self.__get_project_path(self.__settings['project_folder_name'])

    def __load_json_file (self):

        with open(SETTINGS_FILE_PATH, 'rb') as settings_file:
            self.__settings = loads(settings_file.read())
            print(self.__settings)

    def __get_project_path (self, project_dir):

        self.__project_abs_path = findall(f'.*{project_dir}', abspath(__file__))[0] #should give one element with app path

        if len(self.__project_abs_path) == 0:
            exit(f'FATAL ERROR: UNABLE TO FIND APP_PATH when searching for project dir: {project_dir}')

    def get_covers_dir (self):

        self.__settings['cover_dir'] = expanduser(self.__settings['cover_dir'])

        if match('{PROJECT_PATH}', self.__settings['cover_dir']):
            
            self.__settings['cover_dir'] = sub('{PROJECT_PATH}', self.__project_abs_path, self.__settings['cover_dir'])
            self.__settings['cover_dir_site'] = '/static/covers'

        elif not isdir(self.__settings['cover_dir']):
            exit(f'FATAL ERROR: INVALID/NONEXISTANT cover dir: {self.__settings["cover_dir"]}')

        else:
            self.__settings['cover_dir_site'] = f'file://{self.__settings["cover_dir"]}'

        return (self.__settings['cover_dir'], self.__settings['cover_dir_site']) 

    def get_books_dir (self):

        self.__settings['book_dir'] = expanduser(self.__settings['book_dir'])
        
        if match('{PROJECT_PATH}', self.__settings['book_dir']):
            
            self.__settings['book_dir'] = sub('{PROJECT_PATH}', self.__project_abs_path, self.__settings['book_dir'])
            self.__settings['book_dir_site'] = '/static/books'

        elif not isdir(self.__settings['book_dir']):
            exit(f'FATAL ERROR: INVALID/NONEXISTANT book dir: {self.__settings["book_dir"]}')

        else:
            self.__settings['book_dir_site'] = f'file://{self.__settings["book_dir"]}'

        return (self.__settings['book_dir'], self.__settings['book_dir_site']) 

    # WARNING ORDER MATTERS WITH get_cover_dir() being expected to be called first to verify that self.__settings['cover_dir']
    # is a valid directory
    def get_cover_photo (self):

        if match('{COVER_DIR}', self.__settings['default_cover_photo']):
            self.__settings['default_cover_photo'] = sub('{COVER_DIR}', self.__settings['cover_dir'], self.__settings['default_cover_photo'])

        elif not isfile(self.__settings["default_cover_photo"]):
            exit(f'FATAL ERROR: INVALID/NONEXISTANT default_cover_photo: {self.__settings["default_cover_photo"]}')

        return self.__settings['default_cover_photo']

#PROJECT_PATH = get_app_path() # will no longer need once config is done
config = ConfigParser()

[COVERS_DIR_SYSTEM, COVERS_DIR_SITE] = config.get_covers_dir() # COVERS_DIR_SYSTEM relative to system |  = #COVERS_DIR_SITE relative to website
[BOOKS_DIR_SYSTEM, BOOKS_DIR_SITE] = config.get_books_dir() # BOOKS_DIR_SYSTEM relative to system |  = #BOOKS_DIR_SITE relative to website
DEFAULT_COVER_FILE = config.get_cover_photo()