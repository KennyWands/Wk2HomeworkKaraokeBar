import unittest


from src.album import Album
from test_data import album1


class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = album1

    def test_album_has_name(self):
        self.assertEqual("Appetite for Destruction", self.album.name)

    def test_album_has_band(self):
        self.assertEqual("Guns 'n' Roses", self.album.band)

    def test_album_has_track(self):
        self.assertEqual("Mr Brownstone", self.album.track_list[3])
