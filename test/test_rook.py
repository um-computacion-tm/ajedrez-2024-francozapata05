import unittest
from main.rook import Rook
from main.chess import Chess

class TestRook(unittest.TestCase):

    # Tests inciales propios de cada pieza, init, color, name, str

    def test_init(self):
        rook = Rook("White")
        self.assertEqual(rook.get_color(), "White")

    def test_color(self):
        rook = Rook("White")
        self.assertEqual(rook.get_color(), "White")
    
    def test_name(self):
        rook = Rook("White")
        self.assertEqual(rook.__name__, "Rook")
        rook2 = Rook("Black")
        self.assertEqual(rook2.__name__, "Rook")

    def test_str(self):
        rook_white = Rook("White")
        self.assertEqual(str(rook_white), "♖")
        rook_black = Rook("Black")
        self.assertEqual(str(rook_black), "♜")

