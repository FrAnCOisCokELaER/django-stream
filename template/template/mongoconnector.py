# -*- coding: utf-8 -*-
"""
Created on Wed Dec 5 09:29:34 2018

@author: cokelaef
"""
import logging

from django.conf import settings
from pymongo import MongoClient, errors

"""
    MongoConnector Class 
    ----------
    Handle basic connection for mongoDB
"""
logger = logging.getLogger('basiclogger')


class Mongosettings:
    def __init__(self):
        self.MONGO_DBNAME = settings.MONGO_DBNAME
        self.MONGO = settings.MONGO


mongo_settings = Mongosettings()


class MongoConnector():
    def __init__(self, dbname=None, mongo = None):
        self.mongo = mongo
        self.client = None
        self.db = None

        if dbname:
            self.dbname = dbname
        else:
            self.dbname = None


    def __enter__(self):
        try:
            self.client = MongoClient(self.mongo, serverSelectionTimeoutMS=200)
            if self.dbname:
                self.db = self.client[self.dbname]
            else:
                self.db = self.client[__name__.split('.')[0]]
            return self
        except errors as e:
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()


def insertdocument(document, collection=None):
    with MongoConnector(mongo_settings.MONGO_DBNAME, mongo_settings.MONGO) as connector:
        if collection == None:
            collection = 'transaction'
        try:
            collection = connector.db[collection]
            return collection.insert_one(document).inserted_id
        except Exception as e:
            if settings.DEBUG == True:
                logger.warning(".mongoconnector.py : connector info {0}, {1}".format(connector.client, connector.db))
                logger.warning(".mongoconnector.py : {0}".format(e))
            else:
                logger.error(".mongoconnector.py : connector info {0}, {1}".format(connector.client, connector.db))
                logger.error(".mongoconnector.py : {0}".format(e))
                raise e
