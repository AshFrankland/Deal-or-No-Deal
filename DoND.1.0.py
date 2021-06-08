import os
import random
#this os method clears the terminal, it's very neat
os.system("cls||clear")

#this sets up our list of boxes from 1 - 22 and the possible prize values
nums22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,]
prize_nums = [
    1, 10, 50, 100, 500, 1000, 5000, 10000, 25000, 50000, 75000,
    100000, 300000, 500000, 1000000, 1500000, 2000000, 3500000, 5000000, 7500000, 10000000, 25000000,
]
prize_strings = [
    "1p", "10p", "50p", "£1", "£5", "£10", "£50", "£100", "£250", "£500", "£750",
    "£1,000", "£3,000", "£5,000", "£10,000", "£15,000", "£20,000", "£35,000", "£50,000", "£75,000", "£100,000", "£250,000",
]
yes_words = ["deal", "swap", "yes", "y", "yeah", "ye", "yep", "sure", "yeh", "yeh boi",]
no_words = ["no deal", "keep", "no", "n", "nope", "nah", "hell no",]

#this makes a copy of the lists which allows us to make edits during the game
box_list = nums22.copy()
prize_shuffle = nums22.copy()
random.shuffle(prize_shuffle)

game_instructions = """
<GAME INSTRUCTIONS>
There are 22 random boxes presented to you, each contain a random prize inside.
The goal is to remove the smallest values from play, thus maximising the potential value of your prize.
Upon starting the game, you will select a box to keep with you throughout the game.
Once you have chosen your first box, you will then start choosing boxes, in turn removing prizes from the pool of prizes.
Once 6 boxes have been removed from play, the 'banker' will call, offering you a prize deal that if accepted, ends the game.
The bankers deal is based on the value of the prizes remaining in the game; he may offer you a bad deal if high value boxes remain in play!
Think carefully before accepting! The banker will continue to offer you deals occasionally throughout the game.
You will continue choosing boxes until only two boxes are left; your original box and the last one in play.
You are now presented the choice to open your box or swap it with the last remaining box in play.
Upon revealing the values of either boxes, the end prize is established and the game ends!
"""

#this prints the boxes in boxes
def show_boxes():
    for i in box_list:
        print("|{}|".format(i), end=" ")
    print()
    print()

#this prints the prizes still in boxes
def show_prizes():
    if player_box == "box":
        for i in range(11):
            print("| {} || {} |".format(prize_strings[i].ljust(8), prize_strings[i + 11].rjust(8)))
        print()
    elif choice_dond == "no deal":
        for i in range(5):
            print("| {} || {} |".format(prize_strings[i].ljust(8), prize_strings[i + 11].rjust(8)))
        print("| {} || {} |".format(prize_strings[5].ljust(8), prize_strings[5 + 11].rjust(8)), end=" ")
        print("     Your box: |{}|".format(player_box))
        for i in range(6,11):
            print("| {} || {} |".format(prize_strings[i].ljust(8), prize_strings[i + 11].rjust(8)))
        print()
    else:
        for i in range(5):
            print("| {} || {} |".format(prize_strings[i].ljust(8), prize_strings[i + 11].rjust(8)))
        print("| {} || {} |".format(prize_strings[5].ljust(8), prize_strings[5 + 11].rjust(8)), end=" ")
        print("     Your box: |{}|".format(player_box))
        print("| {} || {} |".format(prize_strings[6].ljust(8), prize_strings[6 + 11].rjust(8)), end=" ")
        print("     Your deal: {}".format(current_prize))
        for i in range(7,11):
            print("| {} || {} |".format(prize_strings[i].ljust(8), prize_strings[i + 11].rjust(8)))
        print()

#this run checks to make sure the player has input a valid number
def check_box_num(box_num):
    while box_num.isnumeric() == False:
        box_num = input("Please select a box: ")
        print()
        if box_num.isnumeric():
            if box_list.count(int(box_num)) == 0:
                box_num = "box"
    return box_num

#this removes the box the player chose from the list
def remove_box(box):
    box_list.pop(int(box) - 1)
    box_list.insert(int(box) - 1, "_")

#this removes the prize that was in an opened box
def remove_prize(box):
    prize_key = prize_shuffle[int(box) - 1]
    prize_nums.pop(prize_key - 1)
    prize_nums.insert(prize_key - 1, "0")
    prize_strings.pop(prize_key - 1)
    prize_strings.insert(prize_key - 1, "        ")

