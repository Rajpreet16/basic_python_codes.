#class
class Car:
    def __init__(self, components):
        self.components = components

    @classmethod
    def carA(cls):
        return cls(['suzuki','duccatti'])

    @classmethod
    def carB(cls):
        return cls(['Maruti','Hyundai'])
#static method
import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients


    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

p = Pizza(4, ['mozzarella', 'tomatoes'])
print(p.area())
print(Pizza.circle_area(45))


#innerclass
class Human:

 def __init__(self):
    self.name = 'Rajpreet'
    self.head = self.Head()

 class Head:
    def talk(self):
        return 'talking......'

if __name__ == '__main__':
    guido = Human()
    print (guido.name)
    print (guido.head.talk())
