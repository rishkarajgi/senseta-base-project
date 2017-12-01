import os

API_V1_STR = '/api/v1'

CONTENT_TYPE_JSON = 'application/json'

SECRET_KEY = os.getenvb(b'SECRET_KEY')
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

SERVER_NAME = os.getenv('SERVER_NAME')
SENTRY_DSN = os.getenv('SENTRY_DSN')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')

FIRST_SUPERUSER = os.getenv('FIRST_SUPERUSER')
FIRST_SUPERUSER_PASSWORD = os.getenv('FIRST_SUPERUSER_PASSWORD')