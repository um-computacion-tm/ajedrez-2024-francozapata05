from .piece import Piece 

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Bishop"
        self.__diagonal__ = True
        self.__perpendicular__ = False

    def __str__(self):
        return '♗' if self.__color__ == 'White' else '♝'


    def validate_movement(self, positions, from_row, from_col, to_row, to_col):
        return super().movimiento_diagonal(positions, from_row, from_col, to_row, to_col)
    
        