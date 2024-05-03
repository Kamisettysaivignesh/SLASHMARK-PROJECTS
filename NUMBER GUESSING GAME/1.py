import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts+1} attempts!")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts! The correct number was {secret_number}.")

# Run the game
guessing_game()
