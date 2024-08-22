from main.bishop import Bishop
from main.knight import Knight
from main.rook import Rook
from main.king import King
from main.queen import Queen
from main.pawn import Pawn

class Board:
    def __init__(self):
        # Positions, va a ser una matriz de 8 filas y 8 columnas
        # Instanciamos una matriz vacia e insertamos las piezas en sus posiciones iniciales.
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("White")
        self.__positions__[0][1] = Knight("White")
        self.__positions__[0][2] = Bishop("White")
        self.__positions__[0][3] = King("White")
        self.__positions__[0][4] = Queen("White")
        self.__positions__[0][5] = Bishop("White")
        self.__positions__[0][6] = Knight("White")
        self.__positions__[0][7] = Rook("White")

        self.__positions__[1][0] = Pawn("White")
        self.__positions__[1][1] = Pawn("White")
        self.__positions__[1][2] = Pawn("White")
        self.__positions__[1][3] = Pawn("White")
        self.__positions__[1][4] = Pawn("White")
        self.__positions__[1][5] = Pawn("White")
        self.__positions__[1][6] = Pawn("White")
        self.__positions__[1][7] = Pawn("White")

        self.__positions__[6][0] = Pawn("Black")
        self.__positions__[6][1] = Pawn("Black")
        self.__positions__[6][2] = Pawn("Black")
        self.__positions__[6][3] = Pawn("Black")
        self.__positions__[6][4] = Pawn("Black")
        self.__positions__[6][5] = Pawn("Black")
        self.__positions__[6][6] = Pawn("Black")
        self.__positions__[6][7] = Pawn("Black")

        self.__positions__[7][0] = Rook("Black")
        self.__positions__[7][1] = Knight("Black")
        self.__positions__[7][2] = Bishop("Black")
        self.__positions__[7][3] = King("Black")
        self.__positions__[7][4] = Queen("Black")
        self.__positions__[7][5] = Bishop("Black")
        self.__positions__[7][6] = Knight("Black")
        self.__positions__[7][7] = Rook("Black")

    def get_positions(self):
        return self.__positions__
    
    def set_positions(self, from_row, from_col, to_row, to_col):
        # Copiamos la pieza de la casilla origen a la casilla destino
        self.__positions__[to_row][to_col] = self.__positions__[from_row][from_col]
        # Eliminamos la pieza de la casilla origen
        self.__positions__[from_row][from_col] = None

    def get_piece(self, row, col):
        if self.__positions__[row][col] is None:
            return None # Retornamos None si la casilla no tiene pieza
        return self.__positions__[row][col]
