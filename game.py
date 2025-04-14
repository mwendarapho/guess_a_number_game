import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You have 10 seconds to guess numbers between 1-10.")
    
    score = 0
    end_time = time.time() + 10
    
    while time.time() < end_time:
        secret_number = random.randint(1, 10)
        
        # TODO: Get player's guess (handle non-number inputs)
        guess = None
        
        # TODO: Check if guess is correct and update score
        
        # TODO: Display remaining time
        
    print(f"\nTime's up! Your score: {score}")

if __name__ == "__main__":
    number_guessing_game()