import random
import time
import os
import character

scene_clearing = "clear"
clear = lambda:os.system(f"{scene_clearing}")


'''
    This file handles all the scenes for the main quest line of the game.
    In basic terms it is majority print statments and time.sleep(x) for reading.
    near the end there are different paths you can take for different endings and dialogue
'''


def opening(): # opening scene
    print("Welcome to DesByte")
    print("Semester Project (CYSE-130)")
    print("Created by: Ethan C.")
    time.sleep(3)
    clear()


def intro(player): #Intro Scene
    clear()
    print(f"Z: Hello {player.name}")
    time.sleep(0.5)

    print(f"Z: My team has just established a new network.")
    time.sleep(2.25)

    print(f"Z: We would like you to create a new task force and help the people of Day City.")
    time.sleep(3.25)

    print(f"Z: I will help with your setup. Please stand by...")
    input("\n\n[Press <Enter> to continue]")
    tutorial(player)


def tutorial(player): # Tutorial scene
    clear()

    print("Z: I'm going to teach you a few things about the network.")
    time.sleep(1.25)

    print("Z: Firstly the terminal looks like this \">>>\"")
    time.sleep(2)

    print("Z: This is where you are going to be typing commands.")
    time.sleep(2.25)
    
    print("Z: You will have access to multiple tabs.")
    time.sleep(2.25)

    help()
    time.sleep(2.25)

    print("Z: When you complete quests you will have another active one")
    time.sleep(2.25)

    print("Z: On top of that you get rewards after completing quests")
    time.sleep(2.25)

    print("Z: However be careful because if you get questions wrong you start to lose health.")
    time.sleep(2.25)

    print("Z: But be careful with your choices, because people will remember")
    time.sleep(2.25)

    print("Z: Please explore the map and use your skills for good")
    time.sleep(2.25)

    print("Z: Reach out to me when you are ready")
    time.sleep(2.25)

    print("Z: Goodbye for now...")

    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    #first_mission()


def first_mission(player): # First mission scene
    clear()
    print("Z: Okay we are going to break through desbyte, and solve one of their questions.")
    time.sleep(2.25)

    player.desbyte_question_handler(0,player)

    print("Z: GOOD JOB! you just solved one of desbytes questions.")
    time.sleep(2.25)

    print("Z: But there are more things we have to do to stop desbyte for good.")
    time.sleep(2.25)

    print("Z: Contact me when you are ready")
    time.sleep(1)

    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    

def combat_desbyte(player): # Combat desbyte mission scene
    clear()
    print("Z: Okay all we have to do is...")
    time.sleep(1)
    print("Z: ...")
    time.sleep(1)
    print("Z: WHO ARE YOU?!?!?!")
    time.sleep(1.5)
    print("Z: ...")
    time.sleep(0.5)
    print("Z: ...")
    time.sleep(1.5)
    print("\n\n")

    print(f"{player.name}: Where did he go?")
    time.sleep(2.25)

    print(f"{player.name}: ...")
    time.sleep(2)

    print(f"{player.name}: There is a note.")
    time.sleep(2)

    print(f"{player.name}: I think I have to solve their question.")
    time.sleep(2)

    player.desbyte_question_handler(1,player)

    print(f"Z: Thank you for helping me {player.name}")
    time.sleep(1.5)

    print(f"Z: As I was going to say. You have to go retrieve the codes from desbyte.")
    time.sleep(2.25)

    print("Z: When you are ready go and retrieve the codes.")
    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    

def retrieve_the_codes(player): # retrieve the codes scene
    clear()
    print(f"{player.name}: Okay this is the time. I need to get these codes.")
    time.sleep(2)

    print(f"{player.name}: All I have to do go into their building and complete their question.")
    time.sleep(2.25)

    print(f"{player.name}: Okay it\'s go time.")
    time.sleep(2.25)

    player.desbyte_question_handler(2,player)

    print(f"{player.name}: Perfect I got the codes. I have to let Z know.")
    time.sleep(2.25)
    clear()

    print("You call Z...")
    time.sleep(1.5)
    print("Calling...")
    time.sleep(1)
    print("Calling...")
    time.sleep(1)
    print("Calling...")
    time.sleep(1)

    print(f"{player.name}: Why isn't he picking up?")
    time.sleep(2)

    print("An unknown number is calling...")
    user_check = ""
    active = True
    while active: # Makes sure you choose to answer or not answer the phone
        user_check = input("do you answer (Y/N)\n>>> ").lower()
        if user_check == "y": # you answer the phone
            player.call = True
            active = False
            print("Unknown: I am sorry to inform you but Z has been taken.")
            time.sleep(2)
            print("Unknown: You have to get him back.")
            time.sleep(2)
            print("Unknown: I can't stop them in my condition.")
            time.sleep(2)
            print("Unknown: Please...")
            time.sleep(1)
            print("Call ended")

        elif user_check == "n": # you don't answer the phone
            player.call = False
            active = False
            print(f"{player.name}: That was weird...")
            time.sleep(1)

            print(f"{player.name}: Hopefully that wasn\'t important.")

    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    

