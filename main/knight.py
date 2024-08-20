try:
    from .piece import Piece
except ImportError:
    from piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Knight"

    def __str__(self):
        return '♞' if self.__color__ == 'White' else '♘'

    def get_color(self):
        return self.__color__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        # validar casilla destino
        if positions[to_row][to_col] != None and positions[to_row][to_col].get_color() == self.__color__:
            return "MovimientoInvalido"

        mov_abs = abs(to_row - from_row) + abs(to_col - from_col)
        if mov_abs == 3:
            if abs(to_row - from_row) > 2 or abs(to_col - from_col) > 2:
                return "MovimientoInvalido"
            return "Valido"

        return "MovimientoInvalido"
