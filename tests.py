import unittest
import asyncore

from client.basic_client import BasicClient
from config import *


class TestImageServer(unittest.TestCase):
    number_of_sync_connections = 10

    def test_single_connection(self):
        k = BasicClient(HOST, PORT, '/', log=False)
        asyncore.loop()
        self.assertIsNotNone(k.tag_parser.url)
        del k

    def test_synchronous_connections(self):
        x = [BasicClient(HOST, PORT, '/', log=False)
             for _ in range(self.number_of_sync_connections)]
        asyncore.loop()
        urls = [_.tag_parser.url for _ in x]

        self.assertIsNotNone(urls[0])

        for url in urls[1:]:
            self.assertEqual(url, urls[0])

        for _ in x: del _

    def test_synchronous_data_fetch(self):
        x = [BasicClient(HOST, PORT, '/?get+image=get+image', log=False)
             for _ in range(self.number_of_sync_connections)]
        asyncore.loop()
        urls = [_.tag_parser.url for _ in x]

        self.assertIsNotNone(urls[1])

        for url in urls[2:]:
            self.assertEqual(url, urls[1])

        for _ in x: del _


if __name__ == "__main__":
    unittest.main()
