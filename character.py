import random
import time
import scene
import os

clear = lambda:os.system('clear')


class npc:
    def __init__(self,name,dig_opt):
        self.name = name
        self.dig_opt = dig_opt

    def random():
        random.seed(time.time())
        
        names = [
            "Bill",
            "Mary",
            "James",
            "Sam",
            "Jane"
        ]

        dialogue = [
            "Can you please help us with this problem?"
        ]


        return (names[random.randint(0,len(names)-1)], dialogue[random.randint(0,len(dialogue)-1)], scene.question_getter()) #0: Name ; 1: dialogue ; 2: question




    def z(dig_opt): # Mentors dialouge
        dialogue = [
            "testing"
        ]

        if len(dialogue) - 1 < dig_opt:
            return -1
        else:
            return dialogue[dig_opt]
    
class user:

    def __init__(self,name = "NULL", health=100, support=40, moral=75, money=100,quest_num = 0, inventory=[]):
        self.name = name
        self.health = health
        self.support = support
        self.moral = moral
        self.money = money
        self.quest_num = quest_num
        self.inv = inventory


    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.health}\nSupport: {self.support}\nMoral: {self.moral}\nMoney: {self.money}\nInventory:{self.inv}"


    def damage(self, type_of_dmg=-1, dmg=0):
        if type_of_dmg == -1:
            return -1

        elif type_of_dmg == 1: # Health damage
        
            self.health -= dmg
        
        elif type_of_dmg == 2: # Support damage
            
            self.support -= dmg
        
        elif type_of_dmg == 3: # Moral damage

            self.moral -= dmg

        elif type_of_dmg == 4: # money damage
            self.money -= dmg


    def healing(self, type_of_healing=-1, heal=0):
        
        if type_of_healing == -1:
            return -1
        elif type_of_healing == 1: # Health healing 
            self.health += heal

        elif type_of_healing == 2: # Support healing 
            self.support += heal

        elif type_of_healing == 3: # Moral healing 
            self.moral += heal
        
        elif type_of_healing == 4: # Money healing
            self.money += money


    def inventory_add(self,item):
        self.inv.append(item)

    def inventory_remove(self,item):
        self.inv.remove(item)


    def map(self):
        print("map")

    def information(self):
        print(f"\n\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Support : {self.support}")
        print(f"Moral: {self.moral}")
        print(f"Money: {self.money}")

        print(f"Inventory: {self.inv}\n\n")


    def quest(self):
        active = True

        while active:
            available_quests = [ #Format: <NAME> <Description> <required support> <reward support> <next index>

                    ["Tutorial", 
                     "The tutorial teaches you the basics of the game and controls",
                     0,
                     0,
                     1],

                    ["First_mission",
                     "Help a Civilian with their task",
                     0,
                     10,
                     2]

            ]
            active_quests = []

            active_quests.append(available_quests[0])
           
            completed_quests = []
            completed_quests.append(available_quests[1])



            print("Active Quests (input corresponding numbers for more information (-1 return)):\n")

            for i in range(len(active_quests)):
                print(f"{i+1} - {active_quests[i][0]}")


            print("\n\nCompleted quests:")

            for i in range(len(completed_quests)):
                print(f"{i+1}C - {completed_quests[i][0]}")


            user_input = input("\n\n-> ")
        

            try:
                user_input = int(user_input)
                extend = True

            except:
                extend = False
            

            try:
                user_check = list(user_input)
            
            except TypeError:
                user_check = []



            if user_input == -1:
                active = False
                clear()

            elif len(user_check) == 2 and user_check[1].lower() == "c" and user_check[0].isnumeric() == True and int(user_check[0]) <= len(completed_quests) and int(user_check[0]) > 0:

                clear(
                ind = int(user_check[0]) - 1

                print(f"Name: {completed_quests[ind][0]}")
                print(f"Description: {completed_quests[ind][1]}")
                print(f"Reward: {completed_quests[ind][3]} Support")

                input("\n\n[Press <Enter> to continue")
                clear()

            elif user_input != -1 and extend == True and user_input == 1:
                clear()
                print(f"Name: {active_quests[user_input - 1][0]}")
                print(f"Description: {active_quests[user_input - 1][1]}")
                print(f"Reward: {active_quests[user_input - 1][3]} Support")

                input("\n\n[Press <Enter> to continue]")
                clear()
