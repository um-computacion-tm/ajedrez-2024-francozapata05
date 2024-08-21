from main.chess import Chess
from main.exceptions import CasillaOcupada, PiezaNoExiste, MismaCasilla, ColorIncorrecto, MovimientoInvalido



def main():


    chess = Chess()
    board = chess.get_board()
    positions = board.get_positions()


    while True:

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

        try:
            from_row = int(input('From row: '))

            if from_row == 999:
                break 

            if not (0 <= from_row < 8):
                raise IndexError


            from_col = int(input('From col: '))

            if not 0 <= from_col < 8:
                raise IndexError

            to_row = int(input('To row: '))

            if not 0 <= to_row < 8:
                raise IndexError

            to_col = int(input('To col: '))

            if not 0 <= to_col < 8:
                raise IndexError
            
            movement = chess.move(from_row, from_col, to_row, to_col)

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
            

        #Aca atrapamos TODOS los errores
        except ValueError as e:
            print("El valor introducido no es un entero. Intentelo de nuevo.")
        except IndexError as e:
            print("Numero de fila o columna incorrecto. Intentelo de nuevo.")
        except CasillaOcupada as e:
            print(e.message)
        except PiezaNoExiste as e:
            print(e.message)
        except MismaCasilla as e:
            print(e.message)
        except ColorIncorrecto as e:
            print(e.message)
        except MovimientoInvalido as e:
            print(e.message)




if __name__ == '__main__':
    main()

