from brain_games.games import calc

DESCRIPTION = 'description'
QUESTION = 'question'
RIGHT_ANSWER = 'right_answer'


def test_calc():
    output = calc.calc()

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(output.get(QUESTION)) is str
    assert type(output.get(RIGHT_ANSWER)) is str

    question = output.get(QUESTION).split()
    right_answer = int(output.get(RIGHT_ANSWER))

    if question[1] == '+':
        answer = int(question[0]) + int(question[2])
    if question[1] == '-':
        answer = int(question[0]) - int(question[2])
    if question[1] == '*':
        answer = int(question[0]) * int(question[2])

    assert answer == right_answer
