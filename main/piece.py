class Piece:
    def __init__(self, name, color):
        self.__color__ = color
        self.__name__ = name
        self.__white_str__ = ""
        self.__black_str__ = ""

    def get_color(self):
        return self.__color__
    
    def get_name(self):
        return self.__name__
    
    def __str__(self):
        return self.__white_str__ if self.__color__ == 'White' else self.__black_str__