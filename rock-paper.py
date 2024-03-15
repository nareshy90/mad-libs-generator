import random

options = ["rock", "paper", "scissors"]
user_choice = input("Enter your choice (rock, paper, scissors): ")
computer_choice = random.choice(options)

if user_choice == computer_choice:
    print("It's a tie! You both chose", user_choice)

# You win
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
# You lose
else:
    print("You lose! The computer chose", computer_choice)