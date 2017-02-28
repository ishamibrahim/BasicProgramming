CHESSBOARD = [  [0,1,0,0],
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0]
            ]



def is_queen_safe(row, col):
    for i in range(len(CHESSBOARD)):
        if CHESSBOARD[row][i] or CHESSBOARD[i][col]:
            return False
    
    i = row
    j = col
    while (i>=0 and j>=0):
        if CHESSBOARD[i][j]:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while (i<=0 and j > len(CHESSBOARD)):
        if CHESSBOARD[i][j]:
            return False
        i -= 1
        j += 1
    return True



print is_queen_safe(3, 3)
