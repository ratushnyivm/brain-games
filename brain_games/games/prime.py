import prompt
import random
import sympy


def prime():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(3):
        question = random.randrange(100)

        right_answer = 'yes' if sympy.isprime(question) else 'no'

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if_correct = 'Correct!'

        if answer == right_answer:
            print(if_correct)

        else:
            return print(
                f'"{answer}" is wrong answer ;(.'
                f'Correct answer was "{right_answer}".'
                f'\nLet\'s try again, {name}!'
            )

    return print(f"Congratulations, {name}!")
