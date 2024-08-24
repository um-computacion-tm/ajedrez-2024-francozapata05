from math import sqrt

class ReglasDeMovimientos:

    def __init__(self) -> None:
        pass
    
    def calcular_distancia(self, from_row, from_col, to_row, to_col):
        #Calculamos la distancia entre las casillas
        mov_fila = abs(to_row) - abs(from_row)
        mov_columna = abs(to_col) - abs(from_col) 
        return [mov_fila, mov_columna]

    def movimiento_diagonal(chess, positions, from_row, from_col, to_row, to_col):
        reglas = ReglasDeMovimientos()
        #Calculamos la distancia entre las casilla
        distancias = reglas.calcular_distancia(from_row, from_col, to_row, to_col)
        #Detectamos aritmeticamente si el movimiento es diagonal
        if  abs(distancias[0]) == abs(distancias[1]):

            #Analizamos si alguna casilla que atraviese esta ocupada
            inputs = [from_row, from_col, to_row, to_col]
            return chess.analizar_camino(positions, distancias, inputs)

        return "MovimientoInvalido"


    def calcular_incremento(self, valor):
        incremento = int(valor / abs(valor))
        return incremento

    def analizar_camino(self, positions, distancias, inputs):
        origen = positions[inputs[0]][inputs[1]]
        inc_fila = self.calcular_incremento(distancias[0])
        inc_columna = self.calcular_incremento(distancias[1])
        
        #Analizamos si alguna casilla que atraviese esta ocupada
        mensaje = "Valido"
        for casilla in range(1, abs(distancias[0]) + 1, abs(inc_fila)):

            # Si se ha llegado al final de la casilla, se detiene el bucle
            if casilla == abs(distancias[0]) and positions[inputs[2]][inputs[3]] != None:
                if positions[inputs[2]][inputs[3]].get_color() != origen.__color__:
                    mensaje = "Valido"
                    break

            # Movimiento abajo-a-la-derecha
            if inc_fila > 0 and inc_columna > 0:
                if positions[inputs[0] + casilla][inputs[1] + casilla] != None:
                    mensaje = "MovimientoInvalido"
                    break

            # Movimiento abajo-a-la-izquierda
            elif inc_fila > 0 and inc_columna < 0:
                if positions[inputs[0] + casilla][inputs[1] - casilla] != None:
                    mensaje = "MovimientoInvalido"
                    break

            # Movimiento arriba-a-la-dereecha
            elif inc_fila < 0 and inc_columna > 0:
                if positions[inputs[0] - casilla][inputs[1] + casilla] != None:
                    mensaje = "MovimientoInvalido"
                    break

            # Movimiento arriba-a-la-izquierda
            elif inc_fila < 0 and inc_columna < 0:
                if positions[inputs[0] - casilla][inputs[1] - casilla] != None:
                    mensaje = "MovimientoInvalido"
                    break
        return mensaje
    
    def movimiento_horizontal(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]
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
                
    def movimiento_vertical(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]
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

    def movimiento_perpendicular(chess, positions, from_row, from_col, to_row, to_col):
        reglas = ReglasDeMovimientos()
        if from_row == to_row or from_col == to_col:
            
            #Movimiento horizontal
            if from_row == to_row:
                return reglas.movimiento_horizontal(positions, from_row, from_col, to_row, to_col)
                
            #Movimiento vertical
            elif from_col == to_col:
                return reglas.movimiento_vertical(positions, from_row, from_col, to_row, to_col)
            
        return "MovimientoInvalido"
    
    def movimiento_pawn(chess, positions, from_row, from_col, to_row, to_col):
        
        pieza_inicial = positions[from_row][from_col]
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col
        destination = positions[to_row][to_col]

        direccion = 1 if pieza_inicial.get_color() == "White" else -1

        #Analizamos si es su primer movimiento para permitir que se mueva dos espacios
        if pieza_inicial.__initial_position__ == True:
            if mov_fila == (2*direccion) and mov_columna == 0 and destination == None:
                pieza_inicial.__initial_position__ = False
                return "Valido"

        #Movimiento vertical
        if mov_fila == direccion:
            
            #Movimiento diagonal
            if mov_columna != 0 and destination != None:

                if sqrt(mov_fila**2 + mov_columna**2) == sqrt(2): 
                    
                    if destination.get_color() != pieza_inicial.get_color():
                        pieza_inicial.__initial_position__ = False
                        return "Valido"

            if mov_columna == 0 and destination == None:
                pieza_inicial.__initial_position__ = False
                return "Valido"
                
        return "MovimientoInvalido"
    
    def movimiento_knight(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]

        # Validar casilla destino
        if positions[to_row][to_col] != None and positions[to_row][to_col].get_color() == self.__color__:
            return "MovimientoInvalido"

        mov_abs = abs(to_row - from_row) + abs(to_col - from_col)
        if mov_abs == 3:
            if abs(to_row - from_row) > 2 or abs(to_col - from_col) > 2:
                return "MovimientoInvalido"
            return "Valido"

        return "MovimientoInvalido"
    
    def movimiento_king(chess, positions, from_row, from_col, to_row, to_col):
        self = positions[from_row][from_col]


        # validar casilla destino
        destination = positions[to_row][to_col]
        if destination != None and destination.get_color() == self.__color__:
            return "MovimientoInvalido"
        
        mov_fila = to_row - from_row
        mov_columna = to_col - from_col
        
        #Detectamos aritmeticamente si se mueve a una casilla contigua
        if sqrt(mov_fila**2 + mov_columna**2) == 1 or sqrt(mov_fila**2 + mov_columna**2) == sqrt(2):
            return "Valido"
    

        return "MovimientoInvalido"
    
    def movimiento_queen(chess, positions, from_row, from_col, to_row, to_col):

        mov_vertical = to_row - from_row
        mov_horizontal = to_col - from_col

        # El movimiento de la reina es basicamente el de la torre junto al del alfil
        # Detectamos si el movimiento es diagonal o perpendicular, y llamamos al metodo correspondiente
        if mov_vertical == 0  or mov_horizontal == 0:
            return chess.movimiento_perpendicular(positions, from_row, from_col, to_row, to_col)

        if mov_vertical != 0  and mov_horizontal != 0:
            return chess.movimiento_diagonal(positions, from_row, from_col, to_row, to_col)
        

