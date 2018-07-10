# Connect to pytrends
from pytrends.request import TrendReq
from matplotlib import pyplot as plt

pytrends = TrendReq()


kw_list = ["Blockchain"]
result = pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y')

check = pytrends.interest_over_time()
plt.plot(check["Blockchain"])
plt.title("Blockchain 5 Year History")
plt.ylabel("Search Count")
plt.xlabel("Date Range")