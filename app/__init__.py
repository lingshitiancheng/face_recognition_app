from flask import Flask
import os

# Config Values
# location where file uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'
# needed for session security, the flash() method in this case stores the message
# in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'
from app import views
