import unittest
from main.board import Board
from main.chess import Chess


class TestChess(unittest.TestCase):

    def test_start(self):
        self.chess = Chess()

    def test_initial_turn(self):
        self.chess = Chess()
        # Turno inicial debe ser "White"
        self.assertEqual(self.chess.__turn__, "White")

    def test_move_to_empty_space(self):
        self.chess = Chess()
        # Mover pieza de (1, 0) to (2, 0)
        self.chess.move(1, 0, 2, 0)
        positions = self.chess.get_board().get_positions()
        self.assertIsNotNone(positions[2][0])
        self.assertIsNone(positions[1][0])


    def test_move_to_occupied_space(self):
        self.chess = Chess()

        # Probar mover pieza a casilla ocupada
        result = self.chess.move(0, 0, 1, 0)
        self.assertEqual(result, "CasillaOcupada")
        positions = self.chess.get_board().get_positions()
        self.assertIsNotNone(positions[1][0])
        self.assertIsNotNone(positions[0][0])


    def test_turn_change(self):
        self.chess = Chess()
        #Cambios de turno
        self.assertEqual(self.chess.__turn__, "White")
        self.chess.move(1, 0, 2, 0)
        self.assertEqual(self.chess.__turn__, "Black")

    def test_no_piece_to_move(self):
        self.chess = Chess()
        #Mover una pieza de una casilla vacia
        result = self.chess.move(3, 3, 4, 4)
        self.assertEqual(result, "PiezaNoExiste")
        positions = self.chess.get_board().get_positions()
        self.assertIsNone(positions[4][4])
        self.assertIsNone(positions[3][3])

    def test_move_back_to_same_position(self):
        self.chess = Chess()
        # Mover una pieza a su misma posicion
        result = self.chess.move(1, 0, 1, 0)
        positions = self.chess.get_board().get_positions()
        self.assertIsNotNone(positions[1][0])
        self.assertIsNone(positions[2][0])
        self.assertEqual(result, "CasillaOcupada")
        self.assertEqual(self.chess.__turn__, "White")

