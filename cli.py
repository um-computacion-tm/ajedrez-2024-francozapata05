from chess import Chess

def main():
    chess = Chess()
    try:
        from_row = int(input('From row: '))
        from_col = int(input('From col: '))
        to_row = int(input('To row: '))
        to_col = int(input('To col: '))
        
        chess.move(from_row, from_col, to_row, to_col)

    #aca atrapamos TODOS los errores
    except Exception as e:
        print("Error")
    
    print(chess.board)


if __name__ == '__main__':
    main()