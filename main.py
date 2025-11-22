import os
from character import npc, player


clear = lambda:os.system('clear')
clear()

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

def main():
    user = player()
    format_help(npc.random())
    user.all_info()
    



if __name__ == "__main__":
    main()
