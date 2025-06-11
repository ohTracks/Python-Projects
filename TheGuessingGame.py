import random

def main():
    print("Welcome to The Guessing Game! \nGuess a Number between 1 and 100!")
    target = random.randint(1, 100)
    guess = int(input("Enter a Number: "))
    tries = guessing_game(target, guess)
    print(f"Correct! The random number was {target}!")
    print(f"You guessed it in {tries} tries.")

def guessing_game(target, guess):
    tries = 1  # First guess counts as a try
    while guess != target:
        if guess > target:
            guess = int(input("Lower Number! Try Again: "))
        else:
            guess = int(input("Higher Number! Try Again: "))
        tries += 1
    return tries

main()
