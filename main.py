print('''
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
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

def start_game(choice):
    handle_choice(choice, handle_choice1)

def handle_choice(choice, handle_func):
    if choice == "": return
    else: handle_func(choice)

def handle_choice1(choice):
        if choice != "left": 
            print("You fell into a hole. Game Over.")
            return
        else:
            choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
            handle_choice(choice2, handle_choice2)

def handle_choice2(choice):
        if choice != "wait":
            print("You get attacked by an angry trout. Game Over.")
            return
        else: 
            final_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
            handle_choice(final_choice, handle_final_choice)

def handle_final_choice(choice):
          if choice == "yellow":
                    print("You found the treasure! You Win!")
          elif choice == "red":
                    print("It's a room full of fire. Game Over.")
          elif choice == "blue":
                    print("You enter a room of beasts. Game Over.")
          else: print("Wrong input! Game Over.")

start_game(choice)