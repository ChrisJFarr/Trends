# Flask API
from flask import Flask, render_template, make_response, request
from src.trend_search import TrendSearch
app = Flask(__name__)


DOCKER = True
mongo = "trends_mongo_1:27017" if DOCKER else None
trend_search = TrendSearch(mongo)


@app.route("/")
def home():
    # Call TrendFinder.list_collections
    # Build links for visualize with collection as param in each
    # Call in index.html
    collections = trend_search.list_collections()
    return render_template("index.html", collections=collections)


@app.route("/", methods=['POST'])
def search():
    # take argument from index.html text box
        # https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
    # Call TrendFinder.search
    # Refresh page
        # https://stackoverflow.com/questions/45666664/how-to-refresh-the-flask-web-page
    trend_search.search(request.form["text"])
    collections = trend_search.list_collections()
    return render_template('index.html', collections=collections)


@app.route("/visualize/<collection>")
def visualize(collection):
    # New page where only the image is returned, use back to get to home page
    # take argument for collection name
    # Render visual for collection
        # https://gist.github.com/wilsaj/862153
    png_output = trend_search.visualize(collection)
    response = make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
