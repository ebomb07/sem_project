import random
import time
import question

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


        return (names[random.randint(0,len(names)-1)], dialogue[random.randint(0,len(dialogue)-1)], question.question_getter()) #0: Name ; 1: dialogue ; 2: question




    def z(dig_opt):
        dialogue = [
            "testing"
        ]

        if len(dialogue) - 1 < dig_opt:
            return -1
        else:
            return dialogue[dig_opt]
    
class player:

    def __init__(self,name = "<USER USERNAME NULL>", health=100, support=40, moral=75):
        self.name = name
        self.health = health
        self.support = support
        self.moral = moral

    def all_info(self):
        print(f"\nName: {self.name}")
        print(f"Health: {self.health}")
        print(f"Support: {self.support}")
        print(f"Moral: {self.moral}")




    def damage(self, type_of_dmg=-1, dmg=0):
        if type_of_dmg == -1:
            return -1

        elif type_of_dmg == 1: # Health damage
        
            self.health -= dmg
        
        elif type_of_dmg == 2: # Support damage
            
            self.support -= dmg
        
        elif type_of_dmg == 3: # Moral damage

            self.moral -= dmg


    def healing(self, type_of_healing=-1, heal=0):
        
        if type_of_healing == -1:
            return -1
        elif type_of_healing == 1: # Health healing 
            self.health += heal

        elif type_of_healing == 2: # Support healing 
            self.support += heal

        elif type_of_healing == 3: # Moral healing 
            self.moral += heal
