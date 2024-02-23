import random


def guess(x):
    number_guess = (1, x)
    guess = 0
    while guess != number_guess:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < number_guess:
            print("Try again. too low")
        elif guess > number_guess:
            print("Try again. too high")

print(f"Congratulations! You guessed the number {guess}")
guess()