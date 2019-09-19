CHESSBOARD = [  [0,1,0,0],
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0]
            ]



def is_queen_safe(row, col, chessboard):
    for i in range(len(chess_board)):
        if chessboard[row][i] or chessboard[i][col]:
            return False
    
    i = row
    j = col
    while (i>=0 and j>=0):
        if chessboard[i][j]:
            return False
        i -= 1
        j -= 1
    
    i = row
    j = col
    while (i<=0 and j > len(chessboard)):
        if chessboard[i][j]:
            return False
        i -= 1
        j += 1
    return True



print (is_queen_safe(3, 3, CHESSBOARD))

def create_chessboard(size):
    return [[0 for j in range(size)] for i in range(size)]

def create_nqueens(size):
    safe_list = []
    chessboard = create_chessboard(size)
    chess_len = len(chessboard)

        

        
    
    

