import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER_1_MAX = 100
NUMBER_2_MAX = 100


def gcd():
    output = {'description': DESCRIPTION}

    number1 = random.randrange(NUMBER_1_MAX)
    number2 = random.randrange(NUMBER_2_MAX)

    question = f'{number1} {number2}'
    output['question'] = question

    right_answer = math.gcd(number1, number2)
    output['right_answer'] = str(right_answer)

    return output
