# import random module for generate random numbers
import random

# generate random number from specific range 1-20.
random_number = random.randint(1,20)

print("Welcome to the Number Guessing Game!")
print("I have selected number from 1 to 50.Can you guess it?")

# Count attempts
attempts = 0
while True:
    user_guess = int(input("Enter the number:"))
    attempts += 1

    # Compare both random and user guessing number
    if user_guess < random_number:
        print("Your guess is too low! Try again")
    elif user_guess > random_number:
        print("Your guess is Too High!.Try again")
    else:
        print(f"Congrtulations! You are guessed number{attempts} attempts")
        break
