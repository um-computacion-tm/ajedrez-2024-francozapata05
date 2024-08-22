import unittest
from main.knight import Knight
from main.chess import Chess  

class TestKnight(unittest.TestCase):

    def test_init(self):
        knight = Knight("White")
        self.assertEqual(knight.__color__, "White")

    def test_color(self):
        knight = Knight("White")
        self.assertEqual(knight.get_color(), "White")
    
    def test_name(self):
        knight = Knight("White")
        self.assertEqual(knight.__name__, "Knight")

    def test_str(self):
        knight_black = Knight("Black")
        knight_white = Knight("White")
        self.assertEqual(str(knight_white), "♘")
        self.assertEqual(str(knight_black), "♞")


