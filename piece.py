class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__name__ = ""
        self.__diagonal__ = False
        self.__perpendicular__ = False
        self.__salta__ = False
        self.__alcance__ = None #None == ilimitado

    def get_color(self):
        return self.__color__
    
    def get_name(self):
        return self.__name__

    def get_diagonal(self):
        return self.__diagonal__
    
    def get_perpendicular(self):
        return self.__perpendicular__
    
    def get_salta(self):
        return self.__salta__

    def get_alcance(self):
        return self.__alcance__
    