import unittest
from main.pawn import Pawn
from main.chess import Chess


class TestPawn(unittest.TestCase):

    def test_init(self):
        pawn = Pawn("White")
        self.assertEqual(pawn.get_color(), "White")

    def test_color(self):
        pawn = Pawn("White")
        self.assertEqual(pawn.get_color(), "White")
    
    def test_name(self):
        pawn_white = Pawn("White")
        pawn_black = Pawn("Black")
        self.assertEqual(pawn_white.get_name(), "Pawn")
        self.assertEqual(pawn_black.get_name(), "Pawn")


    def test_str(self):
        pawn_white = Pawn("White")
        self.assertEqual(str(pawn_white), "♙")
        pawn_black = Pawn("Black")
        self.assertEqual(str(pawn_black), "♟")
