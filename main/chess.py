from main.board import Board
from main.movimientos import ReglasDeMovimientos

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
        self.__ganador__ = None
        self.__reglas__ = ReglasDeMovimientos()
    
    # Move recibe los datos de la posicion de origen y destino
    # Es el que permitira o denegara el movimiento
    def move(self, from_row, from_col, to_row, to_col):

        # Si salta alguna excepcion, se retorna el mensaje
        mensaje = ""

        origin_piece = self.__board__.get_piece(from_row, from_col)
        destination = self.__board__.get_piece(to_row, to_col)
        
        # Si la pieza origen no existe, se retorna el mensaje
        if origin_piece is None:
            mensaje = "PiezaNoExiste"

        # Si la pieza a mover no es del color del turno actual, se retorna el mensaje
        elif origin_piece.get_color() != self.__turn__:
            mensaje = "ColorIncorrecto"
        
        # Si la casilla de origen es la misma que la destino, se retorna el mensaje
        elif from_row == to_row and from_col == to_col:
            mensaje = "MismaCasilla"

        # Si la casilla destino esta ocupada por una de las piezas del mismo color, se retorna el mensaje
        elif destination is not None and destination.get_color() == self.__turn__:
            mensaje = "CasillaOcupada" 
            
        # Si no salto ninguna excepcion, mensaje estara vacio, y se retorna el movimiento
        if mensaje != "":
            return(mensaje)
        
        # Habilitar movimiento devolvera Valido o MovimientoInvalido
        return(self.habilitar_movimiento(destination, from_row, from_col, to_row, to_col))
            
    # Esta funcion habilita o no el movimiento
    def habilitar_movimiento(self, destination, from_row, from_col, to_row, to_col):
            
        # Validamos que el movimiento sea válido
        validar = self.analizar_movimiento(self.__board__.get_positions(), from_row, from_col, to_row, to_col)
        if validar == "MovimientoInvalido":
            return "MovimientoInvalido"

        # Si la pieza destino es el rey contratio, retornamos ReyEliminado, para finalizar el juego
        if destination != None and destination.get_name() == "King" and destination.get_color() != self.__turn__:
            self.__ganador__ = self.__turn__
            return "ReyEliminado"
        
        # Si a este punto, esta todo OK. Se mueve la pieza.
        self.__board__.set_positions(from_row, from_col, to_row, to_col)
        self.change_turn()    
        return "Valido"

    def get_reglas(self):
        return self.__reglas__

    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"

    def get_board(self):
        return self.__board__
    
    def get_turn(self):
        return self.__turn__

    def get_ganador(self):
        return self.__ganador__

    # Determinamos si el movimiento cumple con las reglas de la pieza a mover
    def analizar_movimiento(self, positions, from_row, from_col, to_row, to_col):
        nombre_pieza = positions[from_row][from_col].get_name()
        reglas = self.__reglas__

        # Movimiento Rook
        if nombre_pieza == "Rook":
            validacion = reglas.movimiento_perpendicular(positions, from_row, from_col, to_row, to_col)

        # Movimiento knight
        elif nombre_pieza == "Knight":
            validacion = reglas.movimiento_knight(positions, from_row, from_col, to_row, to_col)

        # Movimiento Bishop
        elif nombre_pieza == "Bishop":
            validacion = reglas.movimiento_diagonal(positions, from_row, from_col, to_row, to_col)

        # Movimiento Queen
        elif nombre_pieza == "Queen":
            validacion = reglas.movimiento_queen(positions, from_row, from_col, to_row, to_col)
        
        # Movimiento King
        elif nombre_pieza == "King":
            validacion = reglas.movimiento_king(positions, from_row, from_col, to_row, to_col)
        
        # Movimiento Pawn
        elif nombre_pieza == "Pawn":
            validacion = reglas.movimiento_pawn(positions, from_row, from_col, to_row, to_col)
        
        return validacion