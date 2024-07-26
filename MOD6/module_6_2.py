class Vehicle:
    __COLOR_VARIANTS = ['blue', 'green', 'grey', 'white', 'black', 'red', 'yellow', 'pink', 'khaki', 'olive']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        print(f'Model: {self.__model}')

    def get_horsepower(self):
        print(f'Engine power: {self.__engine_power}')

    def get_color(self):
        print(f'Color: {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Owner: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'You can`t change the color to {self.new_color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Violet')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasiliy'

vehicle1.print_info()
