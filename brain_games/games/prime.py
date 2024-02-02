from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


def play_game():
    question = randint(2, 100)
    number = question
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
