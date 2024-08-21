from main.piece import Piece

from math import sqrt

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Pawn"

    def __str__(self):
        return '♟' if self.__color__ == 'White' else '♙'

    def get_color(self):
        return self.__color__

    def get_name(self):
        return self.__name__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):        
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col

        destination = positions[to_row][to_col]

        direccion = 1 if self.get_color() == "White" else -1

        #Movimiento vertical
        if mov_fila == direccion:
            
            #Movimiento diagonal
            if mov_columna != 0:

                if sqrt(mov_fila**2 + mov_columna**2) == sqrt(2): 
                    
                    if destination == None:
                        return "MovimientoInvalido"
                    
                    if destination.get_color() != self.get_color():
                        return "Valido"
                else:
                    return "MovimientoInvalido"
            if destination != None:
                return "MovimientoInvalido"
            else:
                return "Valido"

        return "MovimientoInvalido"
