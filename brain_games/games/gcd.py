import math
import prompt
import random


def gcd():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Find the greatest common divisor of given numbers.')

    for i in range(3):
        number1 = random.randrange(100)
        number2 = random.randrange(100)

        right_answer = math.gcd(number1, number2)
        print(right_answer)

        question = f'{number1} {number2}'
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if_correct = 'Correct!'

        if answer == str(right_answer):
            print(if_correct)

        else:
            return print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{right_answer}'."
                f"\nLet's try again, {name}!"
            )

    return print(f"Congratulations, {name}!")
