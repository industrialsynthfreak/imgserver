"""
Server configuration vars. Please, modify them wisely.

HOST, PORT - server host and server port
LOG - server log relative or absolute path
SECRET_KEY - a key used in cookies
DEAD_TIME - a minimal time period in seconds between two unique snapshots
IMG_TYPE - extension used for new images (ensure that your cam software can
    actually save in this format)
IMG_PATH - path where all cam images will be stored
DEFAULT_IMG
SCRIPT_PATH
DEBUG - enables / disables debug mode
"""

HOST = 'localhost'
PORT = 8080
LOG = 'server.log'

SECRET_KEY = 'Wow-its-really-The-secret'

DEAD_TIME = 10
IMG_TYPE = 'jpg'
IMG_PATH = 'static/img'
DEFAULT_IMG = 'dawg.jpg'
SCRIPT_PATH = './camera_access.sh'
DEBUG = False