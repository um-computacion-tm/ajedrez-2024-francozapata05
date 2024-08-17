from chess import Chess

def main():
    chess = Chess()
    board = chess.get_board()

    while True: 

        # Imprimiendo el tablero con números de fila y columna
        print("   " + "   ".join([str(i) for i in range(8)]))

        # Imprimir una línea de separación antes de la primera fila
        print("  " + "----" * 8)  # Línea superior

        for i, fila in enumerate(board):
            fila_str = ' | '.join([str(piece) if piece else ' ' for piece in fila])
            print(f'{i} | {fila_str} |')  # Imprimir número de fila seguido de la fila
            print("  " + "----" * 8)  # Imprimir línea de separación entre filas

        try:
            from_row = int(input('From row: '))

            if from_row == 123321:
                break

            if not (0 < from_row < 8):
                raise IndexError


            from_col = int(input('From col: '))

            if not 0 < from_col < 8:
                raise IndexError

            to_row = int(input('To row: '))

            if not 0 < to_row < 8:
                raise IndexError

            to_col = int(input('To col: '))

            if not 0 < to_col < 8:
                raise IndexError

            chess.move(from_row, from_col, to_row, to_col)

        #Aca atrapamos TODOS los errores
        except ValueError as e:
            print("El valor introducido no es un entero. Intentelo de nuevo.")
        except IndexError as e:
            print("Numero de fila o columna incorrecto. Intentelo de nuevo.")




if __name__ == '__main__':
    main()