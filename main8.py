#namedtuple

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')
class MyCarWithMethods(Car): 
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 5678)
c.hexcolor()

#_replace() and _asdict()