import random
import time
import unittest

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You have 10 seconds to guess numbers between 1-10.")

def get_secret_number():
    return random.randit(1, 10)

def check_guess(guess, secret_number):
    if guess < 1 or guess > 10:
        return "invalid"
    elif guess == secret_number:
        return "correct"
    else:"invalid"

    score = 0
    end_time = time.time() + 10
    
    while time.time() < end_time:
        secret_number = random.randint(1, 10)
        try:
            number_to_guess = random.randint(1,10)   


            # TODO: Get players guess(handle non number input)
            elapsed_time = int(end_time - time.time())
            remaining_time = int(end_time - elapsed_time)
            guess = int(input("enter your guess: "))
            if guess == secret_number:
                True
                print(f"Correct. Time left: {elapsed_time}seconds")
                score += 1
                guess = int(3)
            else:
                print(f"Invalid. Time left: {elapsed_time}seconds")  


                # TODO: Check if guess is correct and update score
            if guess < 1 or guess > 10:
                print("please enter a number between 1 and 10")
                secret_number = get_secret_number()
            if guess == secret_number:
                print("correct")
                score += 1
  
            else:
                print(f"wrong, the number is {secret_number}.")    

                  
                # TODO: Display remaining time 
                elapsed_time = time.time() - end_time
           
            if  remaining_time <= 0:
                print("time is over")
                print(f"your total score is: {score}")
        except ValueError:
            print("Invalid input,enter a number between 1 and 10")
            
    print(f"\nTime's up! Your score: {score}")


class TestNumberGuessingGame(unittest.TestCase):
    
    def test_check_guess_correct(self):
        self.assertEqual(check_guess(4, 4), "correct")
    
    def test_check_guess_incorrect(self):
        self.assertEqual(check_guess(3, 4), "incorrect")
    
    def test_check_guess_out_of_range_low(self):
        self.assertEqual(check_guess(0, 4), "out_of_range")
    
    def test_check_guess_out_of_range_high(self):
        self.assertEqual(check_guess(11, 4), "out_of_range")
    
    def test_get_secret_number_range(self):
        for _ in range(100):
            num = get_secret_number()
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 10)

if __name__ == "__main__":
    mode = input("Type 'play' to start the game or 'test' to run tests: ").strip().lower()
    if mode == "play":
        number_guessing_game()
    elif mode == "test":
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        print("Invalid input. Please type 'play' or 'test'.")    