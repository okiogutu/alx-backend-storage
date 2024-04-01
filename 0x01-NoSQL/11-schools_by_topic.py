#!/usr/bin/env python3

"""how to filter docs for mongodb"""


def schools_by_topic(mongo_collection, topic):
    """Find a collection of schools"""
    filtered_topic = {'topics': {'$elemMatch': {'$eq': topic}}}
    return [res for res in mongo_collection.find(filtered_topic)]
