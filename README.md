# PDFShare
</h4>A simple online pdf viewing, downloading, and distrubuting website built with Flask</h4>

<h5>Routes</h5>
<em>/ or /library</em>

Will display the covers of every pdf with link to download it. When clicking cover, the pdf will be opened within the browser

<em>/list</em>

Will display the name of the pdfs in list view which when clicked will prompt to download the pdf

<h5>settings.json</h5>

<h6>project_folder_name</h6>
"project_folder_name" : "app" 

The root folder of the project

<h6>book_dir</h6>
"book_dir" : "{PROJECT_PATH}/static/books" 

The directory were the pdfs are held. Notice {PROJECT_PATH} is an alias(case matters) and is evaluated by the ConfigParser in config.py as **/program_folder_name
This setting could be changed to a valid and accessible(adequate permissions) path containing pdfs in the filesystem

<em> WARNING: </em> Due to the nature and security risks that arise when opening file://* files in the browser, a book dir other than {PROJECT_PATH}/static/books will
result in the loss of this feature in the <em>/</em> or <em>/library</em> pages: 
pdf will be opened within the browser. It is suggested to use the <em>/list</em> page in this case, as pdf name & downloading will not be affected.

<h6>cover_dir</h6>
"cover_dir" : "{PROJECT_PATH}/static/covers" 
 
The directory were the pdf covers are held. Notice {PROJECT_PATH} is an alias(case matters) and is evaluated by the ConfigParser in config.py as **/program_folder_name
This setting could be changed to a valid and accessible(adequate permissions) path containing pdfs in the filesystem

<em> WARNING: </em> Due to the nature and security risks that arise when opening file://* files in the browser, a cover dir other than {PROJECT_PATH}/static/cover will
result in the loss of this feature: display the covers of every pdf in the <em>/</em> or <em>/library</em> pages:
It is suggested to use the <em>/list</em> page in this case, as pdf name & downloading will not be affected.

<h6>default_cover_photo</h6>
"cover_dir" : "{COVER_DIR}/no_picture.png" 

The directory were the pdf covers are held. Notice {COVER_DIR} is an alias(case matters) and is evaluated by the ConfigParser in config.py as **/cover_dir
This setting could be changed to a valid and accessible(adequate permissions) path containing pdfs in the filesystem

<em> WARNING: </em> Due to the nature and security risks that arise when opening file://* files in the browser, a cover dir other than {COVER_DIR}/no_picture.png will
result in the loss of this feature: display the default no cover available for select pdf in the <em>/</em> or <em>/library</em> pages:
It is suggested to use the <em>/list</em> page in this case, as pdf name & downloading will not be affected.