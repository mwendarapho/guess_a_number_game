import unittest
from unittest.mock import patch
import builtins
import time
import random

# Assuming the function is in a file named `guess_game.py`
# from guess_game import number_guessing_game

class TestNumberGuessingGame(unittest.TestCase):

    @patch('builtins.input', side_effect=['5', '3', '7', '10', '1', '2', '4', '6', '8', '9'])
    @patch('time.time')
    @patch('random.randint', side_effect=[5, 3, 7, 10, 1, 2, 4, 6, 8, 9])
    def test_number_guessing_game(self, mock_randint, mock_time, mock_input):
        start_time = 1000000
        # simulate time increasing by 1s per guess
        mock_time.side_effect = [start_time + i for i in range(11)]

        with patch('builtins.print') as mock_print:
            number_guessing_game()

        # Check if the final score is printed
        self.assertTrue(any("Your score" in str(call) for call in mock_print.call_args_list))


if __name__ == '__main__':
    unittest.main()
