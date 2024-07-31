import math


def is_prime(func):
    def wrapper(a, b, c):
        res = func(a, b, c)
        if res > 1:
            for i in range(2, int(math.sqrt(res)) + 1):
                if res % i == 0:
                    print(f'The number {res} is a composite')
                    return res
            print(f'The number {res} is a prime')
            return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result


result = sum_three(8, 3, 6)
print(result)

result = sum_three(6, 9, 7)
print(result)

result = sum_three(1, 9, 615)
print(result)

result = sum_three(899, 6, 2)
print(result)
