import logging
import os

from django.contrib.auth.models import User
from pymongo import MongoClient, errors

logger = logging.getLogger('basiclogger')

# MongoDB settings
#MONGO_HOST = os.environ.setdefault('MONGO_HOST', 'localhost')
#MONGO_PORT = os.environ.setdefault('MONGO_PORT', '27017')
#MONGO_USER = os.environ.get('MONGO_USER')
#MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
#MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO = os.environ.setdefault('MONGO', 'mongodb://localhost:27017')

try:
    client = MongoClient(MONGO)
    usernames = client['Gateway']['jhi_user'].distinct('login')
    print(usernames)
    for username in usernames:
        print(username)
        auser = User.objects.create_user(username, password='django')
        auser.is_superuser = True
        auser.is_staff = True
        auser.save()
except errors as e:
    logger.error(".jhipsterusertodjango.py : mongoDB not connected, check your database configuration")
    raise e
