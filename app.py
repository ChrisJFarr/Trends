# Flask API
from flask import Flask, render_template, make_response, request
from src.trend_search import TrendSearch

"""
@author Chris Farr
This application renders a simple API that take search queries and passes them to google-trends. The results
are stored in a MongoDB and displayed in a line graph when clicking on the corresponding link.
"""

app = Flask(__name__)

DOCKER = True
mongo = "trends_mongo_1:27017" if DOCKER else None
trend_search = TrendSearch(mongo)


@app.route("/")
def home():
    """
    Home page when form submit not used.
    :return:
    """
    collections = trend_search.list_collections()
    return render_template("index.html", collections=collections)


@app.route("/", methods=['POST'])
def search():
    """
    Accept post request for new search, update template with new collection list
    :return: Return home page
    """
    trend_search.search(request.form["text"])
    collections = trend_search.list_collections()
    return render_template('index.html', collections=collections)


@app.route("/visualize/<collection>")
def visualize(collection):
    """
    Render visual for collection. Directs to page where only the image is returned, use back to get to home page
    :param collection: collection or search name
    :return:
    """
    png_output = trend_search.visualize(collection)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
