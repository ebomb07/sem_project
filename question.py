import random
import time
def question_getter():
    random.seed(time.time())
    questions = [
        ["1+2+3+4+5", "15"],
        ["2+3+4+5", "14"]
    ]
    return questions[random.randint(0,len(questions)-1)]

