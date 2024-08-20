import unittest
from main.knight import Knight
from main.chess import Chess  

class TestKnight(unittest.TestCase):

    def test_init(self):
        knight = Knight("White")
        self.assertEqual(knight.__color__, "White")

    def test_color(self):
        knight = Knight("White")
        self.assertEqual(knight.get_color(), "White")
    
    def test_name(self):
        knight = Knight("White")
        self.assertEqual(knight.__name__, "Knight")

    def test_str(self):
        knight_black = Knight("Black")
        knight_white = Knight("White")
        self.assertEqual(str(knight_white), "♞")
        self.assertEqual(str(knight_black), "♘")

    # Movimientos del caballo en posicion incial
    def test_validate_movement_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(positions[0][1].validate_movement(positions, 0,1,2,0), "Valido")
        self.assertEqual(positions[0][1].validate_movement(positions, 0,1,2,2), "Valido")
        self.assertEqual(positions[0][1].validate_movement(positions, 0,1,1,3), "MovimientoInvalido")

    def test_validate_movement_general(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        #Inserto un caballo en el medio del tablero para evaluar sus movimientos
        positions[4][4] = Knight("White")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,3,6), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,3,2), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,2,5), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,2,3), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,5,6), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,5,2), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,6,5), "Valido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,6,3), "Valido")

        #Movimientos Invalidos: Movimiento en linea recta
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,4,7), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,7,4), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,1,4), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,7,4), "MovimientoInvalido")
        self.assertEqual(positions[4][4].validate_movement(positions, 4,4,4,0), "MovimientoInvalido")

