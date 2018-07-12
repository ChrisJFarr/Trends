from pytrends.request import TrendReq
from pymongo import MongoClient
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO

"""
@author Chris Farr
TrendSearch class is used for connecting to Google trends and writing search results back to a MongoDB.
"""


class TrendSearch:
    def __init__(self, mongo="trends_mongo_1:27017"):
        self.google_api = TrendReq()  # Connect to google API
        self.mongo_client = MongoClient(mongo)
        self.db = self.mongo_client.google_searches  # Connect to Mongo db
        return

    def search(self, query):
        """
        Accept a query from user, connect to google-trends and store data in a MongoDB.
        :param query: Text query, any string
        :return: None
        """
        # API data in dictionary format
        self.google_api.build_payload([query])
        data = self.google_api.interest_over_time()
        # Create collection name from query
        collection = self.db[query.replace(" ", "_").lower()]
        # Pre-process data for mongo input
        data.drop("isPartial", axis=1, inplace=True)
        data.columns = ["data"]
        data.reset_index(inplace=True)
        data = data.to_dict(orient='rows')
        # Store in new mongo collection, named by query all lower case with underscores no spaces
        collection.insert_many(data)
        return

    def visualize(self, collection):
        """
        Take argument for specific collection to query. Pull data from MongoDB. Create matplotlib visual
        and convert to bytes for rendering in Flask API.
        :param collection: string, collection name
        :return: BytesIO object
        """
        # Param: collection name
        # Query mongo and create data frame from output
        results = list(self.db[collection].find())
        # Convert to data frame
        df = pd.DataFrame(results)
        df.drop("_id", axis=1, inplace=True)
        df.set_index("date", inplace=True)
        df.sort_index(inplace=True)
        # Create matplotlib line graph, pretty up title remove underscores and proper capitalization
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(df)
        ax.set_title("%s 5 Year History" % collection.replace("_", " ").title())
        ax.set_ylabel("Popularity Score")
        ax.set_xlabel("Date Range")
        canvas = FigureCanvas(fig)
        png_output = BytesIO()
        canvas.print_png(png_output)
        return png_output

    def list_collections(self):
        """
        :return: Return list of collections in MongoDB
        """
        return sorted(self.db.list_collection_names())
