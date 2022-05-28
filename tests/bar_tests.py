import unittest

from src.bar import Bar
from src.room import Room
from src.album import Album
from test_data import room_list, guest_list


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Code Clan Karaoke", room_list, 100)
        self.guest = guest_list[0]

    ##Variable tests
    def test_bar_has_name(self):
        self.assertEqual("Code Clan Karaoke", self.bar.name)

    def test_bar_has_rooms(self):
        self.assertEqual("Early G'n'R", self.bar.rooms[0].name)

    def test_bar_has_Cash(self):
        self.assertEqual(100, self.bar.till)

    ##Method tests
    def test_welcome_customer(self):
        self.assertEqual("finished", self.bar.welcome_msg())

    def test_book_in_guest(self):
        # get room
        self.assertEqual("Early G'n'R", self.bar.assign_room(self.guest))
        # check cash
        self.assertEqual(True, self.bar.check_guest_cash(self.guest, self.bar.rooms[0]))
        # check cap
        self.assertEqual(True, self.bar.check_room_cap(self.bar.rooms[0]))

        # take cash
        self.assertEqual(99, self.guest.cash)
        # add to room
