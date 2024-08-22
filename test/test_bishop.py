import unittest
from main.bishop import Bishop
from main.chess import Chess

class TestBishop(unittest.TestCase):

    def test_init(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.get_color(), "White")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.get_color(), "Black")


    def test_color(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.get_color(), "White")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.get_color(), "Black")

    
    def test_name(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.__name__, "Bishop")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.__name__, "Bishop")


    def test_str(self):
        bishop_white = Bishop("White")
        self.assertEqual(str(bishop_white), "♗")
        bishop_black = Bishop("Black")
        self.assertEqual(str(bishop_black), "♝")

