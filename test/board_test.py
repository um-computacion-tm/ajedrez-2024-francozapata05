import unittest
from board import Board
from chess import Chess

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
        board_object = chess.__board__
        #Cambiar posicion de una pieza
        board_object.set_positions(1, 0, 3, 0)
        self.assertIsNone(board[1][0])
        self.assertIsNotNone(board[3][0])

    def test_get_piece(self):
        chess = Chess()
        board = chess.get_board()
        #Obtener pieza en casilla (1, 0)
        self.assertIsNotNone(board[1][0])

    def test_get_piece_not_exist(self):
        chess = Chess()
        board = chess.get_board()
        #Obtener pieza donde no hay(4, 0)
        self.assertIsNone(board[4][1])