def Final_mission(player): # Final mission scene
    clear()

    if player.call == True: # if you did pick up the phone
        print(f"{player.name}: Okay I have to take down desbyte and save Z.")
        time.sleep(2.25)
        print(f"{player.name}: This is the only time I can do it.")
        time.sleep(2.25)
        print(f"{player.name}: This is the most vulnerable they have been.")
        time.sleep(2.25)
        player.desbyte_question_handler(3,player)

        print(f"{player.name}: I'm so glad I was able to save you")
        time.sleep(2.25)
        print("Z: I can't thank you enough for helping me.")
        time.sleep(2.25)
        print("Z: Desbyte has now fallen. You have saved the world.")
        time.sleep(2.25)
        print("Z: Take some rest you deserved it. When you are ready, reach out again and I have 1 more thing I want you to do.")
        player.ending = True
    else: # if you didn't pick up the phone
        print(f"{player.name}: Okay I have to take down desbyte")
        time.sleep(2.5)
        print(f"{player.name}: I'm still confused why Z isn't answering and who that call was from.")
        
        time.sleep(1)
        print("...")
        time.sleep(0.75)
        print("...")
        time.sleep(1)

        print(f"{player.name}: Anyways this is the only time I can do it.")
        time.sleep(2.5)
        print(f"{player.name}: This is the most vulnerable they have been.")
        time.sleep(2.25)
        player.desbyte_question_handler(3,player)

        print(f"{player.name}: I DID IT.")
        time.sleep(2.25)
        print(f"{player.name}: I wonder where Z is...")
        time.sleep(1)
        print("...")
        time.sleep(0.75)
        print("...")
        time.sleep(1)
        player.ending = False

    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    

def good_ending(player): # Good ending scene
    clear()
    print("Z: I still can't thank you enough for saving me.")
    time.sleep(1.5)
    print("Z: I wouldn't have been able to get out without your help.")
    time.sleep(1.5)
    print("Z: Okay I have one more mission for you...")
    time.sleep(1.5)
    print("Z: I want you to turn the switch on to give the city their network back.")
    time.sleep(1.5)
    print("Z: You have been doing all of the heavy lifting and you deserve it.")
    time.sleep(2.5)

    user_check = ""
    active = True
    while active: # makes sure you choose to either flip the lever or not
        user_check = input("Do you flip the lever? (Y/N)\n>>> ").lower()
        if user_check == "y": # you flip the lever
            clear()
            active = False
            print("You flip the lever...")
            print("Z: I can't believe that we saved the city from ruins.")
            time.sleep(2.25)
            print("Z: People can finally return to their lives and not worry about anything.")
            time.sleep(2)
            print("Z: We all owe you everything.")
            time.sleep(2.5)
            print("Z: However I have to go know, and this might be the last time you see me.")
            time.sleep(2)
            print(f"Z: It has been an honor and privilege {player.name}.")
            time.sleep(2.75)
            print(f"Z: Goodbye...")
            

        elif user_check == "n": # you don't flip the lever
            clear()
            active = False
            print("You don't flip the lever")
            print("Z: What are you doing???")
            time.sleep(1.25)
            print("Z: We are so close to saving everyone")
            time.sleep(1.75)
            print("You destroy the machine...")
            time.sleep(1.5)
            print("Z: WHAT ARE YOU DOING.")
            time.sleep(0.5)
            print("Z: YOU DESTROYED ALL OF OUR PROGRESS")
            time.sleep(0.5)
            print("Z: EVERYTHING IS GONE.")
            time.sleep(0.5)
            print("Z: DON'T EVER SHOW YOUR FACE AROUND HERE AGAIN...")
            time.sleep(0.5)
            print("Z: YOU REMOVED THE DAY FROM THIS CITY")
            time.sleep(0.5)
            print("Z: THIS CITY WILL ALWAYS BE NIGHT")
            input("\n\n[Press <Enter> to continue]")
            clear()
            print("A year passes by...")
            print("You walk by the city hall and on the sign it says")
            print("Welcome to Night_city\nest. 2077")
            player.city_name = "Night_city"

        

    input("\n\n[Press <Enter> to continue]")
    player.quest_complete()
    end_credits(player)



