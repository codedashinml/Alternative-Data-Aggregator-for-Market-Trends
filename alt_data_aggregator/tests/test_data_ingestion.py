import unittest
from data_ingestion.twitter_scraper import TwitterScraper

class TestTwitterScraper(unittest.TestCase):
    def test_fetch_data(self):
        scraper = TwitterScraper(api_key="test_key", api_secret="test_secret")
        data = scraper.fetch_data(query="market trends")
        self.assertIsNotNone(data)

if __name__ == "__main__":
    unittest.main()