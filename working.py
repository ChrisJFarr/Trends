# Connect to pytrends
from pytrends.request import TrendReq
from matplotlib import pyplot as plt
from pymongo import MongoClient

pytrends = TrendReq()


kw_list = ["Blockchain"]
result = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y')

check = pytrends.interest_over_time()
plt.plot(check["Blockchain"])
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
