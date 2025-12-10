import random
import time
import scene
import os
import json

character_clearing = "clear"
clear = lambda:os.system(f"{character_clearing}")

''' 
    This file handles all of the npc and player functions including the questions, saving, etc
'''


class npc:

    '''
        This class "npc" handles the different interactions with the user

        This class hosts the questions from city hall and formats the questions that are asked
    '''

    def random_question():
        random.seed(time.time())
        
        names = [
            "Bill",
            "Mary",
            "James",
            "Sam",
            "Jane"
        ]

        dialogue = [
            "Can you please help us with this problem?",
            "HELP! HELP! HELP!"
        ]

        return (names[random.randint(0,len(names)-1)], dialogue[random.randint(0,len(dialogue)-1)], npc.question_getter())


    def question_getter(): #Question Format [<question>, <answer>, <reward>]
        random.seed(time.time())
        questions = [
            ["hvs_rcu_xiadsr_hvs_tsbqs", "the_dog_jumped_the_fence", 5],
            [".. ..--.- .-.. . ..-. - ..--.- - .... . ..--.- ... - --- ...- . ..--.- --- -.", "i_left_the_stove_on", 5],
            ["India Sierra _ Tango Hotel India Sierra _ Tango Hotel India November Golf _ Oscar November", "is_this_thing_on", 5],
            ["77 65 6C 6C 5F 79 6F 75 5F 66 6F 75 6E 64 5F 6D 65", "well_you_found_me",5],
            ["eW91X2RlY29kZWRfdGhpcz8=","you_decoded_this?",5],
            ["105 95 100 111 95 108 105 107 101 95 110 117 109 98 101 114 115", "i_do_like_numbers", 5],
            ["aaaab aaaaa aaaba abbab abbaa abaaa baaab ababb babba aabab aaaaa baabb abbab baaaa abaaa baaba aabaa\nHint: No underscores", "baconismyfavorite", 5]
        ]
        
        return questions[random.randint(0,len(questions)-1)]


    def format_question(types=0,pos=0):
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

        user_answer = input("\n>>> ").lower()
        
        if user_answer == answer and reward != -1:
            return reward

        elif user_answer != answer and reward != -1:
            return reward * -1
        
        

        if user_answer == answer and reward == -1:
            return 1
        elif user_answer != answer and reward == -1:
            return -1

        

    

    
