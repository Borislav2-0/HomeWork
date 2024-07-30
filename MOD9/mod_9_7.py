"""Цель задания:
    Освоить механизмы создания декораторов Python.
    Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
    Напишите 2 функции:
        Функция, которая складывает 3 числа (sum_three)
        Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.

Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11

Примечания:
    Не забудьте написать внутреннюю функцию wrapper в is_prime
    Функция is_prime должна возвращать wrapper
    @is_prime - декоратор для функции sum_three
"""


def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        if type(res) is int:
            print('A prime number')
        else:
            print('Composite number')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(2, 3, 6)
print(result)
