import unittest
from main.chess import Chess
from main.queen import Queen
from main.knight import Knight
from main.bishop import Bishop
from main.pawn import Pawn
from main.king import King


class TestChess(unittest.TestCase):

    def test_initial_turn(self):
        chess = Chess()
        # Turno inicial debe ser "White"
        self.assertEqual(chess.__turn__, "White")

    def test_move_to_empty_space(self):
        chess = Chess()
        # Mover pieza de (1, 0) to (2, 0)
        chess.move(1, 0, 2, 0)
        positions = chess.get_board().get_positions()
        self.assertIsNotNone(positions[2][0])
        self.assertIsNone(positions[1][0])


    def test_move_errors(self):
        chess = Chess()
        # Probar mover pieza a casilla ocupada
        self.assertEqual(chess.move(0, 0, 1, 0), "CasillaOcupada")
        self.assertEqual(chess.move(3, 3, 4, 4), "PiezaNoExiste")


    def test_get_turn(self):
        chess = Chess()
        self.assertEqual(chess.get_turn(), "White")
        chess.move(1, 0, 2, 0)
        self.assertEqual(chess.get_turn(), "Black")

    def test_turn_change(self):
        chess = Chess()
        #Cambios de turno
        self.assertEqual(chess.change_turn(), None)
        chess.move(1, 0, 2, 0)
        self.assertEqual(chess.change_turn(), None)

    def test_wrong_turn(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEquals(chess.move(6, 0, 4, 0), "ColorIncorrecto")


    def test_habilitar_movimiento(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        destination1 = positions[1][0]
        destination2 = positions[3][0]
        # Mover una pieza a su misma posicion
        self.assertEqual(chess.habilitar_movimiento(destination1, 1, 0, 1, 0), "MovimientoInvalido")
        # Movimiento Valido
        self.assertEqual(chess.habilitar_movimiento(destination2, 1, 0, 3, 0), "Valido")
    
    def test_end_game(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[6][3] = Queen("White")
        self.assertEqual(chess.move(6, 3, 7, 3), "ReyEliminado")

    def test_get_ganador(self):
        chess = Chess()
        positions = chess.get_board().get_positions()
        self.assertEqual(chess.get_ganador(), None)
        positions[6][3] = Queen("White")
        chess.move(6, 3, 7, 3)
        self.assertEqual(chess.get_ganador(), "White")
        

# ------------------------- Tests de Movimientos ---------------------------------

class TestChessMovimientos(unittest.TestCase):
#Alfil
    #En condiciones iniciales, ningun alfil se puede mover, por los peones
    def test_movimiento_alfil_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        # White Bishop
        self.assertEqual(chess.analizar_movimiento(positions, 0,2,1,1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0,2,1,2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0,2,1,3), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0,2,2,0), "MovimientoInvalido")
        # Black Bishop
        self.assertEqual(chess.analizar_movimiento(positions, 7,2,6,1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7,2,6,2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7,2,6,3), "MovimientoInvalido")


    def test_movimiento_alfil(self):
        chess = Chess()
        board = chess.get_board()
        new_positions = board.get_positions()
        new_positions[3][3] = Bishop("White")
        self.assertEqual(chess.analizar_movimiento(new_positions, 3,3,2,2), "Valido")
        self.assertEqual(chess.analizar_movimiento(new_positions, 3,3,2,4), "Valido")
        self.assertEqual(chess.analizar_movimiento(new_positions, 3,3,4,2), "Valido")
        self.assertEqual(chess.analizar_movimiento(new_positions, 3,3,4,4), "Valido")
        self.assertEqual(chess.analizar_movimiento(new_positions, 3,3,5,5), "Valido")

#Torre

    # Evaluamos cada posible tipo de movimiento
    def test_movimiento_torre_initial(self):

        #Ninguna torre se puede mover inicialmente, por los peones
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()

        #Movimiento Inicial Vertical
        self.assertEqual(chess.analizar_movimiento(positions, 0, 0, 1, 0), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 7, 1, 7), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7, 0, 0, 7), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7, 7, 0, 0), "MovimientoInvalido")
        #Movimiento Inicial Horizontal
        self.assertEqual(chess.analizar_movimiento(positions, 0, 0, 0, 1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7, 7, 7, 1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 7, 0, 1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 7, 0, 7, 1), "MovimientoInvalido")
    
    def test_movimiento_torre(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(chess.analizar_movimiento(positions, 0, 0, 1, 0), "MovimientoInvalido")
        #Elimino el peon de enfrente a la torre superior izquierda
        positions[1][0] = None
        self.assertEqual(chess.analizar_movimiento(positions, 0, 0, 2, 0), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 0, 7, 0), "MovimientoInvalido")
        #Muevo la torre para evaluar movimientos horizontales
        chess.move(0,0,2,0)
        self.assertEqual(chess.analizar_movimiento(positions, 2, 0, 2, 7), "Valido")

