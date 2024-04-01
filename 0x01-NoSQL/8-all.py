#!/usr/bin/env python3
""" MongoDB Operations with Python"""


def list_all(mongo_collection):
    """Ls documents in python"""
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
