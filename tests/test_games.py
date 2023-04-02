import math

from brain_games.games import calc, even, gcd, prime, progression

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
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
        71, 73, 79, 83, 89, 97,
    ]
    for num in prime_numbers:
        assert prime.is_prime(num) is True

    not_prime_numbers = [
        0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27,
        28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51,
        52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75,
        76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96,
        98, 99, 100
    ]
    for num in not_prime_numbers:
        assert prime.is_prime(num) is False


def test_prime():
    output = prime.prime()
    question = output.get(QUESTION)
    right_answer = output.get(RIGHT_ANSWER)

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(question) is int
    assert type(right_answer) is str

    if prime.is_prime(question) is True:
        assert right_answer == 'yes'
    elif prime.is_prime(question) is False:
        assert right_answer == 'no'


def test_progression():
    output = progression.progression()
    question = output.get(QUESTION)
    right_answer = output.get(RIGHT_ANSWER)

    assert type(output) is dict
    assert type(output.get(DESCRIPTION)) is str
    assert type(question) is str
    assert type(right_answer) is str

    left, right = question.split('..')
    left = left.strip().split()
    right = right.strip().split()

    subarray = left if len(left) >= len(right) else right
    step = int(subarray[1]) - int(subarray[0])

    if subarray == left:
        answer = str(int(subarray[-1]) + step)
    else:
        answer = str(int(subarray[0]) - step)

    assert answer == right_answer
