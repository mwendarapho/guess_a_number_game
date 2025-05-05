
import unittest
from unittest.mock import patch
import io
import time
import random

import builtins
import number_guessing_game as game

class TestNumberGuessingGame(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "abc", "11", "3"])
    @patch('random.randint', side_effect=[5, 1, 3, 3])
    @patch('time.time')
    def test_game_behavior(self, mock_time, mock_randint, mock_input):
        start = 1000000

        # Create a generator to simulate time progression safely
        def time_generator():
            times = [start, start+1, start+2, start+3]
            for t in times:
                yield t
            while True:
                yield start + 11  # to break the loop (simulate time's up)

        mock_time.side_effect = time_generator()

        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            game.number_guessing_game()
            output = fake_out.getvalue()

            self.assertIn("Correct!", output)
            self.assertIn("Invalid input", output)
            self.assertIn("Please enter a number between 1 and 10.", output)
            self.assertIn("Your score:", output)

    @patch('time.time')
    def test_time_runs_out(self, mock_time):
        mock_time.side_effect = [1000, 1011]  # start and end

        with patch('builtins.input', return_value="5"):
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                game.number_guessing_game()
                output = fake_out.getvalue()
                self.assertIn("Time's up!", output)

if __name__ == '__main__':
    unittest.main()

