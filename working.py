# Connect to pytrends
from pytrends.request import TrendReq
from matplotlib import pyplot as plt
from pymongo import MongoClient

pytrends = TrendReq()


kw_list = ["Taylor Swift"]
result = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y')

check = pytrends.interest_over_time()
plt.plot(check["Taylor Swift"])
plt.title("Blockchain 5 Year History")
plt.ylabel("Search Count")
plt.xlabel("Date Range")


# Store results in Mongo
df = pytrends.interest_over_time()
mongo_client = MongoClient()
db = mongo_client.google_searches
mongo_client.list_database_names()


df.drop("isPartial", axis=1, inplace=True)
df.columns = ["data"]
df.reset_index(inplace=True)

data = df.to_dict(orient='rows')

db.blockchain.insert_many(check)

db.drop_collection("blockchain")

# Pull results in Mongo
results = db.blockchain.find()
results = list(results)
# Convert back to DF
import pandas as pd
new_df = pd.DataFrame(results)
new_df.drop("_id", axis=1, inplace=True)
new_df.set_index("date", inplace=True)
# Create visualization

plt.plot(new_df)
plt.title("Blockchain 5 Year History")
plt.ylabel("Search Count")
plt.xlabel("Date Range")

query = "Taylor Swift"
google_api = pytrends
google_api.build_payload([query])
data = google_api.interest_over_time()
# Create collection name from query
collection = db[query.replace(" ", "_").lower()]
# Preprocess data for mongo input
data.drop("isPartial", axis=1, inplace=True)
data.columns = ["data"]
data.reset_index(inplace=True)
data = data.to_dict(orient='rows')
# Store in new mongo collection, named by query all lower case with underscores no spaces
collection.insert_many(data)


# Test plot
from src.trend_search import TrendSearch
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

ts = TrendSearch(None)
ts.search("Taylor Swift")
plot = ts.visualize("taylor_swift")
plot.imshow
canvas = FigureCanvas(fig)
png_output = StringIO.StringIO()
canvas.print_png(png_output)
response = make_response(png_output.getvalue())
response.headers['Content-Type'] = 'image/png'

