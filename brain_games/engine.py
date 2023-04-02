import prompt
from colorama import Fore, init

NUMBER_OF_ROUNDS = 3


def engine(game_module, number_of_rounds=NUMBER_OF_ROUNDS):
    init(autoreset=True)

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_module()['description'])

    for _ in range(number_of_rounds):
        output_of_game_module = game_module()

        print(f"Question: {output_of_game_module['question']}")
        answer = prompt.string('Your answer: ')

        right = "Correct!"
        wrong = f'"{answer}" is wrong answer ;(. '\
            f'Correct answer was "{output_of_game_module["right_answer"]}".'

        if answer.strip().lower() == output_of_game_module['right_answer']:
            print(Fore.LIGHTGREEN_EX + right)
        else:
            print(Fore.LIGHTRED_EX + wrong)
            return print(f"Let's try again, {name}!")

    return print(f"Congratulations, {name}!")
