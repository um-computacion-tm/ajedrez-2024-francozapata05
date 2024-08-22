try:
    from .piece import Piece
except ImportError:
    from piece import Piece

from math import sqrt

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "King"

    
    def __str__(self):
        return '♔' if self.__color__ == 'White' else '♚'

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        # validar casilla destino
        destination = positions.__positions__[to_row][to_col]
        if destination != None and destination.get_color() == self.__color__:
            return "MovimientoInvalido"
        
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col
        
        #Detectamos aritmeticamente si se mueve a una casilla contigua
        if sqrt(mov_fila**2 + mov_columna**2) == 1 or sqrt(mov_fila**2 + mov_columna**2) == sqrt(2):
            return "Valido"
    

        return "MovimientoInvalido"