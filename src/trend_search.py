# Main class (TrendSearch)
    # init
        # Connect to google API
            # https://github.com/GeneralMills/pytrends#connect-to-google
        # Connect to Mongo db
    # search
        # Param: text query
        # API data in dictionary format
        # Store in new mongo collection, named by query all lower case with underscores no spaces
    # visualize
        # Param: collection name
        # Query mongo and create data frame from output
        # Create matplotlib line graph, pretty up title remove underscores and proper capitalization
        # Return image, matplotlib visual
    # list_collections
        # Param: none
        # Get list of collection names from mongo
        # Return list
