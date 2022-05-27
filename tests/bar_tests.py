import unittest

from src.bar import Bar
from src.room import Room
from src.album import Album
from test_data import room_list


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Code Clan Karaoke", room_list, 100)

    ##Variable tests
    def test_bar_has_name(self):
        self.assertEqual("Code Clan Karaoke", self.bar.name)

    def test_bar_has_rooms(self):
        self.assertEqual("Early G'n'R", self.bar.rooms[0].name)

    def test_bar_has_Cash(self):
        self.assertEqual(100, self.bar.till)


##Method tests
