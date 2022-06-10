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
        right_answer = random.choice(operators)

        question = f'{number1} {operators_sign[right_answer]} {number2}'
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
