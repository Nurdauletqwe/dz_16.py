'''1'''

# class Device:
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power


# class CoffeeMachine(Device):
#     def __init__(self, name, power, year):
#         super().__init__(name, power)
#         self.year = year

#     def info(self):
#         print(f'{self.name} делает кофе')


# class Blender(Device):
#     def __init__(self, name, power, color):
#         super().__init__(name, power)
#         self.color = color

#     def info(self):
#         print(f'{self.name} делает коктейли')


# class MeatGrinder(Device):
#     def __init__(self, name, power, weight):
#         super().__init__(name, power)
#         self.weight = weight

#     def info(self):
#         print(f'{self.name} делает котлеты')


# device = Device('Устройство', 100)
# coffeemachine = CoffeeMachine('Кофемашина', 200, 2020)
# blender = Blender('Блендер', 300, 'Красный')
# meatgrinder = MeatGrinder('Мясорубка', 400, 5)
# coffeemachine.info()
# blender.info()
# meatgrinder.info()

'''2'''

# class Ship:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year

#     def info(self):
#         print(f'{self.name} был построен в {self.year} году')


# class Frigate(Ship):
#     def __init__(self, name, year, guns):
#         super().__init__(name, year)
#         self.guns = guns

#     def info(self):
#         print(f'{self.name} был построен в {self.year} году и имеет {self.guns} пушек')


# class Destroyer(Ship):
#     def __init__(self, name, year, rockets):
#         super().__init__(name, year)
#         self.rockets = rockets

#     def info(self):
#         print(f'{self.name} был построен в {self.year} году и имеет {self.rockets} ракет')\


# class Cruiser(Ship):
#     def __init__(self, name, year, torpedoes):
#         super().__init__(name, year)
#         self.torpedoes = torpedoes

#     def info(self):
#         print(
#             f'{self.name} был построен в {self.year} году и имеет {self.torpedoes} торпед')


# ship = Ship('Корабль', 2000)
# frigate = Frigate('Фрегат', 2005, 10)
# destroyer = Destroyer('Эсминец', 2010, 20)
# cruiser = Cruiser('Крейсер', 2015, 30)
# ship.info()
# frigate.info()
# destroyer.info()
# cruiser.info()


'''3'''

# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def area(self):
#         return self.side_length ** 2


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2


# class CircleSquare(Square, Circle):
#     def __init__(self, side_length):
#         super().__init__(side_length)
#         self.radius = side_length / 2

#     def area(self):
#         return super().area()


# square_side_length = 4
# circle_square = CircleSquare(square_side_length)
# print(square_side_length, circle_square.area())

'''4'''


# class Car:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year


# class Wheel(Car):
#     def __init__(self, name, year, radius):
#         super().__init__(name, year)
#         self.radius = radius

#     def info(self):
#         print(
#             f'{self.name} был выпущен в {self.year} году и имеет радиус колес {self.radius} см')


# class Engine(Car):
#     def __init__(self, name, year, power):
#         super().__init__(name, year)
#         self.power = power

#     def info(self):
#         print(
#             f'{self.name} был выпущен в {self.year} году и имеет мощность двигателя {self.power} л.с.')


# class Door(Car):
#     def __init__(self, name, year, quantity):
#         super().__init__(name, year)
#         self.quantity = quantity

#     def info(self):
#         print(
#             f'{self.name} был выпущен в {self.year} году и имеет {self.quantity} дверей')


# car = Car('Машина', 2000)
# wheel = Wheel('Колесо', 2005, 50)
# engine = Engine('Двигатель', 2010, 200)
# door = Door('Дверь', 2015, 4)
# wheel.info()
# engine.info()
# door.info()
