# •	Flask API
    # o	Instantiate instance of TrendFinder
    # o	list_collections
        # 	Call TrendFinder.list_collections
        # 	Return list
        # 	Build links for visualize with collection as param in each
        # 	Call in index.html
    # o	visualize
        # 	New page where only the image is returned, use back to get to home page
        # 	take argument for collection name
        # 	Render visual for collection
            # •	https://gist.github.com/wilsaj/862153
    # o	search
        # 	take argument from index.html text box
            # •	https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
        # 	Call TrendFinder.search
        # 	Refresh page
            # •	https://stackoverflow.com/questions/45666664/how-to-refresh-the-flask-web-page