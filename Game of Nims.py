
name = input ("what is your name matty ")
UrserInput=""
print("Welcome to the sea matty")
print("You and your crew have been on the seas for decades")
print("many of your crew have fallen in depts of the sea")
print("you and your first mate are the last members of your crew")
print("on this peticular day you are out on the sea when a hungry shark start's to attack you")
choice= input("Do you Fight the shark?")
if choice == "Yes":
        input("You and your first mate battled the shark " +name)
elif choice == "No":
        input("The shark swam up to you and use its mighty jaws to ate you and the ship in one bite ")
        print("Game Over")
        quit()
        choice_is_valid = True
else:
        input ("Because you took so long to think the shark swam up and ate you with one bite ")
        print("game over")
        quit()

print("In the end you defeated the shark but you lost your first mate to the foul of the beast")
print("amoung your weeping you notice a shark tooth that lead to Davy Jones secret treasure")
print("you decied to avange your first mate by going after the treasure")
print("After days of searching on the high sea you found the secret entrance to the temple of Davy Jones")
print("You then notice a sacred treasure chest and run after it when you heard your name")
print("Davy Jones:" + name)
print("Davy Jones: I have notice you for sometime and know you are after me treasure")
print("Davy Jones: so I shall give you me treasure but first lets have a little wager.")
print("you started to look confuse")
print("Lets play a game of coins if you win you can have me treasure but if I win I shall take the life")
choice = input("Do you agree? " + name)
if choice == "Yes":
        input("Davy Jones: You made a wise choice lad")
        print("Davy Jones: prepared to die hehehehehe")
        print("Ok matty here are the rules you and davy jones will take turn takeing 1, 2, or 3 coins who ever pick a coin on the last coin wins ok matty")

import random
import os

START_NUM = 13 
LEVEL = 1  # Only 1 and 2 available
if LEVEL not in [1, 2]:
    raise ValueError("That level isn't available. 1 or 2 only.")


def choose_player():
    if random.randint(0, 1) == 0:
        return "human 1"
    else:
        return "Human 2"


def player_turn():
    global current_number
    player_choice = input("Player One, take away 1, 2, or 3 coins? ")
    while player_choice not in ["1", "2", "3"]:
        player_choice = input("Invalid input. Take away 1, 2, or 3 coins? ")
    player_choice = int(player_choice)
    current_number = current_number - player_choice
    print()
    if current_number <= 0:
        print("You win the bet!")
        print("davy Jones: no how could I lose even with the extra help!")
        print("So in the end Davy Jones was defeated and you got the legendary treasure")
        print("The End")
        quit()


def Davvy_Jones():
    global current_number
    player_choice = input("Davvy Jones, take away 1, 2, or 3 coins")
    while player_choice not in ["1", "2", "3"]:
        player_choice = input("Invalid input. Take away 1, 2, or 3 coins? ")
    player_choice = int(player_choice)
    current_number = current_number - player_choice
    print()
    if current_number <= 0:
        print("Davy Jones Wins!")
        print("Davy Jones: thank you player two now I can kill you " + name)

def play_again():
    print()
    return input("Would you like to try again (yes or no)? ").lower().startswith("y")


def main():
    global current_number
    lets_play_again = True

    while lets_play_again:
        current_number = START_NUM
        current_player = choose_player()

        while current_number > 0:
            print(f"The current number is {current_number}.")
            print()
            if current_player == "human":
                player_turn()
                current_player = "Davvy Jones"
            else:
                Davvy_Jones()
                current_player = "human"
        if not play_again():
            lets_play_again = False

    print()
    print("so long matty thanks for playing")


if __name__ == "__main__":
    main()