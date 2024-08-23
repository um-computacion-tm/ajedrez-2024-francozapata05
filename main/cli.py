from main.chess import Chess
from main.exceptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, MovimientoInvalido, IndexErrorPersonalizada
import os


class Cliente:
    # Esta funcion detecta que sistema operativo estamos usando, para poder limpiar la consola
    def clear_console(self):
        # Verifica si es Windows o Linux/macOS
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para Linux/macOS
            os.system('clear')
            os.system('clear')

    def inicializar_juego(self):
        # Inicializacion del juego
        chess = Chess()
        board = chess.get_board()
        positions = board.get_positions()
        return [chess, positions]


    def comenzar_iteracion(self,chess, positions):
        print("Para salir inserte 999 en fila de origen.")
        print("Turno: " + chess.get_turn())
        # Imprimiendo el tablero con números de fila y columna
        print("   " + "   ".join([str(i) for i in range(8)]))

        # Imprimir una línea de separación antes de la primera fila
        print("  " + "----" * 8)  # Línea superior

        for i, fila in enumerate(positions):
            fila_str = ' | '.join([str(piece) if piece else ' ' for piece in fila])
            print(f'{i} | {fila_str} |')  # Imprimir número de fila seguido de la fila
            print("  " + "----" * 8)  # Imprimir línea de separación entre filas

    def buscar_index_error(self, input):
        if not (0 <= input < 8):
            raise IndexErrorPersonalizada

    def input_function(self):
            from_row = int(input('From row: '))

            if from_row == 999:
                return False

            Cliente.buscar_index_error(self,from_row)

            from_col = int(input('From col: '))
            Cliente.buscar_index_error(self,from_col)

            to_row = int(input('To row: '))
            Cliente.buscar_index_error(self,to_row)

            to_col = int(input('To col: '))
            Cliente.buscar_index_error(self,to_col)   

            return [from_row, from_col, to_row, to_col]

        
    def detectar_exepcion(self, movement):
        if movement == "ColorIncorrecto":
                raise ColorIncorrecto

        if movement == "MismaCasilla":
            raise MismaCasilla
            
        if movement == "CasillaOcupada":
            raise CasillaOcupada
            
        if movement == "PiezaNoExiste":
            raise PiezaNoExiste
            
        if movement == "MovimientoInvalido":
            raise MovimientoInvalido



