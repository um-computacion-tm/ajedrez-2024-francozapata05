from main.piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Knight"
        self.__diagonal__ = False
        self.__perpendicular__ = False
        self.__salta__ = True
        self.__alcance__ = None

    def __str__(self):
        return '♘' if self.__color__ == 'White' else '♞'

