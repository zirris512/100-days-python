print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction_choice = input(
    'You come across a fork in the road. Do you go "left" or "right"?\n'
).lower()
if direction_choice == "left":
    lake_choice = input(
        '\nYou come across a lake. Do you "look" around or "swim" across?\n'
    ).lower()
    if lake_choice == "look":
        door_choice = input(
            '\nYou find a boat and make it across to an island. You find 3 doors. Do you open the "red", "green", or "blue" door?\n'
        ).lower()
        if door_choice == "red":
            print("You walked into a room of fire. Game Over.")
        elif door_choice == "green":
            print("You have found the treasure! You win!")
        elif door_choice == "blue":
            print("You are attacked by a giant snake. Game Over.")
        else:
            print("You're color blindness was the death of you. Game Over.")
    else:
        print("You got attacked by a serpent and drowned. Game Over.")
else:
    print("You walk into a pit of snakes. Game Over.")
