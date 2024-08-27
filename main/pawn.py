from main.piece import Piece


class Pawn(Piece):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.__initial_position__ = True
        self.__white_str__ = '♙'
        self.__black_str__ = '♟'

    def get_initial_position(self):
        return self.__initial_position__
    
    def set_initial_position(self, value):
        self.__initial_position__ = value

