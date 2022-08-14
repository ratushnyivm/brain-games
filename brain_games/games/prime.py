import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_MAX = 100


def is_prime(number):
    if number % 2 == 0 or number == 1:
        return number == 2

    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2

    return divisor * divisor > number


def prime():
    output = {'description': DESCRIPTION}

    question = random.randrange(NUMBER_MAX)
    output['question'] = question

    right_answer = 'yes' if is_prime(question) else 'no'
    output['right_answer'] = str(right_answer)

    return output
