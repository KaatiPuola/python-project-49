from random import randint
RULE = 'What number is missing in the progression?'


def play_game():
    start, step = randint(1, 100), randint(2, 5)
    length = randint(5, 10)
    progression = list(range(start, start + step * length, step))
    random_index = randint(0, len(progression) - 1)
    right_answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(str(item) for item in progression)
    return question, str(right_answer)
