import prompt
import random


def even():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        question = random.randrange(100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if_correct = 'Correct!'

        if question % 2 == 0:
            if answer == 'yes':
                print(if_correct)

            else:
                return print(
                    f'"{answer}" is wrong answer ;(. Correct answer was "yes".'
                    f'\nLet\'s try again, {name}!'
                )

        else:
            if answer == 'no':
                print(if_correct)

            else:
                return print(
                    f'"{answer}" is wrong answer ;(. Correct answer was "no".'
                    f'\nLet\'s try again, "{name}"!'
                )

    return print(f"Congratulations, {name}!")
