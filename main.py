import os
from character import user, npc
import scene
import time

clear = lambda:os.system('clear') #Create a windows version of clearing & determinable with device type
clear()


def console(player):
    clear()
    active = True
    x = 0

    while active:
        if x >= 5:
            x = 0
            clear()


        print("Type \"Help\" or \"H\" for more information")
        user_input = input("\n>>> ").lower()
        x += 1

        if user_input == "-1":
            print("Quiting the game *not saving*")
            exit()

        elif user_input == "help" or user_input == "h":
            clear()
            scene.help()

        elif user_input == "clear" or user_input == "cls":
            clear()

        elif user_input == "m" or user_input == "map":
            player.map()
    
        elif user_input == "i" or user_input == "info":
            player.information()

        elif user_input == "q" or user_input == "quest":
            player.quest()

        else:
            clear()
            print('Please use the \"Help\" Command for valid inputs')


def format_help(info):
    print(f"Name: {info[0]}")
    print(f"\"{info[1]}\"\n")
    question = info[2][0]
    answer = info[2][1]

    print(question)

    user_answer = input("\n---> ")
    
    if user_answer == answer:
        print("CORRECT!")
        return True
    else:
        print(f"Wrong, the answer was {answer}")
        return False



def main(): #WORK ON THE QUESTIONS
    scene.opening_scene()
    
    user_name = str(input("What's your name:\n---> "))
    player = user(name=user_name)
    scene.name = user_name
    
    if input() != "":
        scene.intro_scene()
    

    console(player)





if __name__ == "__main__":
    main()
