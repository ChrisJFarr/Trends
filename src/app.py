# Flask API
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

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)


