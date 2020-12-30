# Rock Paper Scissors

from random import randint

# Create a list of play options
t = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer
computer = t[randint(0, 2)]
computer = computer.lower()

# Set player to false
player = False

while player == False:
    # Set player to true
    player = input("Rock, Paper, Scissors, Quit?")
    player = player.lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose. Computer wins!", computer, "covers", player)
        else:
            print("You win! Computer loses :(", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose. Computer wins!", computer, "cuts", player)
        else:
            print("You win! Computer loses :(", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose. Computer wins!", computer, "smashes", player)
        else:
            print("You win! Computer loses :(", player, "cuts", computer)
    elif player == "quit":
            print("Bye, see you later!!")
    else:
        print("That is not a valid play. Try again with one of the prompted options.")

    if player != "quit":
        player = False
        computer = t[randint(0, 2)]
        computer = computer.lower()
