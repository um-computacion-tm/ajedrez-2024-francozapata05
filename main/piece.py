class Piece:
    def __init__(self, name, color):
        self.__color__ = color
        self.__name__ = name

    def get_color(self):
        return self.__color__
    
    def get_name(self):
        return self.__name__
    