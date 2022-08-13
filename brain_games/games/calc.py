import random

DESCRIPTION = 'What is the result of the expression?'
NUMBER_1_MAX = 30
NUMBER_2_MAX = 20


def calc():
    output = {'description': DESCRIPTION}

    number1 = random.randrange(NUMBER_1_MAX)
    number2 = random.randrange(NUMBER_2_MAX)

    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2

    operators_sign = {
        addition: '+',
        subtraction: '-',
        multiplication: '*'
    }
    operators = list(operators_sign.keys())

    right_answer = random.choice(operators)
    output['right_answer'] = str(right_answer)

    question = f'{number1} {operators_sign[right_answer]} {number2}'
    output['question'] = question

    return output
