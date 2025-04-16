import random
import time

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("You have 10 seconds to guess numbers between 1-10.")
    
    score = 0
    end_time = time.time() + 10
    
    while time.time() < end_time:
        secret_number = random.randint(1, 10)
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
        secret_number = random.randint(1,10)
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

    print(f"\nTime's up! Your score: {score}")

if __name__ == "__main__":
    number_guessing_game()