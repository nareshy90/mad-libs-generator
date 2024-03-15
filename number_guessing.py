import random

secret_number = random.randint(1,100)

guesses_left = 7

while guesses_left > 0:
    # Get user's guess
    guess = int(input("Guess a number between 1 and 100: "))
    guesses_left -= 1  # Decrement guesses remaining

    # Check the guess
    if guess == secret_number:
        break  # Exit the loop if guess is correct
    elif guess < secret_number:
        print("Too low! Tye again")
    else:
        print("Too high! Try again")

# Handle win or loose scenario
if guess == secret_number:
    print("you guessed it! the number was", secret_number)
else:
    print("You ran out of guessed. The number was", secret_number)
