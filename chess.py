from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    def move(self, from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)
        destination = self.__board__.get_piece(to_row, to_col)

        board = self.__board__.get_positions()

        if from_row == to_row and from_col == to_col:
            return "MismaCasilla"

        if destination is not None:
            return "CasillaOcupada" 
            
        elif piece is None:
            return "PiezaNoExiste"

        else:
            self.__board__.set_positions(from_row, from_col, to_row, to_col)
            self.change_turn()

    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__.get_positions()
        
