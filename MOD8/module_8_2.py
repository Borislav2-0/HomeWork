"""Напишите 2 функции:

Функция personal_sum(numbers):
    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во некорректных данных.

Функция calculate_average(numbers)
    Среднее арифметическое - сумма всех данных делённая на их количество.
    Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и верните 0.
    Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.

Пункты задачи:
    Создайте функцию personal_sum на основе условий задачи.
    Создайте функцию calculate_average на основе условий задачи.
    Вызовите функцию calculate_average несколько раз, передав в неё данные разных вариаций."""

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
        num = []
        try:
            for i in numbers:
                if type(i) == int:
                    num.append(i)
            return sum_num[0] / len(num)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')