import os

URL = os.environ.get('MAILGUN_URL') # stored as Heroku environment (config) variables
API_KEY = os.environ.get('MAILGUN_API_KEY')
FROM = os.environ.get('MAILGUN_FROM')
ALERT_TIMEOUT = 10
COLLECTION = "alerts"