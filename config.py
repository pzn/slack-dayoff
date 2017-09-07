import os, pathlib


DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(pathlib.Path(__file__).parent) + '/db.sqlite'

SLACK_OAUTH_ACCESS_URL = 'https://slack.com/api/oauth.access'
SLACK_POST_MESSAGE_URL = 'https://slack.com/api/chat.postMessage'

SLACK_APP_CLIENT_ID = os.environ.get('SLACK_APP_CLIENT_ID', None)
SLACK_APP_CLIENT_SECRET = os.environ.get('SLACK_APP_CLIENT_SECRET', None)
