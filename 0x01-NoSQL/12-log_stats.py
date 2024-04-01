#!/usr/bin/env python3

"""Module built o the previous files"""

from pymongo import MongoClient


def dump_nginx_req_data(nginx_data):
    """Output request data"""
    http_methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print(f'{nginx_data.estimated_document_count()} logs')
    print('Methods:')
    for method in http_methods:
        method_counter = nginx_data.count_documents({'method': method})
        print(f'\tmethod {method}: {method_counter}')
    stat_count = nginx_data.count_documents(
        {'method': 'GET', 'path': '/status'})
    print(f'{stat_count} status check')


def runMain():
    """Run MongoClient"""
    mongodb = MongoClient('mongodb://127.0.0.1:27017')
    dump_nginx_req_data(mongodb.logs.nginx)


if __name__ == '__main__':
    runMain()