#Caballo
    
    # Movimientos del caballo en posicion incial
    def test_movimiento_caballo_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(chess.analizar_movimiento(positions, 0,1,2,0), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 0,1,2,2), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 0,1,1,3), "MovimientoInvalido")

    def test_movimiento_caballo(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[4][4] = Knight("White")
        #Inserto un caballo en el medio del tablero para evaluar sus movimientos
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,3,6), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,3,2), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,2,5), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,2,3), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,5,6), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,5,2), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,6,5), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,6,3), "Valido")

        #Movimientos Invalidos: Movimiento en linea recta
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,4,7), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,7,4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,1,4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,7,4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4,4,4,0), "MovimientoInvalido")
    

#Rey


    def test_movimiento_king_initial(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(chess.analizar_movimiento(positions, 0, 3, 0, 2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 3, 1, 2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 3, 1, 3), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 3, 1, 4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 0, 3, 0, 5), "MovimientoInvalido")

    def test_movimiento_king(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[4][4] = King("White")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 3, 3), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 3, 4), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 3, 5), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 5), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 5, 5), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 5, 4), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 5, 3), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 3), "Valido")
        # Salteando una casilla de por medio
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 3), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 5), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 6), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 6, 5), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 6, 4), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 6, 3), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 2), "MovimientoInvalido")
        

#Reina

    def test_movimiento_queen(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[4][4] = Queen("White")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 2), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 3, 2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 2), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 3), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 5), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 2, 6), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 3, 6), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 4, 4, 4, 6), "Valido")
        

    def test_comer_piezas(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[6][0] = Queen("White")
        #En diagonal
        self.assertEqual(chess.analizar_movimiento(positions, 6,0,7,1), "Valido")
        #Horizontal
        self.assertEqual(chess.analizar_movimiento(positions, 6,0,6,1), "Valido")
        #Vertical
        self.assertEqual(chess.analizar_movimiento(positions, 6,0,7,0), "Valido")

        

#Peon

    def test_movimiento_peon_initial_1_space(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(chess.analizar_movimiento(positions, 1,0,2,0), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 1,0,2,1), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 1,0,2,2), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 1,0,1,1), "MovimientoInvalido")

    def test_movimiento_peon_initial_2_spaces(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        self.assertEqual(chess.analizar_movimiento(positions, 1,0,3,0), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 1,1,3,1), "Valido")
        chess.change_turn()
        self.assertEqual(chess.analizar_movimiento(positions, 6,0,4,0), "Valido")
        self.assertEqual(chess.analizar_movimiento(positions, 6,1,4,1), "Valido")

    def test_movimiento_peon_comer_pieza(self):
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        positions[5][0] = Pawn("White")
        positions[6][1] = Pawn("Black")
        positions[6][0] = Pawn("Black")
        self.assertEqual(chess.analizar_movimiento(positions, 5,0,6,0), "MovimientoInvalido")
        self.assertEqual(chess.analizar_movimiento(positions, 5,0,6,1), "Valido") 