import random

choices = ["rock", "paper", "scissors"]

# 1. Get the FIRST input from the user before the loop starts
# This variable will be checked by the 'while' condition on the first iteration
user_choice = input("Enter your choice (rock, paper, scissors) or 'stop' to end the game: ")

# 2. The main game loop will continue as long as the user doesn't enter "stop"
while user_choice.lower() != "stop":
    
    # 3. Handle invalid input FIRST, before any game logic
    if user_choice.lower() not in choices: 
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
    else:
        # 4. If the input is valid, the game logic runs
        computer_choice = random.choice(choices)
        print("Your Choice:", user_choice.lower())
        print("Computer Choice:", computer_choice)

        # 5. Determine the winner using a clear if/elif/else structure
        if user_choice.lower() == computer_choice:
            print("It's a tie!")
        elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
             (user_choice.lower() == "scissors" and computer_choice == "paper") or \
             (user_choice.lower() == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("Computer wins!")

    # 6. Get the NEXT input from the user at the end of the loop
    # This input will be checked by the 'while' condition in the next iteration
    user_choice = input("\nPlay again? Enter your choice or 'stop' to end the game: ")

# 7. A final message after the loop has exited gracefully
print("Thanks for playing!")