from main.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Rook"

    def __str__(self):
        return '♖' if self.__color__ == 'White' else '♜'

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):
        return super().movimiento_perpendicular(positions, from_row, from_col, to_row, to_col)
