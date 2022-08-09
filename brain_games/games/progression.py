import random

DESCRIPTION = 'What number is missing in the progression?'


def progression():
    output = dict.fromkeys(['game_condition', 'question', 'right_answer'])
    output['game_condition'] = DESCRIPTION

    progression_length = random.randrange(6, 11)
    first_value = random.randrange(0, 20)
    difference = random.randrange(1, 10)
    progression = [first_value]

    for v in range(progression_length):
        progression.append(progression[v] + difference)

    for index, item in enumerate(progression):
        progression[index] = str(item)

    index_of_hidden_value = random.randrange(0, progression_length)
    right_answer = progression[index_of_hidden_value]
    output['right_answer'] = str(right_answer)

    progression[index_of_hidden_value] = '..'
    question = ' '.join(progression)
    output['question'] = question

    return output
