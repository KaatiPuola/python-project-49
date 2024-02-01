from random import randint
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    count = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            count += 1
    return count


def play_game():
    question = randint(2, 100)
    number = question
    right_answer = 'yes' if is_prime(number) <= 0 else 'no'
    return question, right_answer
