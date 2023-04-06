import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    l_boundary = 1
    u_boundary = 101

    while True:
        count += 1
        predict_number = np.random.randint(l_boundary, u_boundary)

        #after each iteration either lower or upper boundaries for predict_number
        #will be updated
        if predict_number < number:
            l_boundary = predict_number
        elif predict_number > number:
            u_boundary = predict_number
        else:
            break

    # Ваш код заканчивается здесь

    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
