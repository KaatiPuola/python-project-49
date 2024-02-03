from random import randint
import math
RULE = 'Find the greatest common divisor of given numbers.'


def generate_data():
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    question = f'{number1} {number2}'
    right_answer = math.gcd(number1, number2)
    return question, str(right_answer)
