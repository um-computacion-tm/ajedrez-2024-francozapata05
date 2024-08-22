from main.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Queen"
        self.__diagonal__ = True
        self.__perpendicular__ = True
        self.__salta__ = False
        self.__alcance__ = None

    def __str__(self):
        return '♕' if self.__color__ == 'White' else '♛'

