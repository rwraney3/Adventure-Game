# Robert Raney
# November 23, 2020
# Special thanks to 10minutetrain - thoughts for
# Rock, Paper, Scissors come from his YouTube
# https://www.youtube.com/results?search_query=rock+paper+scissors+python

import time
import random


def indent(count, statement, num):
    print(" " * num, count, statement)


def player():
    print("Please choose '1 - Rock', '2 - Paper' or '3 - Scissors'\n")
    player_choice = input("Enter '1', '2', or '3':\n").lower()
    if player_choice == "1" or "r" in player_choice:
        player_choice = "Rock"
    elif player_choice == "2" or "p" in player_choice:
        player_choice = "Paper"
    elif player_choice == "3" or "s" in player_choice:
        player_choice = "Scissors"
    else:
        print("invalid choice")
        player()
    return player_choice


def computer(character):
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice


def compare(player_choice, computer_choice, character, item):
    cls()
    print("You chose:", player_choice)
    print("The", character, "chose:", computer_choice)
    if player_choice == "Rock":
        if computer_choice == "Rock":
            tie(player_choice, computer_choice, character, item)
        elif computer_choice == "Paper":
            lose(player_choice, computer_choice, character, item)
        else:
            win(player_choice, computer_choice, character, item)
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            win(player_choice, computer_choice, character, item)
        elif computer_choice == "Paper":
            tie(player_choice, computer_choice, character, item)
        else:
            lose(player_choice, computer_choice, character, item)
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            lose(player_choice, computer_choice, character, item)
        elif computer_choice == "Paper":
            win(player_choice, computer_choice, character, item)
        else:
            tie(player_choice, computer_choice, character, item)


def win(player_choice, computer_choice, character, item):
    print("You win! Your", player_choice, "beats the",
          character + "'s", computer_choice + ".\n"
          "You saved the village and are the Hero - For now."
          "\n")


def lose(player_choice, computer_choice, character, item):
    print("You Lose! The", character + "'s",
          computer_choice, "beats your", player_choice + ".\n"
          "The", character, "takes your", item + ".\n"
          "The village is still at risk.\n")
    items.remove(item)


def tie(player_choice, computer_choice, character, item):
    print("You Tie!\n"
          "The village is safe for now,\n"
          "but a Tie is not as good as a Win."
          "\n")


def cls():
    print("\n" * 50)


def print_pause(statement, how_long):
    time.sleep(how_long)
    print(statement)


