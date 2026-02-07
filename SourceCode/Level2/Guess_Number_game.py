import random
def guess_number():

    # Random generte number
    secret_number  = random.randint(1,100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter the number (1-100):"))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Correct Guess! you guessed th number: {attempts} attempts")
                break
        except ValueError:
            print("Invalid input.Please enter a number.")
    # Start the game
guess_number()