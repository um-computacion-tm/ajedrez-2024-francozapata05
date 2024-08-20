import unittest
from main.bishop import Bishop
from main.chess import Chess

class TestBishop(unittest.TestCase):

    def test_init(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.get_color(), "White")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.get_color(), "Black")


    def test_color(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.get_color(), "White")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.get_color(), "Black")

    
    def test_name(self):
        bishop_white = Bishop("White")
        self.assertEqual(bishop_white.__name__, "Bishop")
        bishop_black = Bishop("Black")
        self.assertEqual(bishop_black.__name__, "Bishop")


    def test_str(self):
        bishop_white = Bishop("White")
        self.assertEqual(str(bishop_white), "♝")
        bishop_black = Bishop("Black")
        self.assertEqual(str(bishop_black), "♗")

    #En condiciones iniciales, ningun alfil se puede mover, por los peones
    def test_validate_movement_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        white_bishop = positions[0][2]
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,1,1), "MovimientoInvalido")
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,1,2), "MovimientoInvalido")
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,1,3), "MovimientoInvalido")
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,2,0), "MovimientoInvalido")
        black_bishop = positions[7][2]
        self.assertEqual(black_bishop.validate_movement(positions, 7,2,2,7), "MovimientoInvalido")

    def test_validate_movement_correct(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        #Quitamos los peones que impidan el movimiento de los alfiles
        positions[1][1] = None
        positions[6][5] = None
        white_bishop = positions[0][2]
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,2,0), "Valido")
        self.assertEqual(white_bishop.validate_movement(positions, 0,2,1,1), "Valido")
        chess.change_turn()
        black_bishop = positions[6][1]
        self.assertEqual(black_bishop.validate_movement(positions, 7,2,5,0), "Valido")
        self.assertEqual(black_bishop.validate_movement(positions, 7,2,6,1), "Valido")

    def test_validate_movement_everywhere(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[3][3] = Bishop("White")
        self.assertEqual(positions[3][3].validate_movement(positions, 3,3,2,2), "Valido")
        self.assertEqual(positions[3][3].validate_movement(positions, 3,3,2,4), "Valido")
        self.assertEqual(positions[3][3].validate_movement(positions, 3,3,4,2), "Valido")
        self.assertEqual(positions[3][3].validate_movement(positions, 3,3,4,4), "Valido")
        self.assertEqual(positions[3][3].validate_movement(positions, 3,3,5,5), "Valido")

    def test_validate_movement_wrong(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()