def is_valid(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print("\nI'm sorry, I don't recognize that response.\n"
                  "")
    return response


def item_count(items):
    key_count = items.count("car keys")
    wallet_count = items.count("wallet")
    match_count = items.count("pack of matches")
    change_count = items.count("loose change")
    jb_count = items.count("bag of jelly beans")
    mm_count = items.count("bag of M&M's")
    oreo_count = items.count("box of Oreos")
    dorito_count = items.count("bag of Doritos")
    print("Your posessions are:\n")
    indent("", "1 Flashlight (YOU WILL NEVER LOSE THIS)", 4)
    indent("", "1 N-95 Mask  (YOU WILL NEVER LOSE THIS)", 4)
    if key_count != 0:
        indent(key_count, "Car key", 5)
    if wallet_count != 0:
        indent(wallet_count, "Wallet", 5)
    if match_count != 0:
        indent(match_count, "Pack of Matches", 5)
    if change_count != 0:
        indent(" ", "Loose Change", 5)
    if jb_count != 0:
        indent(jb_count, "Bags of Jelly Beans", 5)
    if mm_count != 0:
        indent(mm_count, "Bags of MM's", 5)
    if oreo_count != 0:
        indent(oreo_count, "Box(es) of Oreos", 5)
    if dorito_count != 0:
        indent(dorito_count, "Bag(s) of Doritos", 5)


def enter_cave(items, character, item):
    print_pause("\n", 1)
    cls()
    item_count(items)
    cave_items = ["bag of jelly beans", "bag of M&M's",
                  "box of Oreos", "bag of Doritos"]
    item = random.choice(cave_items)
    print("\nYou enter the cave and trip over something.\n"
          "\n"
          "You pull out your flashlight and examine the "
          "object closer, you realize it is a", item + ".\n"
          "\n")
    response = is_valid("Would you like to 'TAKE' the "
                        "treasure 'LEAVE' it on the ground?\n"
                        "Enter 'Take' or 'Leave':\n",
                        "t", "l")
    if "t" in response:
        print_pause("\n", 1)
        cls()
        print("You take the", item, "and go back to the field.\n")
        items.append(item)
        field(items, character, item)
    else:
        print_pause("\n", 1)
        cls()
        print("You leave the", item, "and go back to the field.\n")
        item = []
        field(items, character, item)


def fight(items, character, item):
    print_pause("\n", 1)
    cls()
    if item != []:
        print("You stand your ground, prepared to fight, "
              "when the", character, "challenges you\n"
              "to a game of Rock, Paper, Scissors.\n"
              "\n"
              "If the", character, "wins he gets your", item + ".\n"
              "\n"
              "If you win - you become the hero of the village!\n")
        response = is_valid("Do you accept the challenge?\n"
                            "Enter 'YES' or 'NO':\n",
                            "y", "n")
    else:
        item = random.choice(items)
        print("You stand your ground, prepared to fight, when the", character,
              "challenges you\n"
              "to a game of Rock, Paper, Scissors.\n"
              "\n"
              "If the", character, "wins he gets your", item + ".\n"
              "\n"
              "If you win - you become the hero of the village!\n")
        response = is_valid("Do you accept the challenge?\n"
                            "Enter 'YES' or 'NO':\n",
                            "y", "n")
    if "y" in response:
        player_choice = player()
        computer_choice = computer(character)
        compare(player_choice, computer_choice, character, item)
    else:
        cls()
        print("The", character, "laughs at you and takes your",
              item, "anyway.\n"
              "You leave defeated and deflated!\n")


def field(items, character, item):
    print_pause("\n", 1)
    response = is_valid("You look around and see a cave and an old house.\n"
                        "\n"
                        "Do you want to go to the 'CAVE' or to the 'HOUSE'?\n"
                        "Enter 'CAVE' or 'HOUSE':\n",
                        "c", "h")
    if "c" in response:
        enter_cave(items, character, item)
    else:
        house(items, character, item)


def house(items, character, item):
    print_pause("\n", 1)
    cls()
    character_list = ["ogre", "giant", "troll", "monster"]
    character = random.choice(character_list)
    response = is_valid("You approach the house, making sure "
                        "your mask is on.\n"
                        "As you climb the old, squeaky steps,\n"
                        "you notice how dilapidated the house looks.  "
                        "Soon you are\n"
                        "standing on the porch in front of an enormous door.\n"
                        "\n"
                        "Would you like to 'KNOCK' on the door or 'LEAVE'?\n"
                        "Enter 'KNOCK' or 'LEAVE':\n",
                        "k", "l")
    if "k" in response:
        print_pause("\n", 1)
        cls()
        print("You gulp and knock on the door.  The", character,
              "opens the door.\n"
              "Even behind his N-95 mask he looks terrifying. "
              "He attacks!\n"
              "\n")
        response = is_valid("Do you want to 'FIGHT' or 'RUN'?\n"
                            "Enter 'FIGHT' or 'RUN':\n",
                            "f", "r")
        if "f" in response:
            cls()
            fight(items, character, item)
        else:
            cls()
            print("You turn on your heels and run as fast as you can.\n"
                  "\n"
                  "You hear the", character, "laughing as you go back "
                  "to the field.\n")
            field(items, character, item)
    else:
        cls()
        print("You leave and go back to the field\n")
        field(items, character, item)


def intro(items, character, item):
    cls()
    print("It's a beautiful spring day.\n"
          "You find yourself standing in an open field,\n"
          "the smell of wildflowers and the songs of the birds\n"
          "fill you with a sense of adventure!\n"
          "\n"
          "Rumor has it that an ogre, a giant, a troll, and\n"
          "a monster live somewhere around here,\n"
          "and have been terrifying the nearby village.\n"
          "\n")
    field(items, character, item)


items = ["car keys", "wallet", "loose change", "pack of matches"]
item = []
character = []

intro(items, character, item)
while True:
    print("\n")
    print("Play Again? Yes or No\n")
    print("Enter 'YES' or 'NO'\n")
    again = input().lower()
    if "y" in again:
        cls()
        print("Once again ...")
        field(items, character, item)
    else:
        cls()
        print("I hope you have enjoyed playing - goodbye!\n")
        break
