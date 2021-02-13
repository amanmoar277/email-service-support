"""These are used app wide
"""

# Now we load this file variable as object and assign it to app.config in __init__.py
from .load_config import load_settings
settings = load_settings()

# app relaed settings
ENV = settings["ENV"]
APP_PORT = settings["APP_PORT"]
APP_NAME = settings["APP_NAME"]
DEBUG = settings["DEBUG"]

# mongo related settings
MONGODB_URI = settings["MONGODB_URI"]
MONGODB_NAME = settings["MONGODB_NAME"]
SECRET_KEY = settings["SECRET_KEY"]