def bad_ending(player): # bad ending scene 
    clear()
    print("You're getting a call...")
    time.sleep(1.5)

    print("Unknown: YOU DIDN\'T PICK UP MY CALL.")
    time.sleep(1.5)

    print("Unknown: Z WAS TAKEN BY THEM.")
    time.sleep(1.5)

    print("Unknown: YOU COULD\'VE SAVED HIM.")
    time.sleep(1.5)

    print("Unknown: AND NOW IT IS TOO LATE")
    time.sleep(2)

    print("Call ended...")
    time.sleep(1)
    print("You have recieved a text message")
    time.sleep(2.25)
    input("[Press <Enter> to continue]")
    clear()

    print(f"{'Unknown':^15}")
    print(f"{'_':_^15}")
    print("")

    print("Unknown -> Z would want you to go to his funeral.")
    print("Unknown -> Address: 4400 University Dr, Fairfax, VA 22030")
    print("Unknown -> Date & Time: 12/10/25 @ 23:59")
    print("Unknown has blocked you")

    input("\n\n[Press <Enter> to continue]")

    print(f"{player.name}: I am so sorry...")
    player.quest_complete()
    end_credits(player)

def end_credits(player): # end credits scene
    clear()
    message = "Congratulations on completing the game.\nThis game took many hours and over 1000 lines of code across 3 python files and 1 json file. Aside from that here are your stats from your game."
    len_message = len(message)
    message = message.split()

    next_message = player.__str__().split()

    
    for word in message:
        for char in word:
            print(char,end="", flush=True)
            time.sleep(328/3600) #328/3600 <average wpm of reading>/ 3600 (to get word/second)
        print(" ",end="")
    print('\n')
    print("-"*len_message)
    print("\n\n\n")

    for i,word in enumerate(next_message): #information tab printing
        for char in word:
            print(char, end="", flush=True)
            time.sleep(328/3600)
        if i % 2 == 1:
            print("\n")
        else:
            print(" ", end = "")

    print("-"*len(f"Inventory: {str(player.inv)}"))

    time.sleep(1.25)
    len_end_message = 0


    # All below is last mentions of the program

    if player.call == False:
        next_message = "\nYou didn't pick up the phone to protect Z. This lead to you getting the bad_ending."
    else:
        next_message = "\nYou picked up the phone and saved Z, leading to you getting the good_ending."
    
    len_end_message = len(next_message)

    time.sleep(1.25)
    if player.call == True and player.city_name == "Day_city":
        next_message += "\n\nSince you flipped the lever and saved the city you earned the really good ending."
        len_end_message = len("\n\nSince you flipped the lever and saved the city you earned the really good ending.")

    elif player.call == True and player.city_name == "Night_city":
        next_message += "\n\nSince you didn't flip the lever you brought the city into darkness. This brought you to the good-bad ending"
        next_message += "\nNote: The name and year is a reference to the game and show cyberpunk."
        len_end_message = len("\nNote: The city name and year is a reference to the game and show cyberpunk.")


    for i,word in enumerate(next_message): # final messages
        for char in word:
            print(char, end="", flush=True)
            time.sleep(328/3600)
        
        print("", end="")

    print("\n")
    print("-"*len_end_message)
    
    time.sleep(2.25)
    print("\n\n\n\nThank you again for playing my game.")
    input("\n[Press <Enter> to end the game]")

    print("Saving...")
    #player.save(1)
    time.sleep(1)

    exit()
    

def help(): # Help tab (shows all the commands)
    print("Tab Table:\n")
    print("Note: every 5 commands the console will clear")
    print("M | Map: Map tab")
    print("I | Info: Information tab")
    print("Q | Quest: Quests tab")
    print("S | Save: Save your game")
    print("U | Upload: Upload saves")
    print("R | Override | RESTORE: Override all save data")
    print("C | clear | cls: clear terminal")
    print("sh | shop: opens the shop")
    print("use x | use an item (format: user <number corresponding to the inventory slot>)")
    print("-1: Exit game\n\n")

