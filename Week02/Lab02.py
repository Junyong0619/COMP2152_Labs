import random
choices=["Rock", "Paper", "Scissors"]

playerChoice = input("Enter a number between 1 to 3 for the following choices:1-Rock, 2-Paper, 3-Scissors:")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Invalid choice! Please select a number between 1 and 3.")
else:
    # Develop the game logic using if/elif/else
    computerChoice = random.randint(1, 3)

    if playerChoice == computerChoice:
        print("It's a tie!")

    elif playerChoice == 1 and computerChoice == 3:
        print("You win! Rock crushes Scissors.")

    elif playerChoice == 2 and computerChoice == 1:
        print("You win! Paper covers Rock.")

    elif playerChoice == 3 and computerChoice == 2:
        print("You win! Scissors cut Paper.")

    else:
        print("Computer wins!")








