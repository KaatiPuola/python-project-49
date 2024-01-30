import prompt
ATTEMPTS = 3


def general():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULE)
    for _ in range(ATTEMPTS):
        question, right_answer = game()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congritulations, {name}!')
