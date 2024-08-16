from piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Knight"

    def __str__(self):
        return '♘' if self.__color__ == 'White' else '♞'

    def mover(self):
        pass
