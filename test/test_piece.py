import unittest
from main.piece import Piece

class TestPiece(unittest.TestCase):

    def test_color(self):
        piece = Piece("White")
        self.assertEqual(piece.get_color(), "White")

    def test_name(self):
        piece = Piece("White")
        self.assertEqual(piece.get_name(), "")
    
    def test_diagonal(self):
        piece = Piece("White")
        self.assertEqual(piece.get_diagonal(), False)

    def test_perpendicular(self):
        piece = Piece("White")
        self.assertEqual(piece.get_perpendicular(), False)

    def test_salta(self):
        piece = Piece("White")
        self.assertEqual(piece.get_salta(), False)

    def test_alcance(self):
        piece = Piece("White")
        self.assertEqual(piece.get_alcance(), None)
