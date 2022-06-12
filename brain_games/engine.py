import prompt


def engine(game_module, number_of_rounds=3):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    # Переменная, в которой будет своё условие для каждой игры.
    print(game_module()['game_condition'])

    for i in range(number_of_rounds):
        output_of_game_module = game_module()

        # Вопрос, на который игрок должен дать ответ.
        print(f"Question: {output_of_game_module['question']}")

        # Запрос ответа от игрока
        answer = prompt.string('Your answer: ')

        # Текст сообщения, если игрок ответил верно.
        if_right = 'Correct!'

        # Текст сообщения, если игрок ответил неверно.
        if_wrong = f"'{answer}' is wrong answer ;(."\
            f"Correct answer was '{output_of_game_module['right_answer']}'."\
            f"\nLet's try again, {name}!"

        # Сравниваем ответ пользователя с правильным ответом из модуля игры.
        if answer == output_of_game_module['right_answer']:
            # Если ответ верен, выводим сообщение и переходим дальше.
            print(if_right)

        else:
            # Вывод сообщения о неправильном ответе, Game Over
            return print(if_wrong)

    # Поздравление игрока с победой.
    return print(f"Congratulations, {name}!")
