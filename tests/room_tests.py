import unittest


from src.room import Room
from test_data import room_list  # , album1


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = room_list[0]

    ## variable tests
    def test_room_has_name(self):
        self.assertEqual("Early G'n'R", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(1, self.room.capacity)

    def test_room_has_album(self):
        self.assertEqual("Appetite for Destruction", self.room.album.name)

    def test_has_admission_price(self):
        self.assertEqual(5, self.room.admission)


## Method tests
