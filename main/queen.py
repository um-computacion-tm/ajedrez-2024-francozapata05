from main.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Queen"

    def __str__(self):
        return '♛' if self.__color__ == 'White' else '♕'
    
    def get_color(self):
        return self.__color__

    def get_name(self):
        return self.__name__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        mov_vertical = to_row - from_row
        mov_horizontal = to_col - from_col

        if mov_vertical == 0  or mov_horizontal == 0:
            return self.movimiento_vertical(positions,from_row, from_col, to_row, to_col)

        if mov_vertical != 0  and mov_horizontal != 0:
            return self.movimiento_diagonal(positions, from_row, from_col, to_row, to_col)
        
    

    
    def movimiento_vertical(self, positions, from_row, from_col, to_row, to_col):

        if from_row == to_row:
            # Determinar el incremento
            step = 1 if to_col > from_col else -1

            for i in range(from_col + step, to_col + step, step):
                if positions[from_row][i] is None:
                    if i == to_col:
                        return "Valido"
                    continue
                
                if positions[from_row][i] is not None:
                    if i == to_col and positions[from_row][i].get_color() != self.__color__:
                        return "Valido"
                    return "MovimientoInvalido"
                
    def movimiento_diagonal(self, positions, from_row, from_col, to_row, to_col):

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