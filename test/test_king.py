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

    def test_validate_movement_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        white_king = positions[0][4]
        self.assertEqual(white_king.validate_movement(board, 0, 4, 0, 3), "MovimientoInvalido")
        self.assertEqual(white_king.validate_movement(board, 0, 4, 1, 3), "MovimientoInvalido")
        self.assertEqual(white_king.validate_movement(board, 0, 4, 1, 4), "MovimientoInvalido")
        self.assertEqual(white_king.validate_movement(board, 0, 4, 1, 5), "MovimientoInvalido")
        self.assertEqual(white_king.validate_movement(board, 0, 4, 0, 5), "MovimientoInvalido")

    def test_validate_movement_general(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[4][4] = King("White")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 3, 3), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 3, 4), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 3, 5), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 4, 5), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 5, 5), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 5, 4), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 5, 3), "Valido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 4, 3), "Valido")
        # Salteando una casilla de por medio
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 2, 3), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 2, 4), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 2, 5), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 4, 6), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 6, 5), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 6, 4), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 6, 3), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(board, 4, 4, 4, 2), "MovimientoInvalido")
