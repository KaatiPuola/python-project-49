from random import randint
RULE = 'What number is missing in the progression?'


def play_game():
    start, step = randint(1, 100), randint(2, 5)
    length = randint(5, 10)
    prog_list = list(range(start, start + step * length, step))
    random_index = randint(0, len(prog_list) - 1)
    right_answer = prog_list[random_index]
    prog_list[random_index] = '..'
    question = ' '.join(str(item) for item in prog_list)
    return question, str(right_answer)
