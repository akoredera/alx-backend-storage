#!/usr/bin/env python3
'''Python script that provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient

if __name__ == "__main__":
    '''Python script that provides some stats about Nginx logs stored in MongoDB'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_collection = client.logs.nginx
    n_logs = db_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = db_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = db_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{status_check} status check')
