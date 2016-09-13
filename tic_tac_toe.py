__author__ = 'Marcin Pieczyński'


import sys


def win_patterns_generator(board_len):
    """Generator of winning position pattern"""

    win_patterns = [
        [[i, i] for i in range(board_len)],
        [[i, board_len - 1 - i] for i in range(board_len)]
    ]
    for i in range(board_len):
        win_patterns.append([[i, j] for j in range(board_len)])
        win_patterns.append([[j, i] for j in range(board_len)])

    for one_win_pattern in win_patterns:
        yield one_win_pattern


def one_pattern(board, row):
    """Return one pattern from board"""
    return "".join([board[x][y] for (x, y) in row])


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
        # board = input("Submit a board:\n")
        board = sys.stdin.readlines()

    board = [elem.strip() for elem in board if elem]
    board_len = len(board)

    # assessing if board is NxN
    for row in board:
        if len(row) != board_len:
            return sys.exit(1)

    win_requirement = [
        'X' * board_len,
        'O' * board_len,
    ]

    # reading the board according to win_patterns using generator and set comprehension
    win_state = {one_pattern(board, row)[0] for row in win_patterns_generator(board_len)
                   if one_pattern(board, row) in win_requirement}

    # assessing who won X or O
    if "X" in win_state or "X" in win_state and "O" in win_state:
        return "X"
    elif "O" in win_state:
        return "O"
    return '.'


if __name__ == '__main__':
    print(tic_tac_toe_state_checker())
