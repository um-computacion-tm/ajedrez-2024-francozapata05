from piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Queen"

    def __str__(self):
        return '♕' if self.__color__ == 'White' else '♛'

    def mover(self):
       pass