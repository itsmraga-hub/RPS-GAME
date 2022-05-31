# import random
from random import random


def play_game():
    """The main game function that is called to run the game."""
    choices = ["R", "P", "S"]
    # randomly choose a variable between 0, 1 and 2 and store it in a variable a.
    a = int(random() * len(choices))
    # find the value from our choices list to use as CPU's choice.
    choice = choices[a]
    inp = input("Input R or P and S: ").strip().upper()

    # Call input_validator to validate the choice entered if its "R" or "P" or "S".
    input_validator(inp, choice)


def win_checker(comp, player):
    """Function to check the winner"""
    if comp == player:
        print("Tie")
    elif comp == "R" and player == "S":
        print("Computer wins!!")
    elif comp == "P" and player == "R":
        print("Computer wins!!")
    elif comp == "S" and player == "P":
        print("Computer wins!!")
    elif player == "R" and comp == "S":
        print("You win!!")
    elif player == "P" and comp == "R":
        print("You win!!")
    elif player == "S" and comp == "P":
        print("You win!!")


def chooser(inp, choice):
    """This chooser function takes two validated variables inp and choice and checks
        their corresponding values in the dictionary printing them out and then calls
        the win_checker function to get the winner
    """
    gameDict = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }
    print(f'Player ({gameDict[inp]}) : CPU ({gameDict[choice]})')
    win_checker(choice, inp)


def input_validator(inp, choice):
    """
        This function validates the user input, if user input is valid, the chooser() function
        is called and the game continues and exits. If not valid, the play_game() function is called again to allow for user input again.
    """
    if inp == 'R' or inp == "P" or inp == "S":
        chooser(inp, choice)
    else:
        print("Wrong choice: Try Again!!!")
        play_game()


# Call the function play_game() which takes no variables to start the game.
play_game()
