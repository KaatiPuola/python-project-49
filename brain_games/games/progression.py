import random
from random import randint
RULE = 'What number is missing in the progression?'


def game():
    step_progression = randint(2, 5)
    list1 = list(range(1, 100, step_progression))
    length = randint(5, 10)
    idx = randint(0, len(list1) - length)
    list2 = list1[idx:idx + length]
    right_answer = random.choice(list2)
    for index, value in enumerate(list2):
        if value == right_answer:
            list2[index] = '..'
    question = ' '.join(str(item) for item in list2)
    return question, str(right_answer)
