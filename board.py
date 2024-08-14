from piece import Rook, Knight, Bishop, King, Queen, Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for fila in range(8):
            col = []
            for columna in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("WHITE")
        self.__positions__[0][1] = Knight("WHITE")
        self.__positions__[0][2] = Bishop("WHITE")
        self.__positions__[0][3] = Queen("WHITE")
        self.__positions__[0][4] = King("WHITE")
        self.__positions__[0][5] = Bishop("WHITE")
        self.__positions__[0][6] = Knight("WHITE")
        self.__positions__[0][7] = Rook("WHITE")

        self.__positions__[1][0] = Pawn("WHITE")
        self.__positions__[1][1] = Pawn("WHITE")
        self.__positions__[1][2] = Pawn("WHITE")
        self.__positions__[1][3] = Pawn("WHITE")
        self.__positions__[1][4] = Pawn("WHITE")
        self.__positions__[1][5] = Pawn("WHITE")
        self.__positions__[1][6] = Pawn("WHITE")
        self.__positions__[1][7] = Pawn("WHITE")

        self.__positions__[6][0] = Pawn("BLACK")
        self.__positions__[6][1] = Pawn("BLACK")
        self.__positions__[6][2] = Pawn("BLACK")
        self.__positions__[6][3] = Pawn("BLACK")
        self.__positions__[6][4] = Pawn("BLACK")
        self.__positions__[6][5] = Pawn("BLACK")
        self.__positions__[6][6] = Pawn("BLACK")
        self.__positions__[6][7] = Pawn("BLACK")

        self.__positions__[7][0] = Rook("BLACK")
        self.__positions__[7][1] = Knight("BLACK")
        self.__positions__[7][2] = Bishop("BLACK")
        self.__positions__[7][3] = King("BLACK")
        self.__positions__[7][4] = Queen("BLACK")
        self.__positions__[7][5] = Bishop("BLACK")
        self.__positions__[7][6] = Knight("BLACK")
        self.__positions__[7][7] = Rook("BLACK")

    def get_piece(self, row, col):
        return self.__positions__[row][col]


""" Probando acceso a matriz
a = Board()

for lista in a.__positions__:
    print(lista)
    print()

print(a.__positions__[3][3]) """