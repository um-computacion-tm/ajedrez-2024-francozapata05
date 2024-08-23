from main.piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Pawn"
        self.__initial_position__ = True

    def __str__(self):
        return '♙' if self.__color__ == 'White' else '♟'
