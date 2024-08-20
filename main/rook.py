from main.piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__name__ = "Rook"

    def __str__(self):
        return '♜' if self.__color__ == 'White' else '♖'
    
    def get_color(self):
        return super().get_color()
    
    def get_name(self):
        return self.__name__

    def validate_movement(self, positions, from_row, from_col, to_row, to_col):

        if from_row == to_row or from_col == to_col:
            
            #Movimiento horizontal
            if from_row == to_row:
                # Determinar el incremento
                step = 1 if to_col > from_col else -1

                for i in range(from_col + step, to_col + step, step):

                    if positions[from_row][i] is None:
                        if i == to_col:
                            return "Valido"
                        continue
                    
                    if positions[from_row][i] is not None:
                        if i == to_col and positions[from_row][i].get_color() != self.__color__:
                             return "Valido"
                        return "MovimientoInvalido"
            

            #Movimiento vertical
            elif from_col == to_col:
                # Determinar el incremento
                step = 1 if to_row > from_row else -1

                for i in range(from_row + step, to_row + step, step):

                    if positions[i][from_col] is None:
                        if i == to_row:
                            return "Valido"
                        continue
                    
                    if positions[i][from_col] is not None:
                        if i == to_row and positions[i][from_col].get_color() != self.__color__:
                             return "Valido"
                        return "MovimientoInvalido"
            
        return "MovimientoInvalido"
