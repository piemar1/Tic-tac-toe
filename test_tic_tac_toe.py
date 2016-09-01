__author__ = 'Marcin Pieczyński'


import unittest
from tic_tac_toe import tic_tac_toe_state_checker


class Tic_Tac_Toe_State_Checker_Test(unittest.TestCase):
    """Tests for tic_tac_toe_state_checker from Tic_tac_toe.py"""

    def setUp(self):
        """ Examples of board"""

        self.board_1 = [
            "XO.",
            ".0X",
            ".X."
            ]
        self.board_2 = [
            "X...",
            ".X..",
            "..X.",
            "...X",
            ]
        self.board_3 = [
            "X...",
            ".X..",
            "..X.",
            "....",
            ]
        self.board_4 = [
            "..O..",
            "..O..",
            "..O..",
            "..O..",
            "..O..",
        ]
        self.board_5 = [
            "XX00.",
            "...X.",
            "0000",
            "....",
            "....."
            ]

        self.board_6 = [
            "X..O",
            "X..O",
            "X..O",
            "X..O",
        ]

    def test_tic_tac_toe(self):
        """Tests """

        self.assertEqual(tic_tac_toe_state_checker(board=self.board_1), ".")
        self.assertEqual(tic_tac_toe_state_checker(board=self.board_2), "X")
        self.assertEqual(tic_tac_toe_state_checker(board=self.board_3), ".")
        self.assertEqual(tic_tac_toe_state_checker(board=self.board_4), "O")

        with self.assertRaises(SystemExit) as cm:
            tic_tac_toe_state_checker(board=self.board_5)
        self.assertEqual(cm.exception.code, 1)

        self.assertEqual(tic_tac_toe_state_checker(board=self.board_6), "X")

if __name__ == '__main__':
    unittest.main()