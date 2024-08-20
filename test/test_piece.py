import unittest
from main.piece import Piece

class TestPiece(unittest.TestCase):
    def test_color(self):
        piece = Piece("White")
        self.assertEqual(piece.get_color(), "White")


