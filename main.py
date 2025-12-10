import os
import character
import scene
import time
import platform

'''
    Project_name = Desbyte
    Name: Ethan C.
    Reason: Semester project for CYSE-130

    Note: This game took a lot of time and  around 1200 lines of code across 3 python files and 1 json file
'''


# Checks your operating system so it can use the right command to clear the terminal properly
if platform.system() != "Windows": 
    clear = lambda:os.system('clear') #Create a windows version of clearing & determinable with device type
    clear()

else:
    clear = lambda:os.system('cls')
    # This section writes to character and scene to give them the correct version of clearing
    character.character_clearing = 'cls'
    scene.scene_clearing = 'cls'
    clear()

def console(player):
    ''' 

        This function handles every command that you enter. This function communicates with the character file in the user class.
    
    '''
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
            clear()
            player.quest()


        elif user_input == "s" or user_input == "save":
            player.save(1)
        
        elif user_input == "u" or user_input == "upload":
            player.save(2)

        elif user_input == "r" or user_input == "override" or user_input == "restore":
            player.save(3)

        elif user_input == "sh" or user_input == "shop":
            player.store()
        
        else:
            clear()
            x = 0
            print('Please use the \"Help\" Command for valid commands')


        try:
            if user_input.split()[0] == "use":
                clear()
                item_id = int(user_input.split()[1])
                player.use_item(item_id)
        except:
            clear()
            x = 0
            print('Please use the \"Help\" Command for valid commands')

def main():
    clear()
    '''
        The beginning of the game
    '''


    up = input("Would you like to upload your save (Y/N)\n---> ").lower()
    if up == "y":
        player = character.user(up=up)
    else:
        user_name = str(input("What's your name:\n---> "))
        if user_name == "":
            print("You can't have an empty name...")
            print("Default user_name: Aiden")
            time.sleep(2.25)
            player = character.user(name="Aiden")
        else:
            player = character.user(name=user_name)

    clear()
    scene.opening()
    
    if player.quest_num == 0:
        scene.intro(player)

    console(player)


if __name__ == "__main__":
    main()
