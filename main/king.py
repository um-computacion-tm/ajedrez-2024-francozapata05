from main.piece import Piece


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "King"

    
    def __str__(self):
        return '♔' if self.__color__ == 'White' else '♚'