#this is the banker call function
def banker_call():
    if box_list.count("_") % 3 == 0 and box_list.count("_") >= 6 and choice_dond == "no deal":
        banker_offer()

def banker_offer():
    global choice_dond, current_prize, box_prize
    print("BANKER IS CALLING...")
    print("...")
    prize_sum = 0
    for i in prize_nums:
        prize_sum = prize_sum + int(i)
    banker_offer = round(prize_sum / (100 * (23 - box_list.count("_"))), 2)
    if banker_offer >= 1:
        banker_offer = "£{:,.2f}".format(banker_offer)
    else:
        banker_offer = "{:.0f}p".format(100 * banker_offer)
    print("The Banker offers you {}".format(banker_offer))
    print()
    choice_dond = "dond"
    while choice_dond == "dond":
        choice_dond = input("Do you accept the bankers offer? ")
        print()
        if choice_dond in yes_words:
            print("You accepted the bankers offer!")
            print()
            choice_dond = "deal"
            box_prize = current_prize
            current_prize = "{}".format(banker_offer)
        elif choice_dond in no_words:
            choice_dond = "no deal"
        else:
            print("I didn't understand that, try again")
            choice_dond = "dond"

#this is the pre game/intro text where player name, job and hometown is established. also player is presented with option to read instructions
print()
print("Hello! Welcome to Deal Or No Deal!")
print()
player_name = input("let's get to know each other first... What is your name?: ")
os.system("cls||clear")
player_home = input(f"... and where are you from {player_name}?: ")
os.system("cls||clear")
player_job = input(f"... and what is your job title, in the most simplest terms, {player_name}?: ")   
os.system("cls||clear")
print(f"OK, {player_name}, who is a {player_job} from {player_home}!")
print()
tutorial = "choice"
while tutorial == "choice":
    tutorial = input("Would you like to hear the instructions first?: ")
    os.system("cls||clear")
    if tutorial in yes_words:
        print(str(game_instructions))
        input("Press <ENTER> to continue")
        tutorial = "tutorial"
        os.system("cls||clear")
    elif tutorial in no_words:
        print(f"Ok {player_name}, let's jump straight in...")
        tutorial = "no tutorial"
        os.system("cls||clear")
    else:
        print("I didn't understand that, try again")
        tutorial = "choice"

#intro screen
player_box = "box"
choice_dond = "no deal"
show_boxes()
show_prizes()
print("Let's play Deal or No Deal")
print()

#this code has the player choose their first box
player_box = check_box_num(player_box)
current_prize = prize_strings[prize_shuffle[int(player_box) - 1] - 1]
box_prize = current_prize
remove_box(player_box)
os.system("cls||clear")
show_boxes()
show_prizes()

#this asks the player which box to remove next and loops until there's one box left
while box_list.count("_") < 21:
    banker_call()
    next_box = "box"
    next_box = check_box_num(next_box)
    lost_prize = prize_strings[prize_shuffle[int(next_box) - 1] - 1]
    remove_box(next_box)
    remove_prize(next_box)
    os.system("cls||clear")
    show_boxes()
    show_prizes()
    print("The last box contained {}".format(lost_prize))
    print()

print("There is now 1 box remaining!...")
if choice_dond == "no deal":
    banker_offer()
#here we give the player the choice of choosing to swap their original box with the last remaining box
keep_or_swap = "choice"
while keep_or_swap == "choice":
    keep_or_swap = input("Would you like to swap box {} for the last box? ".format(player_box))
    print()
    if keep_or_swap in no_words:
        print("You have chosen to keep your original box")
        keep_or_swap = "keep"
    elif keep_or_swap in yes_words:
        print("You have chosen to swap your original box")
        keep_or_swap = "swap"
    else:
        print("I didn't understand that, try again")
        keep_or_swap = "choice"

#this swaps the last two boxes if swap was selected
if keep_or_swap == "keep":
    print()
else:
    print()
    old_player_box = player_box
    for i in range(21):
        box_list.remove("_")
    player_box = str(box_list[0])
    box_prize = prize_strings[prize_shuffle[int(player_box) - 1] - 1]
    if choice_dond == "no deal":
        current_prize = box_prize

#here are the results of the players choice
if keep_or_swap == "keep":
    print("Box number {} contained {}".format(player_box, box_prize))
else:
    print("You swapped box number {}, for box number {} containing {}".format(old_player_box, player_box, box_prize))

#end screen
print()
print("Game Over, you won {}".format(current_prize))