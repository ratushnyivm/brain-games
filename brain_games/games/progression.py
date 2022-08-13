import random

DESCRIPTION = 'What number is missing in the progression?'

LENGTH_MIN = 6
LENGTH_MAX = 11

START_MIN = 0
START_MAX = 20

STEP_MIN = 1
STEP_MAX = 10

REPLACEMENT = '..'


def progression():
    output = {'description': DESCRIPTION}

    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    stop = start + length * step
    progression = [str(item) for item in range(start, stop, step)]

    hidden_value = random.choice(progression)
    output['right_answer'] = hidden_value

    question = ' '.join(
        item if item != hidden_value else REPLACEMENT for item in progression
    )
    output['question'] = question

    return output
