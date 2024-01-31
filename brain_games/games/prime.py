from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    question = randint(2, 100)
    count = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            count = count + 1
    right_answer = 'yes' if count <= 0 else 'no'
    return question, right_answer
