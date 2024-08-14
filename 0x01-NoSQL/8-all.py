#!/usr/bin/env python3
'''
8. List all documents in Python
'''
from pymongo import MongoClient

def list_all(mongo_collection):
    '''
    Python function that lists all documents in a collection:
    '''
    list_doc = mongo_collection.find()

    if list_doc:
        return list_doc
    else:
        return []
