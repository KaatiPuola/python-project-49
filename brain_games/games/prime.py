from random import randint
import math
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def generate_data():
    question = randint(2, 100)
    number = question
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
