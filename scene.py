import random
import time
import os


clear = lambda:os.system('clear')


def opening_scene():
    print("Welcome to DesByte")
    print("Semester Project (CYSE-130)")
    print("Created by: Ethan C.")
    time.sleep(3)
    clear()


def intro_scene():
    clear()
    print(f"Z: Hello {name}")
    time.sleep(0.5)

    print(f"Z: My team has just established a new network.")
    time.sleep(2.25)

    print(f"Z: We would like you to create a new task force and help the people of Day City.")
    time.sleep(3.25)

    print(f"Z: I will help with your setup. Please stand by...")
    input("\n\n[Press <Enter> to continue]")
    tutorial_scene()


def tutorial_scene():
    clear()

    print("Z: I'm going to teach you a few things about the network.")
    time.sleep(1.25)

    print("Z: Firstly the terminal looks like this \">>>\"")
    time.sleep(2)

    print("Z: This is where you are going to be typing commands.")
    time.sleep(2.25)
    
    print("Z: You will have access to mutliple tabs.")
    time.sleep(2.25)

    help()
    time.sleep(2.25)

    print("Z: When you complete quests you will have another active one")
    time.sleep(2.25)

    print("Z: On top of that you get rewards after completing quests")
    time.sleep(2.25)

    print("Z: But be careful with your timing and choice, because people will remember")
    time.sleep(2.25)

    print("Z: Please explore the map and use your skills for good")
    time.sleep(2.25)

    print("Z: I will reach out to you with future quest")
    time.sleep(2.25)

    print("Z: GoodBye for now...")

    input("\n\n[Press <Enter> to continue]")

def help():
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
    print("use: use an item")
    print("-1: Exit game\n\n")

