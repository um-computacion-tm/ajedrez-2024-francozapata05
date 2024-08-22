from main.piece import Piece 

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Bishop"
        self.__diagonal__ = True
        self.__perpendicular__ = False
        self.__salta__ = False
        self.__alcance__ = None #None == ilimitado

    def __str__(self):
        return '♗' if self.__color__ == 'White' else '♝'

