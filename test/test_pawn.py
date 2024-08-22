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

    def test_validate_movement_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        white_pawn = positions[1][0]
        self.assertEqual(white_pawn.validate_movement(positions, 1,0,2,0), "Valido")
        self.assertEqual(white_pawn.validate_movement(positions, 1,0,2,1), "MovimientoInvalido")
        self.assertEqual(white_pawn.validate_movement(positions, 1,0,2,2), "MovimientoInvalido")
        self.assertEqual(white_pawn.validate_movement(positions, 1,0,1,1), "MovimientoInvalido")

    def test_validate_movement_comer_pieza(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[5][0] = Pawn("White")
        self.assertEqual(positions[5][0].validate_movement(positions, 5,0,6,0), "MovimientoInvalido")
        self.assertEqual(positions[5][0].validate_movement(positions, 5,0,6,1), "Valido")