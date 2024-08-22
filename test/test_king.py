import unittest
from main.king import King
from main.chess import Chess

class TestKing(unittest.TestCase):
    def test_init(self):
        king = King("White")
        self.assertEqual(king.__color__, "White")
    
    def test_name(self):
        king = King("White")
        self.assertEqual(king.__name__, "King")

    def test_color(self):
        king = King("White")
        self.assertEqual(king.get_color(), "White")

    def test_str(self):
        king_black = King("Black")
        king_white = King("White")
        self.assertEqual(str(king_white), "♔")
        self.assertEqual(str(king_black), "♚")
