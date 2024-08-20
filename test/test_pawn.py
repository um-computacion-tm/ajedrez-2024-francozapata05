import unittest
from main.pawn import Pawn

class TestPawn(unittest.TestCase):

    def test_init(self):
        pawn = Pawn("White")
        self.assertEqual(pawn.get_color(), "White")

    def test_color(self):
        pawn = Pawn("White")
        self.assertEqual(pawn.get_color(), "White")
    
    def test_name(self):
        pawn = Pawn("White")
        self.assertEqual(pawn.__name__, "Pawn")

    def test_str(self):
        pawn_white = Pawn("White")
        self.assertEqual(str(pawn_white), "♟")
        pawn_black = Pawn("Black")
        self.assertEqual(str(pawn_black), "♙")