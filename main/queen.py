from main.piece import Piece

class Queen(Piece):
    def __init__(self, name,color):
        super().__init__(name, color)
        self.__white_str__ = '♕'
        self.__black_str__ = '♛'

