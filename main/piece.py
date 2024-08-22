class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        if self == None:
            pass
        return self.__color__
    
    def get_name(self):
        return self.__name__

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

                if casilla == abs(mov_fila) and positions[to_row][to_col] != None:
                    if positions[to_row][to_col].get_color() != self.__color__:
                        return "Valido"

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
    
    def movimiento_perpendicular(self, positions, from_row, from_col, to_row, to_col):

        if from_row == to_row or from_col == to_col:
            
            #Movimiento horizontal
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
            

            #Movimiento vertical
            elif from_col == to_col:
                # Determinar el incremento
                step = 1 if to_row > from_row else -1

                for i in range(from_row + step, to_row + step, step):

                    if positions[i][from_col] is None:
                        if i == to_row:
                            return "Valido"
                        continue
                    
                    if positions[i][from_col] is not None:
                        if i == to_row and positions[i][from_col].get_color() != self.__color__:
                             return "Valido"
                        return "MovimientoInvalido"
            
        return "MovimientoInvalido"