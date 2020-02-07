# Rock-paper-scissors-lizard-Spock program

# helper functions

def name_to_number(name):
    """helper function that converts a string to an integer """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: Invalid Name"



def number_to_name(number):
    """helper function that converts an integer to its corresponding string"""
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Error: Invalid Number"
    
import random
def rpsls(player_choice): 
    """function to simulate rock paper scissors lizard Spock"""

    print ("")
    # prints a blank line to separate consecutive games
    print ("Player chooses " + player_choice)
    # prints out the message for the player's choice
    player_number = name_to_number(player_choice)
    # converts the player's choice to player_number using the function name_to_number()
    comp_number = random.randrange(0,5)
    # computes random guess for comp_number using random.randrange()
    comp_choice = number_to_name(comp_number)
    # converts comp_number to comp_choice using the function number_to_name()
    print ("Computer chooses " + comp_choice)
    # prints out the message for computer's choice
    diff = (comp_number - player_number) % 5
    # computes difference of comp_number and player_number modulo five
    if diff == 1 or diff == 2:
        print ("Computer wins!")
    elif diff == 3 or diff == 4:
        print ("Player wins!")
    else:
        print ("Player and computer tie!")
        
        
    # uses if/elif/else to determine winner, print winner message

    
# testing the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
