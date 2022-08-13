from colorama import init, Fore
import prompt


def engine(game_module, number_of_rounds=3):
    init(autoreset=True)

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(game_module()['description'])

    for i in range(number_of_rounds):
        output_of_game_module = game_module()

        print(f"Question: {output_of_game_module['question']}")
        answer = prompt.string('Your answer: ')

        if_right = "Correct!"
        if_wrong = f"'{answer}' is wrong answer ;(. "\
            f"Correct answer was '{output_of_game_module['right_answer']}'."

        if answer.strip().lower() == output_of_game_module['right_answer']:
            print(Fore.LIGHTGREEN_EX + if_right)
        else:
            print(Fore.LIGHTRED_EX + if_wrong)
            return print(f"Let's try again, {name}!")

    return print(f"Congratulations, {name}!")
