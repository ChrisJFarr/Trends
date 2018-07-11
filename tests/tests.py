import unittest
from unittest import TestCase
from src.trend_search import TrendSearch
from io import BytesIO


class TestTrendSearch(TestCase):

    trend_search = TrendSearch(None)

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
        self.assertIsInstance(self.trend_search.visualize(self.trend_search.list_collections()[0]),
                              BytesIO,
                              "Unexpected type returned, expected BytesIO")

    def test_list_collections(self):
        # assert list is returned and that each collection exists in mongo
        self.assertIsInstance(self.trend_search.list_collections(), list,
                              "Unexpected type returned, expected list")


if __name__ == "__main__":
    unittest.main()
