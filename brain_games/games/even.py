import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_MAX = 100


def even():
    output = {'description': DESCRIPTION}

    question = random.randrange(NUMBER_MAX)
    output['question'] = question

    right_answer = "yes" if question % 2 == 0 else "no"
    output['right_answer'] = right_answer

    return output
