from brain_games.games import calc, even, gcd, prime
import math
import sympy

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


def test_even():
    output = even.even()
    question = output.get(QUESTION)
    right_answer = output.get(RIGHT_ANSWER)

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(question) is int
    assert type(right_answer) is str

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    assert answer == right_answer


def test_gcd():
    output = gcd.gcd()

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(output.get(QUESTION)) is str
    assert type(output.get(RIGHT_ANSWER)) is str

    question = output.get(QUESTION).split()
    right_answer = int(output.get(RIGHT_ANSWER))
    answer = math.gcd(int(question[0]), int(question[1]))

    assert answer == right_answer


def test_is_prime():
    for _ in range(4000):
        assert prime.is_prime(_) == sympy.isprime(_)


def test_prime():
    output = prime.prime()
    question = output.get(QUESTION)
    right_answer = output.get(RIGHT_ANSWER)

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(question) is int
    assert type(right_answer) is str

    answer = 'yes' if sympy.isprime(question) else 'no'
    assert answer == right_answer
