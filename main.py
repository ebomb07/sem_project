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
            user_input = input("Would you like to save (y/n)\n---> ")
            if user_input == "y":
                player.save(1)
            else:
                print("Quiting the game *not saving*")
            exit()

        elif user_input == "help" or user_input == "h":
            clear()
            x = 0
            scene.help()

        elif user_input == "clear" or user_input == "cls" or user_input == "c":
            clear()
            x = 0

        elif user_input == "m" or user_input == "map":
            player.map()
    
        elif user_input == "i" or user_input == "info":
            player.information()

        elif user_input == "q" or user_input == "quest":
            player.quest()


        elif user_input == "s" or user_input == "save":
            player.save(1)
        
        elif user_input == "u" or user_input == "upload":
            player.save(2)

        elif user_input == "r" or user_input == "override" or user_input == "restore":
            player.save(3)

        else:
            clear()
            x = 0
            print('Please use the \"Help\" Command for valid commands')



def main(): #WORK ON THE QUESTIONS
    scene.opening_scene()
    up = input("Would you like to upload your save (Y/N)\n---> ").lower()
    if up == "y":
        player = user(up=up)
    else:
        user_name = str(input("What's your name:\n---> "))

        player = user(name=user_name)


    scene.name = player.name
    
    if input("<SKIP INTRO>") != "":
        scene.intro_scene()
    
    else: #FOR TESTING AND DEBUGGING
        #reward = npc.format_question()
        #player.quest_complete()
        #input()
        pass

    console(player)






if __name__ == "__main__":
    main()
