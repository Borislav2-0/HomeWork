class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start: int, stop: int, step: int = 1):
        self.start, self.stop, self.step = start, stop, step
        self.pointer = 0
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1)
for i in iter5:
    print(i, end=' ')
print()
