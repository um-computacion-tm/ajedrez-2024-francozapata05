from main.piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Queen"

    def __str__(self):
        return '♕' if self.__color__ == 'White' else '♛'


    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        mov_vertical = to_row - from_row
        mov_horizontal = to_col - from_col

        if mov_vertical == 0  or mov_horizontal == 0:
            return super().movimiento_perpendicular(positions, from_row, from_col, to_row, to_col)

        if mov_vertical != 0  and mov_horizontal != 0:
            return super().movimiento_diagonal(positions, from_row, from_col, to_row, to_col)
        