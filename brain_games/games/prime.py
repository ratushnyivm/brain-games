import random


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def prime():
    output = dict.fromkeys(['game_condition', 'question', 'right_answer'])
    output['game_condition'] = 'Answer "yes" if given number is prime. '\
        'Otherwise answer "no".'

    question = random.randrange(100)
    output['question'] = question

    right_answer = 'yes' if isPrime(question) else 'no'
    output['right_answer'] = str(right_answer)

    return output
