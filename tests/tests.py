import unittest
from unittest import TestCase
from src.trend_search import TrendSearch


class TestTrendSearch(TestCase):

    trend_search = TrendSearch(None)

    def test_setup(self):
        # assert collections for taylor swift, elton john, royals, and chiefs exist
        pass

    def test_search(self):
        db = self.trend_search.db
        query = "Taylor Swift"
        collection_name = query.replace(" ", "_").lower()
        # assert query passed is new collection in mongo with lower case and underscores
        if collection_name in db.list_collection_names():
            db[collection_name].drop()
        self.trend_search.search(query)
        self.assertTrue(collection_name in db.list_collection_names())
        db[collection_name].drop()
        return

    def test_visualize(self):
        # assert image is returned
        pass

    def test_list_collections(self):
        # assert list is returned and that each collection exists in mongo
        pass


if __name__ == "__main__":
    unittest.main()
