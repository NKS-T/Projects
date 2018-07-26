
import time

Hands = ["s", "r", "p"]
play = "y"

while play.lower() == "y":
    player_1 = raw_input("Player ONE, Enter Hand: ")
    while player_1.lower() not in Hands:
        player_1 = raw_input("Player ONE, Enter Hand: ")

    time.sleep(1)
    print

    player_2 = raw_input("Player TWO, Enter Hand: ")
    while player_2.lower() not in Hands:
        player_2 = raw_input("Player TWO, Enter Hand: ")

    print

    if player_1.lower() == player_2.lower():
        print ("DRAW")
    elif player_1.lower() == "r":
        if player_2.lower() == "s":
            print ("WINNER: ONE")
        else:
            print ("WINNER: TWO")
    elif player_1.lower() == "p":
        if player_2.lower() == "r":
            print ("WINNER: ONE")
        else:
            print ("WINNER: TWO")
    elif player_1.lower() == "s":
        if player_2.lower() == "p":
            print ("WINNER: ONE")
        else:
            print ("WINNER: TWO")

    print
    play = raw_input("PLAY AGAIN (Y/N)? ")
    print
