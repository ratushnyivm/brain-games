import prompt
import random


def progression():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('What number is missing in the progression?')

    for i in range(3):
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

        progression[index_of_hidden_value] = '..'

        question = ' '.join(progression)

        print(f'Question: {question}')

        answer = prompt.string('Your answer: ')

        if_correct = 'Correct!'

        if answer == str(right_answer):
            print(if_correct)

        else:
            return print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{right_answer}'."
                f"\nLet's try again, {name}!"
            )

    return print(f"Congratulations, {name}!")
