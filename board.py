from bishop import Bishop
from knight import Knight
from rook import Rook
from king import King
from queen import Queen
from pawn import Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("White")
        self.__positions__[0][1] = Knight("White")
        self.__positions__[0][2] = Bishop("White")
        self.__positions__[0][3] = Queen("White")
        self.__positions__[0][4] = King("White")
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
        self.__positions__[to_row][to_col] = self.__positions__[from_row][from_col]
        self.__positions__[from_row][from_col] = None

    def get_piece(self, row, col):
        if self.__positions__[row][col] is None:
            return None
        
        return self.__positions__[row][col]
