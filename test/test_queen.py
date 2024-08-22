import unittest
from main.queen import Queen
from main.chess import Chess    

class TestQueen(unittest.TestCase):

    def test_init(self):
        queen_white = Queen("White")
        self.assertEqual(queen_white.get_color(), "White")
        queen_black = Queen("Black")
        self.assertEqual(queen_black.get_color(), "Black")

    def test_color(self):
        queen_white = Queen("White")
        self.assertEqual(queen_white.get_color(), "White")
        queen_black = Queen("Black") 
        self.assertEqual(queen_black.get_color(), "Black")
    
    def test_name(self):
        queen = Queen("White")
        self.assertEqual(queen.get_name(), "Queen")


    def test_str(self):
        queen_white = Queen("White")
        self.assertEqual(str(queen_white), "♕")
        queen_black = Queen("Black")
        self.assertEqual(str(queen_black), "♛")

    def test_validate_movement(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[4][4] = Queen("White")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 4, 2), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 3, 2), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 2, 2), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 2, 3), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 2, 5), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 2, 6), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 3, 6), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4, 4, 4, 6), "Valido")
        #Comer Piezas
