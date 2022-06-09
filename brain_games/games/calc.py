import prompt
import random
import operator


def calc():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What is the result of the expression?')

    for i in range(3):
        number1 = random.randrange(30)
        number2 = random.randrange(20)

        addition = operator.add(number1, number2)
        subtraction = operator.sub(number1, number2)
        multiplication = operator.mul(number1, number2)

        operators_sign = {
            addition: '+',
            subtraction: '-',
            multiplication: '*'
        }

        operators = list(operators_sign.keys())
        r = random.choice(operators)

        question = f'{number1} {operators_sign[r]} {number2}'
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if_correct = 'Correct!'

        if int(answer) == r:
            print(if_correct)

        else:
            return print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{r}'."
                f"\nLet's try again, {name}!"
            )

    return print(f"Congratulations, {name}!")
