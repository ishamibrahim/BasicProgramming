import pdb

"""
    This is to list all possible words from a matrix that can occur by moving all eight ways from word to word
    in the matrix
    
    we check if a word exists in a matrix.. like a crossword puzzle except here the words need not be in a straight line
"""
# Below lists detail all eight possible movements from a cell
# (top, right, bottom, left, and four diagonal moves)
row_movements = [-1, -1, -1, 0, 1, 0, 1, 1]
col_movements = [-1, 1, 0, -1, -1, 1, 0, 1]

final_words = []


def print_marked_locations(marked_locations):
    final_seq = ""
    for r in marked_locations:
        final_seq += " ".join(["1" if i else "0" for i in r])
        final_seq += "\n"
    final_seq += "\n"
    print(final_seq)


def is_word_in_list(word, word_list):
    return any(list_item.startswith(word) for list_item in word_list)


# A recursive function to generate all possible words in a boggle
def search_path_on_board(marked_locations, board, words, i, j, path=''):
    path += board[i][j]
    if is_word_in_list(path, words):
        marked_locations[i][j] = True
        if path in words:
            print_marked_locations(marked_locations)
            final_words.append(path)
        for k in range(len(row_movements)):
            new_r = i + row_movements[k]
            new_c = j + col_movements[k]

            if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and not marked_locations[new_r][new_c]:
                    search_path_on_board(marked_locations, board, words, new_r, new_c, path)

    marked_locations[i][j] = False


def search_words_in_board(words, board):
    marked_locations = [[False] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            search_path_on_board(marked_locations, board, words, i, j)


if __name__ == '__main__':
    board = [
        ['M', 'S', 'E'],
        ['R', 'A', 'T'],
        ['L', 'O', 'N']
    ]

    words = ['STAR', 'NOTE', 'SAND', 'STONE', 'STORM', 'MATE', 'STEW', 'MANY']

    search_words_in_board(words, board)
    print(final_words)
