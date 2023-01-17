import random

# Generate a random number between 0 and 20
number = random.randint(0, 20)

while True:
    # Ask the user for their guess
    guess = int(input("Guess a number between 0 and 20: "))

    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess > number:
        print("Sorry, your guess is too high.")
    else:
        print("Sorry, your guess is too low.")
