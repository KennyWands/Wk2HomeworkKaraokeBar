import unittest

from src.bar import Bar
from src.room import Room
from src.album import Album
from test_data import room_list, guest_list


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar("Code Clan Karaoke", room_list, 100)
        self.guest = guest_list[0]
        self.guest1 = guest_list[1]
        self.guest2 = guest_list[2]
        self.guest4 = guest_list[4]

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
        self.assertEqual(95, self.guest.cash)
        # add to room
        self.assertEqual("Slash", self.bar.rooms[0].guests_in_room[0].name)

    def test__book_in_guest_FAIL_cash(self):
        # get room
        self.assertEqual("Spice Girls", self.bar.assign_room(self.guest2))
        # check cash
        self.assertEqual(
            True, self.bar.check_guest_cash(self.guest2, self.bar.rooms[3])
        )
        # check cap
        self.assertEqual(True, self.bar.check_room_cap(self.bar.rooms[3]))
        # take cash
        self.assertEqual(9, self.guest2.cash)
        # add to room
        self.assertEqual("Axl", self.bar.rooms[3].guests_in_room[0].name)

    def test__book_in_guest_FAIL_song(self):
        self.assertEqual(
            "You have horrible taste in music, get out.",
            self.bar.assign_room(
                self.guest4,
            ),
        )


# def test__book_in_guest_FAIL_cap(self):
#    self.bar.assign_room(self.guest1)
