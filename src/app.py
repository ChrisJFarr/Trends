# Flask API


from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)





"""
@author Chris Farr
The SearchEngine class is used for all search engine processes including indexing
and rating document relevance based on a query.
"""

# Build index (index_all, index_one)
#   pull fields and normalize: sps in db controls what is returned
#       spPortal_Search_Data: columns include (report_id, anything indexed)
#       Only active reports
#       Use search_controls table to filter to fields that need to be normalized
#       Return error message, create test, when fields are in search_controls and not in data
#   store in mongo with report id as primary key "_id"
#   driven by endpoints (/index_all, /index_one)
#   ensure no interruption to searching when indexing

# Consume index (search)
#   pull text for use in bm25
#   pass query from reports/
#   return df with scores for each search field
#   driven by reports endpoint
#   results combined with /reports output

# Modify index ()
#   table to determine search fields and weights
#       search_controls
#   easily modified without changes to code
#   include client-facing alias for search field



client = MongoClient("trends_mongo_1:27017")  # TODO this may change, investigate static
db = client.test_db
test = db.test_collection
test.insert_one({"data": "it works"})

@app.route("/")
def hello():
    output = test.find_one()["data"]
    return output

# Instantiate instance of TrendFinder
# list_collections
    # Call TrendFinder.list_collections
    # Build links for visualize with collection as param in each
    # Call in index.html
# visualize
    # New page where only the image is returned, use back to get to home page
    # take argument for collection name
    # Render visual for collection
        # https://gist.github.com/wilsaj/862153
# search
    # take argument from index.html text box
        # https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
    # Call TrendFinder.search
    # Refresh page
        # https://stackoverflow.com/questions/45666664/how-to-refresh-the-flask-web-page

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)


