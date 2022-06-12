import math
import random


def gcd():
    output = dict.fromkeys(['game_condition', 'question', 'right_answer'])
    output['game_condition'] = 'Find the greatest common divisor '\
        'of given numbers.'

    number1 = random.randrange(100)
    number2 = random.randrange(100)
    question = f'{number1} {number2}'
    output['question'] = question

    right_answer = math.gcd(number1, number2)
    output['right_answer'] = str(right_answer)

    return output
