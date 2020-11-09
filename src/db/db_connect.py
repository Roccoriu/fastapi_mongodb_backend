from pymongo import MongoClient
from pymongo.errors import ConfigurationError
from dns.exception import Timeout as DnsTimeout

from os import getenv

try:
    def connect_db(db_name: str):
        client = MongoClient(getenv('MONGO_CONNECTION_STRING'))

        return client[str(db_name)]

except ConfigurationError:
    print('Failed to connect to DB')

except DnsTimeout:
    print('DNS opretation failed')
