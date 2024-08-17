from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
    
    def move(self, from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)
        
        board = self.__board__.get_positions()

        if board[to_row][to_col] is None:        
            board[to_row][to_col] =  board[from_row][from_col]
            board[from_row][from_col] = None
        
        else:
            return "error"

        self.change_turn()

    
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__.get_positions()
        


