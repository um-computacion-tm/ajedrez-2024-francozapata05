from main.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "White"
    
    def move(self, from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)

        if piece is None:
            return "PiezaNoExiste"

        color_piece = piece.get_color()
        destination = self.__board__.get_piece(to_row, to_col)


        if color_piece != self.__turn__:
            return "ColorIncorrecto"

        if destination is not None and destination.get_color() == self.__turn__:
            return "CasillaOcupada" 

        if from_row == to_row and from_col == to_col:
            return "MismaCasilla"
            
        
        else:
            
            validar = self.__board__.validate_move(self.__board__.get_positions(), from_row, from_col, to_row, to_col)
            if validar == "MovimientoInvalido":
                return "MovimientoInvalido"
            
            self.__board__.set_positions(from_row, from_col, to_row, to_col)
            self.change_turn()

    
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"

    def get_board(self):
        return self.__board__


