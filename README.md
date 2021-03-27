# PDFShare

#### A simple online pdf viewing, downloading, and distrubuting website built with Flask.

## **WebUI**

### **Gallery View**

![Alt text](./screenshots/gallery_view_light.png "Gallery View Light Theme")

Accessible under `<hostname>/` or `<hostname>/library/gallery-view`, gallery view allows one to view their pdf's visually via the covers of the pdfs. Clicking the cover will open the pdf up in the browser's built-in pdf viewer. 

### **List View**

![Alt text](./screenshots/list_view_light.png "Gallery View Light Theme")

Accessible under `<hostname>/library/list-view`, list view gives a continuous list of all the names of the pdfs. Clicking any of the links behind the pdf will prompt the user with the download request to download the pdf onto the local machine.

### **Dark Mode**

It is possible to toggle dark mode site-wide using the config box in the top right corner of the screen.

*Gallery view in dark mode:*
![Alt text](./screenshots/gallery_view_dark.png "Gallery View Light Theme")

*List view in dark mode:*
![Alt text](./screenshots/list_view_dark.png "Gallery View Light Theme")

## **Configuration**
The `config.cfg` file under `/app` stores global configuration details and constants used throughout the program. Settings in the `config.cfg` file include:
- **BOOKS_DIR_SYSTEM=** path where pdfs are stored.
- **COVERS_DIR_SYSTEM=** path where pdf png covers are stored.
- **DEFAULT_COVER_FILE=** default cover photo is error arised and one cannot be genereted.
- **PORT=** port of flask server. *Note changing this will necessitates changes to gunicorn_config.py, Dockerfile, and docker-compose.yml files*
- **BOOKS_PER_ROW=** number of books for row when in gallery view. Must be between [1,3].

## **Installation**

*Note installation assumes apt package manager is  pre-installed. Modify as needed for other package managers.*

### **Without Docker**
1. Run `apt-get install poppler-utils gunicorn python3` .
2. Install python packages with `pip3 install -r requirements.txt` .
3. Run `python3 main.py`
4. (Optional). Run over gunicorn WSGI with `gunicorn -c gunicorn_config.py wsgi:app` . 

### **With Docker**
1. Create directory called `~/Books/` and place all pdfs there. Alternate dirs require changing `docker-compose.yml`.
2. Build containers `docker-compose build`
3. Start PDFShare with `docker-compose up -d`. 