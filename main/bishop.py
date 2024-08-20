from main.piece import Piece 


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Bishop"

    def __str__(self):
        return '♝' if self.__color__ == 'White' else '♗'


    def get_color(self):
        return self.__color__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        #Calculamos la distancia en diagonal entre las casillas
        mov_fila = abs(to_row) - abs(from_row)
        mov_columna = abs(to_col) - abs(from_col) 

        #Detectamos aritmeticamente si el movimiento es diagonal
        if  abs(mov_fila) == abs(mov_columna):

            inc_fila = int(mov_fila / abs(mov_fila))
            inc_columna = int(mov_columna / abs(mov_columna))

            #Analizamos si alguna casilla que atraviese esta ocupada
            for casilla in range(1, abs(mov_fila) + 1, abs(inc_fila)):

                if inc_fila > 0 and inc_columna > 0:
                    if positions[from_row + casilla][from_col + casilla] != None:
                        return "MovimientoInvalido"

                elif inc_fila > 0 and inc_columna < 0:
                    if positions[from_row + casilla][from_col - casilla] != None:
                        return "MovimientoInvalido"

                elif inc_fila < 0 and inc_columna > 0:
                    if positions[from_row - casilla][from_col + casilla] != None:
                        return "MovimientoInvalido"

                elif inc_fila < 0 and inc_columna < 0:
                    if positions[from_row - casilla][from_col - casilla] != None:
                        return "MovimientoInvalido"

            return "Valido"

        return "MovimientoInvalido"
        