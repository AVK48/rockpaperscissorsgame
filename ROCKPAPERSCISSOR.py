import random

choices = ["rock", "paper", "scissors"]


user_choice = input("Enter your choice (rock, paper, scissors) or 'stop' to end the game: ")

while user_choice.lower() != "stop":
    
    if user_choice.lower() not in choices: 
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    else:
        computer_choice = random.choice(choices)
        print("Your Choice:", user_choice.lower())
        print("Computer Choice:", computer_choice)

        if user_choice.lower() == computer_choice:
            print("It's a tie!")
        elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
             (user_choice.lower() == "scissors" and computer_choice == "paper") or \
             (user_choice.lower() == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("Computer wins!")

   
    user_choice = input("\nPlay again? Enter your choice or 'stop' to end the game: ")


print("Thanks for playing!")
