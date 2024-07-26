def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError:
            incorrect_data = incorrect_data + 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        sum_num = personal_sum(numbers)
        c_num = []
        try:
            for i in numbers:
                if type(i) == int:
                    c_num.append(i)
            return sum_num[0] / len(c_num)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')


option1 = "1, 2, 3"
option2 = [1, 'Cтрока', 3, 'Еще строка']
option3 = 567
option4 = [42, 15, 36, 13]

print(f'Результат 1: {calculate_average(option1)}')
print(f'Результат 2: {calculate_average(option2)}')
print(f'Результат 3: {calculate_average(option3)}')
print(f'Результат 4: {calculate_average(option4)}')
