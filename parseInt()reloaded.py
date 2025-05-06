import re


def parse_int(string):
    newString = re.split(r"[ -]", string)
    print(newString)
    current = 0
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100,
        "thousand": 1000,
        "million": 1000000,
    }
    total = 0
    for i in newString:
        if i in numbers:
            num = numbers[i]
            if num == 100:  # Обрабатываем "hundred"
                current *= num
            elif num == 1000 or num == 1000000:  # Обрабатываем "thousand" или "million"
                total += current * num
                current = 0  # Сбрасываем временную переменную
            else:
                current += num  # Просто добавляем число в текущее значение

    total += current  # Добавляем оставшееся число

    return total
