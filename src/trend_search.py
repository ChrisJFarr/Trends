from pytrends.request import TrendReq
from pymongo import MongoClient


"""
@author Chris Farr
TrendSearch class is used for connecting to Google trends and writing data
back to a MongoDB.

Resources:
# https://github.com/GeneralMills/pytrends#connect-to-google
"""


class TrendSearch:
    def __init__(self):
        self.google_api = TrendReq()  # Connect to google API
        self.mongo_client = MongoClient("trends_mongo_1:27017")  # Connect to Mongo db
        return

    def search(self, query):
        # Param: text query
        # API data in dictionary format
        # Store in new mongo collection, named by query all lower case with underscores no spaces
        pass

    def visualize(self, collection):
        # Param: collection name
        # Query mongo and create data frame from output
        # Create matplotlib line graph, pretty up title remove underscores and proper capitalization
        # Return image, matplotlib visual
        pass

    def list_collections(self):
        # Param: none
        # Get list of collection names from mongo
        # Return list
        pass


"""
client = MongoClient("trends_mongo_1:27017")
db = client.test_db
test = db.test_collection
test.insert_one({"data": "it works"})


@app.route("/")
def hello():
    output = test.find_one()["data"]
    return output

"""