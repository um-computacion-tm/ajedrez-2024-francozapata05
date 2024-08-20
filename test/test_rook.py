import unittest
from main.rook import Rook
from main.chess import Chess

class TestRook(unittest.TestCase):

    # Tests inciales propios de cada pieza, init, color, name, str

    def test_init(self):
        rook = Rook("White")
        self.assertEqual(rook.get_color(), "White")

    def test_color(self):
        rook = Rook("White")
        self.assertEqual(rook.get_color(), "White")
    
    def test_name(self):
        rook = Rook("White")
        self.assertEqual(rook.__name__, "Rook")
        rook2 = Rook("Black")
        self.assertEqual(rook2.__name__, "Rook")

    def test_str(self):
        rook_white = Rook("White")
        self.assertEqual(str(rook_white), "♜")
        rook_black = Rook("Black")
        self.assertEqual(str(rook_black), "♖")

    # Evaluamos cada posible tipo de movimiento
    def test_validate_movement_initial(self):

        #Ninguna torre se puede mover inicialmente, por los peones
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        rook1 = board.get_piece(0,0) #Torre superior izquierda
        rook2 = board.get_piece(0,7) #Torre superior derecha
        rook3 = board.get_piece(7,0) #Torre inferior izquierda
        rook4 = board.get_piece(7,7) #Torre inferior derecha

        #Movimiento Inicial Vertical
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 1, 0), "MovimientoInvalido")
        self.assertEqual(rook2.validate_movement(positions, 0, 7, 1, 7), "MovimientoInvalido")
        self.assertEqual(rook3.validate_movement(positions, 7, 0, 0, 7), "MovimientoInvalido")
        self.assertEqual(rook4.validate_movement(positions, 7, 7, 0, 0), "MovimientoInvalido")
        #Movimiento Inicial Horizontal
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 0, 1), "MovimientoInvalido")
        self.assertEqual(rook2.validate_movement(positions, 7, 7, 7, 1), "MovimientoInvalido")
        self.assertEqual(rook3.validate_movement(positions, 0, 7, 0, 1), "MovimientoInvalido")
        self.assertEqual(rook4.validate_movement(positions, 7, 0, 7, 1), "MovimientoInvalido")

    def test_validate_movement_white(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        rook1_white = board.get_piece(0,0)
        self.assertEqual(rook1_white.validate_movement(positions, 0, 0, 1, 0), "MovimientoInvalido")
        #Elimino el peon de enfrente a la torre superior izquierda
        positions[1][0] = None
        self.assertEqual(rook1_white.validate_movement(positions, 0, 0, 2, 0), "Valido")
        self.assertEqual(rook1_white.validate_movement(positions, 0, 0, 7, 0), "MovimientoInvalido")
        #Muevo la torre para evaluar movimientos horizontales
        chess.move(0,0,2,0)
        self.assertEqual(rook1_white.validate_movement(positions, 2, 0, 2, 7), "Valido")

    def test_validate_movement_black(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        rook1_black = board.get_piece(7,0)
        #Debo cambiar el turno para evaluar a las negras
        chess.change_turn()
        self.assertEqual(rook1_black.validate_movement(positions, 7, 0, 5, 0), "MovimientoInvalido")
        #Elimino el peon de enfrente a la torre inferior izquierda
        positions[6][0] = None
        self.assertEqual(rook1_black.validate_movement(positions, 7, 0, 5, 0), "Valido")
        self.assertEqual(rook1_black.validate_movement(positions, 7, 0, 0, 0), "MovimientoInvalido")
        #Muevo la torre para evaluar movimientos horizontales
        chess.move(7,0,5,0)
        chess.change_turn()
        self.assertEqual(rook1_black.validate_movement(positions, 5, 0, 5, 7), "Valido")


    def test_validate_movement_errores_comunes(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        rook1 = board.get_piece(0,0)
        #Mover pieza a la misma casilla
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 0, 0), "MovimientoInvalido")
        #Mover torre de forma no recta
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 3, 3), "MovimientoInvalido")
        #Mover torre a una casilla ocupada
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 1, 0), "MovimientoInvalido")
        #Saltar a otra pieza/Casilla Ocupada
        self.assertEqual(rook1.validate_movement(positions, 0, 0, 3, 0), "MovimientoInvalido")