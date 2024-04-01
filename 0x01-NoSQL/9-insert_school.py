#!/usr/bin/env python3
""" MongoDB Operations with Python"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document"""
    return mongo_collection.insert(kwargs)
