import random
choices = ["rock", "paper", "scissors"]
choices_length = len(choices)

computer_choice = random.randint(0, choices_length - 1)
print("Welcome to Rock, Paper, Scissors!")
human_choice = int(input("Please make your choice! Type 0 for rock, 1 for paper, and 2 for scissors\n"))

if human_choice == 0:
    print("rock")
elif human_choice == 1:
    print("paper")
elif human_choice == 2:
    print("scissors")
else:
    print("Invalid choice")


if computer_choice == 0:
    print("rock")
elif computer_choice == 1:
    print("paper")
elif computer_choice == 2:
    print("scissors")

if human_choice == computer_choice:
    print("draw")
if human_choice != computer_choice:
    if human_choice == 0 and computer_choice == 1:
        print("You lose")
    elif human_choice == 0 and computer_choice == 2:
        print("You win")
    elif human_choice == 1 and computer_choice == 0:
        print("You win")
    elif human_choice == 1 and computer_choice == 2:
        print("You lose")
    elif human_choice == 2 and computer_choice == 0:
        print("You lose")
    elif human_choice == 2 and computer_choice == 1:
        print("You win")
