from main.piece import Piece
from math import sqrt

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Pawn"

    def __str__(self):
        return '♟' if self.__color__ == 'White' else '♙'

    def get_color(self):
        return self.__color__

    def get_name(self):
        return self.__name__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):
        return "Valido"
