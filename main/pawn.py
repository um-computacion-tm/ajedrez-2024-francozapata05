from main.piece import Piece


class Pawn(Piece):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.__initial_position__ = True

    def get_initial_position(self):
        return self.__initial_position__
    
    def set_initial_position(self, value):
        self.__initial_position__ = value

    def __str__(self):
        return '♙' if self.__color__ == 'White' else '♟'
