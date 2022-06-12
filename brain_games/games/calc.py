import random
import operator


def calc():
    output = dict.fromkeys(['game_condition', 'question', 'right_answer'])
    output['game_condition'] = 'What is the result of the expression?'

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
    output['right_answer'] = str(right_answer)

    question = f'{number1} {operators_sign[right_answer]} {number2}'
    output['question'] = question

    return output
