from enum import Enum

from pymongo import MongoClient


class DatabaseTypes(Enum):
    MONGODB = 1

class DatabaseNames(Enum):
    python_test_db = 'python_test_db'

class Collections(Enum):
    member = 'member'


def connect_to_db(db_type, uri, db_name):
    if db_type == DatabaseTypes.MONGODB:
        return MongoClient(uri)[db_name]
    return None