class user:

    '''
        This class "user" handles everything the player does.

        It has an init function which can communicate with the save function to either upload from the file or not to.

        This class also has access to the different questions that desbyte will ask in your main quest.

        There is also a damage and healing functions in this class to either give or take away stats like health, money, support, etc.
        Along with that there is the shop, this is where you buy everything that you can use and it adds to your inventory. 

        At the end of this class there is the quest_complete function which automatically checks which quest you are on based on your last completed quest or your upload.  
    '''

    def __init__(self,name = "Aiden", health=100, support=0, moral=75, money=100, quest_num = 0, inventory=[], up = "n"):

        # This function initializes the player object

        self.active_quests = []
        self.call = None
        self.city_name = "Day_city"
        self.ending = None
        self.completed_quests = []
        self.clearing = "clear"
        self.available_quests = [ #Format: <NAME> <Description> <required support> <reward support> <next index>

                    ["Tutorial", 
                    "The tutorial teaches you the basics of the game and controls",
                    0,
                    5,
                    1],

                    ["First_mission",
                    "Help a Civilian with their task",
                    0,
                    20,
                    2],

                    ["Combat_desbyte",
                    "Complete the challenges recieved by the hacker group desbyte",
                    35,
                    20,
                    3],

                    ["Retrieve_the_codes",
                    "Find and retrieve the code to enter desbytes network",
                    65,
                    25,
                    4],

                    ["Final_mission",
                    "Shutdown desbytes network and report the the police",
                    100,
                    30,
                    5],
                    ["good_ending",
                    "Everyone in Day city is happy that you saved them",
                    0,
                    0,
                    -1],
                    ["bad_ending",
                    "City doesn't view you as a savior and turns more into darkness",
                    0,
                    0,
                    -2]

            ]

        if up == "n":
            # If the user doesn't want to upload this is the default values
            self.name = name
            self.health = health
            self.support = support
            self.moral = moral
            self.money = money
            self.quest_num = quest_num
            self.inv = inventory
            
            if self.quest_num == 0: 
                self.active_quests.append(self.available_quests[self.quest_num])
            else:
                self.active_quests.append(self.available_quests[self.quest_num - 1])
        elif up == "y":
            # If the user wants to upload the save(2) function will handle the later initialization
            self.save(2)
        
        else:
            # Makes the user pick Y/N
            print("Y/N")




    def save(self, mode=None):
        # Allows the user to save, upload and restore their save file
        if mode == None:
            return -1
        elif mode == 1: # Save to file
            with open("save.json","r") as file:
                info = json.load(file)

                info["name"] = self.name
                info["health"] = self.health
                info["support"] = self.support
                info["moral"] = self.moral
                info["money"] = self.money
                info["quest_num"] = self.quest_num
                info["inv"] = self.inv
                info["call"] = self.call
                info["city_name"] = self.city_name

            with open("save.json", "w") as fp:
                json.dump(info, fp)
        
        elif mode == 2: # Uploads from the save file
            with open("save.json","r") as file:
                info = json.load(file)

                self.name = info["name"]
                self.health = info["health"]
                self.support = info["support"]
                self.moral = info["moral"]
                self.money = info["money"]
                self.quest_num = int(info["quest_num"])
                self.inv = info["inv"]
                self.call = info["call"]
                self.city_name = info["city_name"]
                self.active_quests.append(self.available_quests[self.quest_num])
                self.quest_num = self.active_quests[0][-1]

                for i in range(self.active_quests[0][-1] - 1):
                    self.completed_quests.append(self.available_quests[i])


        elif mode == 3: # Restores the save file to default
            
            if input(f"Type CONFIRM_{self.name} to restore to default\n>>> ") == f"CONFIRM_{self.name}":
                print("OVERRIDING...")
                with open("save.json","w") as fp:
                    default = { 
                        "name": "Aiden",
                        "health": 100,
                        "support": 0,
                        "moral": 75,
                        "money": 100,
                        "quest_num": 0,
                        "inv": [],
                        "call": False,
                        "city_name": "Day_city"
                    }

                    json.dump(default,fp)
                    clear()
            else:
                return -1

    def __str__(self): # Allows you to print the player object
        return f"Name: {self.name}\nHealth: {self.health}\nSupport: {self.support}\nMoral: {self.moral}\nMoney: {self.money}\nInventory: {self.inv}"

    def damage(self, type_of_dmg=-1, dmg=0): # Damages your stats

        if type_of_dmg == -1:
            return -1

        elif type_of_dmg == 1: # Health damage
        
            self.health -= dmg

            if self.health <= 0:
                print("You have lost exiting game due to no health")
                exit()
        
        elif type_of_dmg == 2: # Support damage
            
            self.support -= dmg

            if self.health <= -25:
                print("You have lost exiting game due to no support being less than 25")
                exit()
        
        elif type_of_dmg == 3: # Moral damage

            self.moral -= dmg

            if self.moral <= 0:
                print("You have lost exiting game due to no moral")
                exit()

        elif type_of_dmg == 4: # money damage
            self.money -= dmg

    def healing(self, type_of_healing=-1, heal=0): # Adds to your stats
        
        if type_of_healing == -1:
            return -1
        elif type_of_healing == 1: # Health healing 

            if self.health + heal <= 100: # checks if health is over 100 if so it caps it at 100
                self.health += heal

            elif self.health == 100:
                return -1

            else:
                self.health = 100
                print(f"You have used your item to heal {100-heal} to reach 100 HP.")
                
            return 1

        elif type_of_healing == 2: # Support healing 
            self.support += heal


        elif type_of_healing == 3: # Moral healing 
            if self.moral + heal <= 100: # Caps the moral at 100
                self.moral += heal

            elif self.moral == 100:
                return -1

            else:
                self.moral = 100
                print(f"You have used your item to add {100-heal} moral to reach 100 moral.")

            return 1

        elif type_of_healing == 4: # Money healing
            self.money += heal

    def inventory_add(self,item): # Adds to your inventory
        self.inv.append(item)

    def inventory_remove(self,item): # Removes from your inventory
        self.inv.pop(item)


    def store(self): # Store where the user can buy items
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
        while active: # Allows an amount of buying up to the user (return: -1)
            clear()
            print(f"{'Shop items':-^20}")
            print(f"Your money: ${self.money}")

            for i in range(len(shop_items)): #prints all of the items
                print(f"\n[{i+1}] {shop_items[i][0]} - ${shop_items[i][1]}")
            
            print("\n(-1) Return")
            
            try:
                user_choice = int(input("\n>>> "))

                if user_choice <= 0: # checks the input to be more than 0
                    return 0
                
                if self.money - shop_items[user_choice-1][1] >= 0: # checks if the user can actually buy it

                    self.damage(4, shop_items[user_choice - 1][1])
                    self.inventory_add(shop_items[user_choice - 1])

                else: # If the user can't buy it
                    clear()
                    print("Not enough money")
                    time.sleep(1.5)
                    clear()

            except ValueError: # catches errors if the user doesn't put in a number
                print("please input a valid number")
                time.sleep(1.5)
                clear()

    def use_item(self,item_id): #using the items the user buys
            if item_id > len(self.inv) or item_id < 0: # makes sure the user picks a valid number
                return -1
            else:
                match self.inv[item_id][-1]: # matches the item_id to the correct functionality
                    case 0:
                        self.healing(2, 5)
                        self.inventory_remove(item_id)
                    case 1:

                        check = self.healing(1,5)
                        if check == 1:
                            self.inventory_remove(item_id)

                    case 2: 

                        check = self.healing(1,15)
                        if check == 1:
                            self.inventory_remove(item_id)

                    case 3:
                        check = self.healing(3,10)
                        if check == 1:
                            self.inventory_remove(item_id)
                



    def map(self): # Prints a map for the user
        clear()

        items = ["City_hall"]
        active = True
        for i in range(len(items)):
            print(f"[{i+1}] {items[i]}")

        user_input = ""
        while user_input != "-1":
            user_input = input("Map Console (\"i\" for more info ; -1 return)\n>>> ")
            clear()

            if user_input == "i": # Map information tab
                print("City_hall: Location where you can help the citizens")

            elif user_input == "1": # NPC question
                reward = npc.format_question()

                if reward < 0: # if it is wrong
                    rand_moral = random.randint(5,10)
                    reward *= -1
                    self.damage(2,reward) #damage to support
                    self.damage(3,rand_moral) # damage to moral
                    self.damage(1,5) # damage to health

                    print(f"Wrong you lost {reward} support and 5 health and {rand_moral} moral")
                    time.sleep(2)
                    clear()
                else:
                    rand_moral = random.randint(1,10)
                    rand_money = random.randint(10,25)
                    self.healing(2,reward) # health the support
                    self.healing(3,rand_moral) # health to moral
                    self.healing(4, rand_money) # health to money
                    print(f"Correct! you gained {reward} support and {rand_money} dollars and {rand_moral} moral")
                    time.sleep(2)
                    clear()

    def information(self): # Information tab
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


    def quest(self): # Quest tab
        active = True

        '''
            This function prints the quests that are active and have been completed. It also displays the quest that the user wants to see. As well as start active quests.
        '''

        while active:

            print("Active Quests (input corresponding numbers for more information (-1 return)):\n")

            print(f"{1} - {self.active_quests[0][0]}")


            print("\n\nCompleted quests:")

            for i in range(len(self.completed_quests)):
                print(f"{i+1}C - {self.completed_quests[i][0]}")


            user_input = input("\n\n>>> ")
        

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

            elif len(user_check) == 2 and user_check[1].lower() == "c" and user_check[0].isnumeric() == True and int(user_check[0]) <= len(self.completed_quests) and int(user_check[0]) > 0: # Shows the details of the completed quest the user chose

                clear()
                ind = int(user_check[0]) - 1

                print(f"Name: {self.completed_quests[ind][0]}") 
                print(f"Description: {self.completed_quests[ind][1]}")
                print(f"Reward: {self.completed_quests[ind][3]} Support")

                input("\n\n[Press <Enter> to continue")
                clear()

            elif user_input != -1 and extend == True and user_input == 1: # Shows details of the active quest that the user chose
                clear()
                required_support = self.active_quests[0][2]
                print(f"Name: {self.active_quests[0][0]}")
                print(f"Description: {self.active_quests[0][1]}")
                print(f"Required support: {required_support}")
                print(f"Your support: {self.support}")
                print(f"Reward: {self.active_quests[0][3]} Support")

                check = input("\n\nDo you want to start the quest? (Y/N)\n[Press <Enter> to continue]\n>>> ").lower()
                
                if check == "y" and self.support >= required_support: # This chooses which scene that the user is currently having active
                    match self.active_quests[0][4] - 1: # Doesn't start at 0 because they complete it before having access
                        case 1:
                            scene.first_mission(self)
                        case 2:
                            scene.combat_desbyte(self)
                        case 3:
                            scene.retrieve_the_codes(self)
                        case 4:
                            scene.Final_mission(self)
                        case -2:
                            scene.good_ending(self)
                        case -3:
                            scene.bad_ending(self)
                elif check == "n": # Goes back if the user doesn't want to start the quest
                    clear()
                else: # if their support is not high enough they will be presented with this message
                    clear()
                    print("Please go to the city hall via the map to earn support")
                    time.sleep(2)
                    clear()
                clear()
            else:
                clear()
                


    def desbyte_question_handler(self,pos,player): # Formats and handles the desbyte questions (main quest)
        
        desbyte_names = [
            "desbyte_Cameron",
            "desbyte_David",
            "desbyte_Ethan",
            "desbyte_Somil",
            "desbyte_Jub"
        ]

        desbyte_question = [
            ["What is the md5 hash for \"desbyte\"", "26daafa43fc380ea0b30f0cbb6d51815",-1],
            ["What hash is this \"0CB6948805F797BF2A82807973B89537\"","ntlm",-1],
            ["When was the RSA encryption published", "1977",-1],
            ["What is the SHA1 hash for \"day_city\"", "6a879991b1e365842924007ba5d2f9e96b6f631b",-1]
        ]

        desbyte_dialogue = [
            "NoOOOOoOoOOOOooo HOW DID YOU SOLVE IT!",
            "THIS IS IMPOSSIBLE!",
            "HOW CAN THIS BE!",
            "what is real anymore..."

        ]


        name = desbyte_names[random.randint(0,len(desbyte_names) - 1)]
        question = desbyte_question[pos][0]
        answer = desbyte_question[pos][1]
        active = True

        if pos == 0: #checks if the user's pos is 0. We do this because there is scaleable damage depending on the quest you are on, and 0 * any_number = 0
            pos += 1
            
        while active: # Continues to run until the user gets the right answer
            clear()
            print(f"Your HP: {self.health}")
            
            print(f"{name}: You wont be able to solve this")
            print(f"{question}")

            user_answer = input(">>> ").lower()

            

            if user_answer == answer: # checks if the answer is right
                print(f"\n\n{name}: {desbyte_dialogue[random.randint(0,len(desbyte_dialogue) - 1)]}")
                time.sleep(1.5)
                clear()
                active = False
                return 0

            
            else: # If they are wrong then they lose 5 HP
                print(f"\nWrong you lost {5*pos} HP")
                self.damage(1,5*pos)
                time.sleep(1.5)
                clear()

    def quest_complete(self): #Handles the quests being completed and setting up for the next one
        self.healing(2,self.active_quests[0][3])

        if self.quest_num == 0:
            self.quest_num += 1

        self.active_quests.append(self.available_quests[self.quest_num])
        self.completed_quests.append(self.active_quests[0])
        self.active_quests.pop(0)
        self.quest_num = self.active_quests[0][4]

        if self.quest_num < 0 and self.call == True: # Handles the good or bad ending showing in the quest menu
            self.active_quests.pop(0)
            self.active_quests.append(self.available_quests[-2])
        elif self.quest_num < 0 and self.call == False:
            self.active_quests.pop(0)
            self.active_quests.append(self.available_quests[-1])

        
