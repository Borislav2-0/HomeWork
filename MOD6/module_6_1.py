# Создайте:
# 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
#
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
#
# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(food) - метод, где food - это параметр, принимающий объекты классов растений.
#
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>",
# меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>",
# меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
#
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#
# Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
#
# Пункты задачи:
# 1) Создайте классы Animal и Plant с соответствующими атрибутами и методами
# 2) Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# 3) Создайте объекты этих классов.

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # живой
        self.fed = False  # накормленный

    def eat(self, food):
        if not food.edibility:
            self.alive = False
            print(f'{self.name} didn`t eat the {food.name}')
        else:
            self.fed = True
            print(f'{self.name} ate {food.name}')


class Herbivore(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edibility = False  # съедобность

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    alive = False


class Fruit(Plant):
    edibility = True


a1 = Predator('The Wolf of Wall Street')
a2 = Herbivore('Cow')
p1 = Flower('Seven-colored flower')
p2 = Fruit('A clockwork orange')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
