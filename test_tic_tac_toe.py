__author__ = 'Marcin Pieczyński'


import unittest
import sys
from tic_tac_toe import tic_tac_toe_state_checker
from tic_tac_toe import one_pattern
from tic_tac_toe import win_patterns_generator


class Tic_Tac_Toe_State_Checker_Test(unittest.TestCase):
    """Tests for tic_tac_toe_state_checker from Tic_tac_toe.py.
    Checks weather:
    - stdin works correctly
    - board is NxN
    - who won X, O, both X and O or none
    """

    def test_tic_tac_toe_1(self):
        """ stdin test     TO DO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
        pass

    def test_tic_tac_toe_2(self):
        """Test - none won board."""
        board_1 = [
            "XO.",
            ".OX",
            ".X."
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_1), ".")

    def test_tic_tac_toe_3(self):
        """Test - X won board.
        Board contains extra empty line at beginning and end."""
        board_2 = [
            "",
            "X...",
            ".X..",
            "..X.",
            "...X",
            ""
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_2), "X")

    def test_tic_tac_toe_4(self):
        """Test - none won board."""
        board_3 = [
            "X...",
            ".X..",
            "..X.",
            "....",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_3), ".")

    def test_tic_tac_toe_5(self):
        """Test - O won board."""
        board_4 = [
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_4), "O")

    def test_tic_tac_toe_6(self):
        """Test - board is not NxN, return exit code 1."""

        board_5 = [
            "XXOO.",
            "...X.",
            "OOOO",
            "...",
            "....."
            ]
        with self.assertRaises(SystemExit) as cm:
            tic_tac_toe_state_checker(board=board_5)
        self.assertEqual(cm.exception.code, 1)

    def test_tic_tac_toe_7(self):
        """Test - X and O both won board."""
        board_6 = [
            "X..O",
            "X..O",
            "X..O",
            "X..O",
            ]
        self.assertEqual(tic_tac_toe_state_checker(board=board_6), "X")


class One_Pattern_Test(unittest.TestCase):
    """Tests for one_pattern from Tic_tac_toe.py.
    Checks weather:
    - function return correct value.
    """

    def test_one_pattern_1(self):
        """ Test - checks if win patterns are correctly read from board."""
        board = [
            "XO.",
            ".OX",
            ".X."
            ]
        row_1 = [[0, 0], [0, 1], [0, 2]]
        row_2 = [[0, 0], [1, 0], [2, 0]]
        row_3 = [[0, 0], [1, 1], [2, 2]]

        self.assertEqual(one_pattern(board, row_1), "XO.")
        self.assertEqual(one_pattern(board, row_2), "X..")
        self.assertEqual(one_pattern(board, row_3), "XO.")


class Win_Patterns_Generator_Test(unittest.TestCase):
    """Tests for win_patterns_generator from Tic_tac_toe.py.
    Checks weather:
    - generator return all and correct win patterns from board.
    """

    def test_win_patterns_generator_1(self):
        """Test - checks if function return all proper win patterns. """
        boar_len = 3
        correct_win_patterns = [
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],

            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],

            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
        for row in win_patterns_generator(boar_len):
            self.assertIn(row, correct_win_patterns)



















if __name__ == '__main__':
    unittest.main()