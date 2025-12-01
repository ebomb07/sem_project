import random
import time
import scene
import os
import json


clear = lambda:os.system('clear')


class npc:

    def random_question():
        random.seed(time.time())
        
        names = [
            "Bill",
            "Mary",
            "James",
            "Sam",
            "Jane",
            "Cameron",
            "David",
            "Ethan",
            "Somil"
        ]

        dialogue = [
            "Can you please help us with this problem?",
            "HELP! HELP! HELP!"
        ]


        return (names[random.randint(0,len(names)-1)], dialogue[random.randint(0,len(dialogue)-1)], npc.question_getter())

    def question_getter(types=0, pos=0): #Question Format [<question>, <answer>, <reward>]
        random.seed(time.time())
        questions = [
            ["10", "e", 1],
            ["2+3+4+5", "14", 1]
        ]

        desbyte_question = []

        
        if types == 0:
            return questions[random.randint(0,len(questions)-1)]
        else:
            return desbyte_question[pos]

    def format_question():
        clear()
        info = npc.random_question()

        name = info[0]
        dialogue = info[1]
        question = info[2][0]
        answer = info[2][1]
        reward = info[2][2]
        
        print(f"{name}: {dialogue}\n")
        print(f"Question: {question}\n")
        print(f"Reward: {reward} support")

        user_answer = input("\n---> ")
        
        if user_answer == answer:
            print("CORRECT!")
            return reward

        else:
            print(f"Wrong, the answer was {answer}")
            time.sleep(1.5)
            return -1

    

    
class user:

    def __init__(self,name = "NULL", health=100, support=0, moral=75, money=100,quest_num = 0, inventory=[], up = "n"):
        self.active_quests = []
        self.completed_quests = []
        self.available_quests = [ #Format: <NAME> <Description> <required support> <reward support> <next index>

                    ["Tutorial", 
                    "The tutorial teaches you the basics of the game and controls",
                    0,
                    10,
                    1],

                    ["First_mission",
                    "Help a Civilian with their task",
                    0,
                    15,
                    2],

                    ["Combat_desbyte",
                    "Complete the challegnes recieved by the hacker group desbyte",
                    10,
                    20,
                    3],

                    ["Retrieve_the_codes",
                    "Find and retrieve the code to enter desbytes network",
                    20,
                    25,
                    4],

                    ["Final_mission",
                    "Shutdown desbytes network and report the the police",
                    50,
                    30,
                    -1]

            ]

        if up == "n":

            self.name = name
            self.health = health
            self.support = support
            self.moral = moral
            self.money = money
            self.quest_num = quest_num
            self.inv = inventory
            
            if self.quest_num == 0: #ADD AN UPLOAD COMPLETED QUEST
                self.active_quests.append(self.available_quests[self.quest_num])
            else:
                self.active_quests.append(self.available_quests[self.quest_num - 1])
        elif up == "y":
            self.save(2)
        
        else:
            print("Y/N")


    def save(self, mode=None):

        if mode == None:
            return -1
        elif mode == 1: # Save to file
            with open("save.json","r") as file:
                info = json.load(file)
                print(info["quest_num"])

                info["name"] = self.name
                info["health"] = self.health
                info["support"] = self.support
                info["moral"] = self.moral
                info["money"] = self.money
                info["quest_num"] = self.quest_num
                info["inv"] = self.inv

            with open("save.json", "w") as fp:
                json.dump(info, fp)
        
        elif mode == 2:
            with open("save.json","r") as file:
                info = json.load(file)
                print(info["quest_num"])

                self.name = info["name"]
                self.health = info["health"]
                self.support = info["support"]
                self.moral = info["moral"]
                self.money = info["money"]
                self.quest_num = info["quest_num"]
                self.inv = info["inv"]
                self.active_quests.append(self.available_quests[self.quest_num])
                self.quest_num = self.active_quests

                for i in range(self.active_quests[0][-1] - 1):
                    self.completed_quests.append(self.available_quests[i])


        elif mode == 3:
            
            if input(f"Type CONFIRM_{self.name} to restore to default\n---> ") == f"CONFIRM_{self.name}":
                print("OVERRIDING...")
                with open("save.json","w") as fp:
                    default = {
                        "name": "",
                        "health": 0,
                        "support": 0,
                        "moral": 0,
                        "money": 0,
                        "quest_num": 0,
                        "inv": []
                    }

                    json.dump(default,fp)
                    clear()
            else:
                return -1

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
            if self.health + heal <= 100:
                self.health += heal
            else:
                self.health = 100
                print("you have reached the maximum of 100 health")

        elif type_of_healing == 2: # Support healing 
            if self.support + heal <= 100:
                self.support += heal

            else:
                self.support = 100
                print("You have reached the maximum of 100 Support")

        elif type_of_healing == 3: # Moral healing 
            if self.moral + heal <= 100:
                self.moral += heal
            else:
                self.moral = 100
                print("You have reached the maximum of 100 moral")
        
        elif type_of_healing == 4: # Money healing
            self.money += money

    def inventory_add(self,item):
        self.inv.append(item)

    def inventory_remove(self,item):
        self.inv.remove(item)

    def map(self):
        clear()
        items = ["City_hall"]
        active = True
        for i in range(len(items)):
            print(f"[{i+1}] {items[i]}")

        user_input = ""
        while user_input != "-1":
            user_input = input("Map Console (\"i\" for more info ; -1 return)\n>>> ")
            
            if user_input == "i":
                print("City_hall: Location where you can help the citizens")
            elif user_input == "1":
                reward = npc.format_question()
                if reward == -1:
                    return -1
                else:
                    self.healing(2,reward)

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

            print("Active Quests (input corresponding numbers for more information (-1 return)):\n")

            print(f"{1} - {self.active_quests[0][0]}")


            print("\n\nCompleted quests:")

            for i in range(len(self.completed_quests)):
                print(f"{i+1}C - {self.completed_quests[i][0]}")


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

            elif len(user_check) == 2 and user_check[1].lower() == "c" and user_check[0].isnumeric() == True and int(user_check[0]) <= len(self.completed_quests) and int(user_check[0]) > 0:

                clear()
                ind = int(user_check[0]) - 1

                print(f"Name: {self.completed_quests[ind][0]}")
                print(f"Description: {self.completed_quests[ind][1]}")
                print(f"Reward: {self.completed_quests[ind][3]} Support")

                input("\n\n[Press <Enter> to continue")
                clear()

            elif user_input != -1 and extend == True and user_input == 1:
                clear()
                print(f"Name: {self.active_quests[0][0]}")
                print(f"Description: {self.active_quests[0][1]}")
                print(f"Reward: {self.active_quests[0][3]} Support")

                input("\n\n[Press <Enter> to continue]")
                clear()

            else:
                clear()

    def quest_complete(self):
        self.active_quests.append(self.available_quests[self.quest_num])
        self.completed_quests.append(self.active_quests[0])
        self.active_quests.pop(0)
        self.quest_num = self.active_quests
