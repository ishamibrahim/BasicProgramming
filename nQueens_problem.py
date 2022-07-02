import pdb

positive_diagonals = set()
negative_diagonals = set()
column_index = set()
final_boards = []

"""
N Queens problem is a backtracking problem.
The problem is to list all possibilities of placing queens safely in a NxN chessboard
"""
def is_queen_safe(row, col):
    safe = True
    if (row-col) in negative_diagonals or (row+col) in positive_diagonals or col in column_index:
        safe = False
    return safe


def backtrack_queens(row, size, chessboard):
    if row == size:
        final_boards.append([i[:] for i in chessboard])
        return

    else:
        for col in range(size):
            if not is_queen_safe(row, col):
                continue
            negative_diagonals.add(row-col)
            positive_diagonals.add(row+col)
            column_index.add(col)
            chessboard[row][col] = "Q"
            backtrack_queens(row+1, size, chessboard)
            negative_diagonals.remove(row - col)
            positive_diagonals.remove(row + col)
            column_index.remove(col)
            chessboard[row][col] = "."


def create_nqueens(size):
    chessboard = [["."]* size for i in range(size)]
    backtrack_queens(0, size, chessboard)

create_nqueens(4)

final_seq = ""
for solution in final_boards:
    for row in solution:
        final_seq += " ".join(row)
        final_seq += "\n"
    final_seq += "\n"

print(final_seq)
print(len(final_boards))
        

        
    
    

