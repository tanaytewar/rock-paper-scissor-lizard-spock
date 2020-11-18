"""
Rock-paper-scissors-lizard-Spock game
"""
import random
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
    if name=="rock":
        return 0
    elif name=="spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    elif name=="scissor":
        return 4
    else:
        return "Error: Enter either of the following 5: rock/paper/scissor/lizard/spock"  
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    if number==0:
        return "rock"
    elif number==1:
        return "spock"
    elif number==2:
        return "paper"
    elif number==3:
        return "lizard"
    elif number==4:
        return "scissor"
    else:
        return "Error: Enter positive value less that 5"
def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    # print out message for computer's choice
    print("Computer's choice: ",comp_choice)
    # compute difference of player_number and comp_number modulo five
    diff=(player_number-comp_number)%5
    # use if/elif/else to determine winner and print winner message
    if diff==1 or diff==2:
        print("You win this round!")
        #player_score=player_score+1
    elif diff==3 or diff==4:
        print("Computer wins this round!")
        #comp_score=comp_score+1
    else:
        print("Tie! No one wins!")
rounds=int(input("Enter the number of rounds you want to play:"))
for i in range(rounds):
    print("ROUND",i+1)
    player_choice=input("Enter your choice from rock/paper/scissor/lizard/spock/exit: ")
    print("Your choice: ",player_choice)
    rpsls(player_choice)
    #print("Computer score is:{} \nPlayer score is:{}".format(comp_score,player_score))
    print("----------------------------------------------------------")