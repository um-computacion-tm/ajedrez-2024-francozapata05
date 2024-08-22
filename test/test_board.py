import unittest
from main.board import Board
from main.chess import Chess

class TestBoard(unittest.TestCase):

    def test_board_creation(self):
        chess = Chess()
        board = chess.get_board()
        #Inicializamos el tablero
        self.assertIsNotNone(board)

    def test_get_positions(self):
        chess = Chess()
        board = chess.__board__
        positions = board.get_positions()
        self.assertIsNotNone(positions)

    def test_set_positions(self):
        chess = Chess()
        board = chess.get_board()
        positions = chess.get_board().get_positions()
        #Cambiar posicion de una pieza
        board.set_positions(1, 0, 3, 0)
        self.assertIsNone(positions[1][0])
        self.assertIsNotNone(positions[3][0])

    def test_get_piece(self):
        chess = Chess()
        positions= chess.get_board().get_positions()
        #Obtener pieza en casilla (1, 0)
        self.assertIsNotNone(positions[1][0])

    def test_get_piece_not_exist(self):
        chess = Chess()
        positions= chess.get_board().get_positions()
        #Obtener pieza donde no hay(4, 0)
        self.assertIsNone(positions[4][1])


    def test_validate_move(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        #Validar movimiento de una pieza
        self.assertEqual(board.validate_move(positions, 0, 0, 3, 0), "MovimientoInvalido")
        self.assertEqual(board.validate_move(positions, 1, 0, 2, 0), "Valido")