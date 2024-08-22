import unittest
from main.queen import Queen
from main.chess import Chess    

class TestQueen(unittest.TestCase):

    def test_init(self):
        queen_white = Queen("White")
        self.assertEqual(queen_white.get_color(), "White")
        queen_black = Queen("Black")
        self.assertEqual(queen_black.get_color(), "Black")

    def test_color(self):
        queen_white = Queen("White")
        self.assertEqual(queen_white.get_color(), "White")
        queen_black = Queen("Black") 
        self.assertEqual(queen_black.get_color(), "Black")
    
    def test_name(self):
        queen = Queen("White")
        self.assertEqual(queen.get_name(), "Queen")


    def test_str(self):
        queen_white = Queen("White")
        self.assertEqual(str(queen_white), "♕")
        queen_black = Queen("Black")
        self.assertEqual(str(queen_black), "♛")
