#OOP
#instance and class variables 


#Here I will show key difference between instance and class variables
class Dog:
    num_legs = 4 # <- Class variable

    def __init__(self, name):
        self.name = name # <- Instance variable


jack = Dog('Jack')
sonya = Dog('Sonya')
ted = Dog('Ted')
jack.num_legs = 2

print(jack.name, sonya.name, ted.name)
print(jack.num_legs, sonya.num_legs, ted.num_legs)
print(Dog.num_legs)
print(Dog.name) # <- AttributeError: type object 'Dog' has no attribute 'name


#Here I will show how instance variable can shaddow class variable
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances+=1


print(CountedObject.num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)

class CountedBuggyObject:
    num_instances = 0

    def __init__(self):
        self.num_instances+=1
        

print(CountedBuggyObject.num_instances)
print(CountedBuggyObject().num_instances)
print(CountedBuggyObject().num_instances)
print(CountedBuggyObject().num_instances)
print(CountedBuggyObject.num_instances)


    