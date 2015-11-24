import os

# *****************************
# Environment specific settings
# *****************************

# The settings below can (and should) be over-ruled by OS environment variable settings

# Flask settings                     # Generated with: import os; os.urandom(24)
SECRET_KEY = '\xcf^\x15\xcd\xe9\x04\xd9?\xac(\xf7\x98RQ\xa4\xcb<\xae\xb2SR\x11h\x7f'
# PLEASE USE A DIFFERENT KEY FOR PRODUCTION ENVIRONMENTS!

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/flask_registration'

# Flask settings
CSRF_ENABLED = True

SQLALCHEMY_TRACK_MODIFICATIONS =True

# Flask-Mail settings
MAIL_USERNAME =           ''
MAIL_PASSWORD =           ''
MAIL_DEFAULT_SENDER =     'noreply@vertisinfotech.com'
MAIL_SERVER =             'smtp.vertis'
MAIL_PORT =               ''
MAIL_USE_SSL =            False

# Flask-User settings
USER_APP_NAME        = "AppName"                # Used by email templates

ADMINS = [
    '"Sagar" <sagar.talekar@vertisinfotech.com>',
    ]

# Web-server related settings
PORT_NUMBER= 5000
DEBUG_FLAG= True