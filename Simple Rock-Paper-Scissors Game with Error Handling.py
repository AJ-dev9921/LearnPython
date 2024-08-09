import random  # Import the random module to generate random choices for the computer

# Define choices and their corresponding values
choices = [-1, 0, 1]  # -1: paper, 0: scissor, 1: rock

# Computer randomly selects a choice from the list
computer = random.choice(choices)

# Get user input and convert it to lowercase for consistency
user_input = input("Enter Your Choice (Rock, Paper, or Scissor): ").lower()

# Map user-friendly choices to numerical values
choice_dict = {
    "rock": 1,
    "paper": -1,
    "scissor": 0
}

# Check if the user input is valid
if user_input not in choice_dict:
    print("Invalid Input")  # Inform the user if their input is invalid
    exit()  # Exit the program if input is not valid
else:
    user_choice = choice_dict[user_input]  # Map the user input to its numerical value

# Determine the game result
if user_choice == computer:
    print("Match Draw")  # The game is a draw if both choices are the same
elif (user_choice < 0 and computer > 0) or (user_choice > 0 and computer == 0) or (user_choice == 0 and computer < 0):
    print("You Win!")  # User wins based on the game rules
else:
    print("You Lose")  # User loses if none of the winning conditions are met

# Map numerical values back to user-friendly choice names for output
reverse_dict = {
    1: "Rock",
    -1: "Paper",
    0: "Scissor"
}
computer_choice = reverse_dict[computer]  # Get the computer's choice in user-friendly format

# Print the choices made by both the computer and the user
print(f"Computer chose: {computer_choice}, You chose: {user_input.capitalize()}")
