
import random
import time
import threading

guess = None  # Shared variable to capture input

def get_input():
    global guess
    try:
        guess = input("Your guess: ")
    except:
        pass

def number_guessing_game():
    global guess
    print("Welcome to the Number Guessing Game!")
    print("You have 10 seconds to guess numbers between 1-10.")

    score = 0
    end_time = time.time() + 10

    while time.time() < end_time:
        secret_number = random.randint(1, 10)
        guess = None

        remaining_time = int(end_time - time.time())
        print(f"\nGuess the number (1-10). Time left: {remaining_time} seconds")

        input_thread = threading.Thread(target=get_input)
        input_thread.start()

        input_thread.join(timeout=remaining_time)

        if guess is None:
            print("No input entered in time!")
            break  # End game if no input in remaining time
        else:
            try:
                user_guess = int(guess)
                if user_guess == secret_number:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! The number was {secret_number}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    print(f"\nTime's up! Your score: {score}")

if __name__ == "__main__":
    number_guessing_game()
