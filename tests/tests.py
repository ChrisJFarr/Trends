import unittest
from unittest import TestCase
from src.trend_search import TrendSearch


class TestTrendSearch(TestCase):

    trend_search = None

    def setUp(self):
        # Create instance of TrendSearch
        self.trend_search = TrendSearch()
        return

    def test_setup(self):
        # assert collections for taylor swift, elton john, royals, and chiefs exist
        pass

    def test_search(self):
        # assert query passed is new collection in mongo with lower case and underscores
        pass

    def test_visualize(self):
        # assert image is returned
        pass

    def test_list_collections(self):
        # assert list is returned and that each collection exists in mongo
        pass


if __name__ == "__main__":
    unittest.main()
