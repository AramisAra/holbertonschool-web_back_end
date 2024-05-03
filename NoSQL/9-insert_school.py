#!/usr/bin/env python3
""" MongoDB operations with Python """


def insert_school(mongo_collection, **kwargs):
    """ Insert a document in Python based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id