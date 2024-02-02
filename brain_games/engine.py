import prompt
ROUNDS_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(ROUNDS_COUNT):
        question, right_answer = game.play_game()
        print(f"Question: {question}")
        answer = prompt.string('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
