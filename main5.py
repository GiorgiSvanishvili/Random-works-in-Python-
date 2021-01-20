#string conversion
class Car:
    def __init__(self, color, kilometrage):
        self.color = color
        self.kilometrage = kilometrage

    def __str__(self):
        return f'a {self.color} car with {self.kilometrage} kms'

my_car = Car('red', 56700)
print(my_car)

#difference between str and repr
import datetime
today = datetime.date.today()

str(today)
repr(today)
