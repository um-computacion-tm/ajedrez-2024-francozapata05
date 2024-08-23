from main.piece import Piece

class Rook(Piece):
    def __init__(self, name,color):
        super().__init__(name, color)

    def __str__(self):
        return '♖' if self.__color__ == 'White' else '♜'
