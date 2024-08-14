#!/usr/bin/env python3
'''
9. Insert a document in Python
'''


def insert_school(mongo_collection, **kwargs):
    '''
    a Python function that inserts a new document in a collection based on kwargs
    '''
    mongo_collection.insert_one(kwargs)
    item = mongo_collection.find()
    return item['_id']
