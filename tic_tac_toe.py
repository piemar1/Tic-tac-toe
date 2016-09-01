__author__ = 'Marcin Pieczyński'


import sys


def tic_tac_toe_state_checker(board=None):
    """
    Function for assessing state of Tic-Tac-Toe game.
    Accepts board as example below:
    board = [
        "XO.",
        ".0X",
        ".X."
    ]
    """

    # Form for input a board
    if not board:
        board = sys.stdin.readlines()
        board = [elem.strip() for elem in board]

    board_len = len(board)

    # assessing if board is NxN
    for row in board:
        if len(row) != board_len:
            return sys.exit(1)

    # Creating winning position pattern
    win_pattern = []
    win_pattern.append([[i, i] for i in range(board_len)])
    win_pattern.append([[i, board_len - 1 - i] for i in range(board_len)])

    for i in range(board_len):
        win_pattern.append([(i, j) for j in range(board_len)])
        win_pattern.append([(j, i) for j in range(board_len)])

    # reading the board according to win_pattern
    current_state = ["".join([board[x][y] for (x, y) in row]) for row in win_pattern]

    # assessing who won X or O
    if 'X'*board_len in current_state and 'O'*board_len in current_state:
        return 'X'

    elif 'X'*board_len in current_state:
        return 'X'

    elif 'O'*board_len in current_state:
        return 'O'

    return '.'


if __name__ == '__main__':
    print(tic_tac_toe_state_checker())
