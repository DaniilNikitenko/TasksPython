def is_interesting(number, awesome_phrases):
    if number < 99:
        return 0
    elif is_round_number(number):
        return 2

    elif same_number(number):
        return 2

    elif is_sequential(number):
        return 2


def is_round_number(n):
    n_str = str(n)
    return n_str[0] != "0" and all(c == "0" for c in n_str[1:])


def same_number(n):
    n_str = str(n)
    return str(n) == n_str[::-1]


def is_sequential(n):
    digits = [int(d) for d in str(n)]
    if len(digits) < 2:
        return False

    # Определяем шаг между цифрами
    step = digits[1] - digits[0]

    # Проверяем, одинаков ли шаг между всеми соседними цифрами
    for i in range(1, len(digits)):
        if digits[i] - digits[i - 1] != step:
            return False

    return abs(step) == 1  # Только шаг ±1 считается "последовательным"

    digits = [int(d) for d in str(n)]
    if len(digits) < 2:
        return False

    # Определяем шаг между цифрами
    step = digits[0] - digits[1]

    # Проверяем, одинаков ли шаг между всеми соседними цифрами
    for i in range(1, len(digits)):
        if digits[i - 1] - digits[i] != step:
            return False

    return abs(step) == 1  # Только шаг ±1 считается "последовательным"


print(is_interesting(7890, []))
