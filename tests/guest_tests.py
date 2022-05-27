import unittest


from src.guest import Guest
from test_data import guest_list


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = guest_list[0]

    ##Variable tests
    def test_guest_has_name(self):
        self.assertEqual("Slash", self.guest.name)

    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)

    def test_guest_has_favourite(self):
        self.assertEqual("Paradise City", self.guest.song)
