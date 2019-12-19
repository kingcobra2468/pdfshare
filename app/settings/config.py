from os.path import abspath
from re import findall

def get_app_path(project_dir = 'app'):

    abs_path = abspath(__file__)
    app_path = findall(f'.*{project_dir}', abs_path) #should give one element with app path

    if len(app_path) == 0:

        exit (f'FATAL ERROR: UNABLE TO FIND APP_PATH when searching for project dir: {project_dir}')
    
    return app_path[0]
    
PROJECT_PATH = get_app_path() 
COVERS_DIR = f'{PROJECT_PATH}/static/covers' #under project dir
BOOKS_DIR = f'{PROJECT_PATH}/static/books' #under project dir
DEFAULT_COVER_FILE = 'no_picture.png'