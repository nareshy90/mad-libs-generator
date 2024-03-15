import random

secret_number = random.randint(1,20)

guesses_left = 7

while guesses_left > 0:
    guess = int(input("Guess number between 1 and 20: "))
    guesses_left -= 1
    if guess == secret_number:
        break
    elif guess < secret_number:
        print("It's too low! Try again")
    else:
        print("It's too high! Try again")

if guess == secret_number:
    print("You guessed it!")
else:
    print("You ran out of guesses. The number was", secret_number)