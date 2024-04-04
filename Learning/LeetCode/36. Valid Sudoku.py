def isValidSudoku(board):

    valid_digits = [1,2,3,4,5,6,7,8,9]


    for row_idx in range(len(board)):
        # print(row)

        row_lst = []

        for digit in board[row_idx]:
            if digit not in row_lst and digit != '.':
                row_lst.append(digit)
            elif digit in row_lst and digit != '.':
                print("False")
                return False

        col = []
        for column_idx in range(len(board)):
            col.append(board[column_idx][row_idx])

        col_lst = []
        for digit in col:
            print(digit)
            if digit not in col_lst and digit != '.':
                col_lst.append(digit)
            elif digit in col_lst and digit != '.':
                print("False")
                return False





board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]


isValidSudoku(board)