import random

# List of choices
choices = ["rock", "paper", "scissors"]

# Get user's choice
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Check for invalid input
if user_choice not in choices:
  print("Invalid choice. Please try again.")
  exit()

# Get computer's random choice
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
  print("Tie! You both chose", user_choice)
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
  print("You win! You chose", user_choice, "and computer chose", computer_choice)
else:
  print("You lose! You chose", user_choice, "and computer chose", computer_choice)
 