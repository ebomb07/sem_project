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
            ["hvs_rcu_xiadsr_hvs_tsbqs", "the_dog_jumped_the_fence", 1],
            [".. ..--.- .-.. . ..-. - ..--.- - .... . ..--.- ... - --- ...- . ..--.- --- -.", "i_left_the_stove_on", 1],
            ["India Sierra _ Tango Hotel India Sierra _ Tango Hotel India November Golf _ Oscar November", "is_this_thing_on", 1],
            ["77 65 6C 6C 5F 79 6F 75 5F 66 6F 75 6E 64 5F 6D 65", "well_you_found_me"],
            ["eW91X2RlY29kZWRfdGhpcz8=","you_decoded_this?",1],
            ["105 95 100 111 95 108 105 107 101 95 110 117 109 98 101 114 115", "i_do_like_numbers", 1],
            ["aaaab aaaaa aaaba abbab abbaa abaaa baaab ababb babba aabab aaaaa baabb abbab baaaa abaaa baaba aabaa", "bacon_is_my_favorite", 1]
        ]

        desbyte_question = [
            ["What is the md5 hash for: (desbyte)", "26daafa43fc380ea0b30f0cbb6d51815"],
            ["When was the RSA encryption published", "1977"],
            ["What hash is this\n0CB6948805F797BF2A82807973B89537","ntlm"],
            ["What is the SHA1 hash for: (day_city)", "6a879991b1e365842924007ba5d2f9e96b6f631b"]
        ]

        
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
                    5],
                    ["good_ending",
                    "Everyone in Day city is happy that you saved them",
                    130,
                    0,
                    -1],
                    ["bad_ending",
                    "City dosn't view you as a savior and turns more into darkness",
                    99,
                    0,
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
            return 1

        elif type_of_healing == 2: # Support healing 
            self.support += heal


        elif type_of_healing == 3: # Moral healing 
            if self.moral + heal <= 100:
                self.moral += heal
            else:
                self.moral = 100
                print("You have reached the maximum of 100 moral")
            return 1

        elif type_of_healing == 4: # Money healing
            self.money += money

    def inventory_add(self,item):
        self.inv.append(item)

    def inventory_remove(self,item):
        self.inv.pop(item)


    def store(self):
        clear()
        print("Z: Welcome to my shop\nZ: What would you like to buy")
        active = True
        shop_items = [ #<name>, <price>, <ID>
            ["support boost (+5)", 50, 0],
            ["Healing potion (+5)", 25, 1],
            ["Healing potion (+15)", 80, 2],
            ["Moral boost (+10)",100, 3]
        ]

        time.sleep(1.5)
        clear()
        while active:
            clear()
            print(f"{'Shop items':-^20}")
            print(f"Your money: ${self.money}")
            for i in range(len(shop_items)):
                print(f"\n[{i+1}] {shop_items[i][0]} - ${shop_items[i][1]}")
            
            print("\n(-1) Return")
            
            try:
                user_choice = int(input("\n---> "))

                if user_choice <= 0:
                    return 0
                
                if self.money - shop_items[user_choice-1][1] >= 0:

                    self.damage(4, shop_items[user_choice - 1][1])
                    self.inventory_add(shop_items[user_choice - 1])

                else:
                    clear()
                    print("Not enough money")
                    time.sleep(1.5)
                    clear()

            except ValueError:
                print("please input a valid number")
                time.sleep(1.5)
                clear()

    def use_item(self,item_id):
            if item_id > len(self.inv) or item_id < 0:
                return -1
            else:
                match self.inv[item_id][-1]: # ADD A REMOVE FEATURE
                    case 0:
                        self.healing(2, 5)
                        self.inventory_remove(item_id)
                    case 1:

                        check = self.healing(1,5)
                        if check != 1:
                            self.inventory_remove(item_id)

                    case 2: 

                        check = self.healing(1,15)
                        if check != 1:
                            self.inventory_remove(item_id)

                    case 3:
                        check = self.healing(3,10)
                        if check != 1:
                            self.inventory_remove(item_id)
                



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
        clear()
        print(f"{'Inventory':-^19}")
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Support : {self.support}")
        print(f"Moral: {self.moral}")
        print(f"Money: {self.money}")
        print(f"Inventory:[")
        for i in range(len(self.inv)):
            print(f"\t[{i}] {self.inv[i][0]}")
        print("]\n\n")


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
