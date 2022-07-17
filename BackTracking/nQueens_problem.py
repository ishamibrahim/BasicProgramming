import pdb

"""
N Queens problem is a backtracking problem.
The problem is to list all possibilities of placing queens safely in a NxN chessboard
"""


class NQueens:
    positive_diagonals = set()
    negative_diagonals = set()
    column_indices = set()
    final_boards = []


    @staticmethod
    def print_final_board():
        final_seq = ""
        for solution in NQueens.final_boards:
            for row in solution:
                final_seq += " ".join(row)
                final_seq += "\n"
            final_seq += "\n"
        print(final_seq)


def is_queen_safe(row, col):
    safe = True
    if (row-col) in NQueens.negative_diagonals or (row+col) in NQueens.positive_diagonals or col in NQueens.column_indices:
        safe = False
    return safe


def backtrack_queens( row, size, chessboard):
    if row == size:
        NQueens.final_boards.append([i[:] for i in chessboard])
        return

    else:
        for col in range(size):
            if not is_queen_safe(row, col):
                continue
            NQueens.negative_diagonals.add(row-col)
            NQueens.positive_diagonals.add(row+col)
            NQueens.column_indices.add(col)
            chessboard[row][col] = " Q"
            backtrack_queens(row+1, size, chessboard)
            NQueens.negative_diagonals.remove(row - col)
            NQueens.positive_diagonals.remove(row + col)
            NQueens.column_indices.remove(col)
            chessboard[row][col] = " ."


def create_nqueens(size):
    chessboard = [["."]* size for i in range(size)]
    backtrack_queens(0, size, chessboard)


def main():
    create_nqueens(8)
    NQueens.print_final_board()

        
if __name__ == "__main__":
    main()
        
    
    

