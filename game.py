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
                # the try except is ment to give the ValueError if the user enters something that is not a number
        try:
            # defined remaining time and made an output
            remaining_time = int(end_time - time.time())
            print(f"Guess the number (1-10). Time left: {remaining_time} seconds")
            guess = int(input("Your guess: "))

            # avoids input of numbers less than 1 and those more than 10
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            # if the number guessed same as the randomly generated number then it is correct and score should be added by 1
            elif guess == secret_number:
                print("Correct!")
                score += 1

            # if there is no break in the above the else runs an output of wrong number and gives what the correct number was
            else:
                print(f"Wrong! The number was {secret_number}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        

    print(f"\nTime's up! Your score: {score}")

if __name__ == "__main__":
    number_guessing_game()