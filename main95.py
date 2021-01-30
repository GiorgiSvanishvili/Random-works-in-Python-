my_list = ['a', 'b', 'c', 'd']

#How you can write in Java
i = 0 
while i < len(my_list):
    print(my_list[i])
    i += 1

#Totally same in Python
for item in my_list:
    print(item)


#enumerate
for i, item in enumerate(my_list):
    print(f'{i}: {item}')


emails = {
    'George': 'George@example.com',
    'Nick': 'Nick@example.com',
    'Mary': 'Mary@examle.com'
}
for name, email in emails.items():
    print(f'{name}: {email}')


#list comprehension
squares = [x * x for x in range(10)]
print(squares)

even_squares = [x * x for x in range(10)
                if x % 2 == 0]
print(even_squares)


#set comprehension
{x * x for x in range(-9, 10)}
{64, 1, 0, 36, 4, 9, 16, 81, 49, 25} #<--more random order than lists


#dictionary comprehension
{x: x * x for x in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#list slicing
lst = [1, 2, 3, 4, 5]
print(lst)
print(lst[1:3:1]) #lst[start:end:step]
print(lst[1:3])
print(lst[::2]) #every other
print(lst[::-1]) #reverse copy of original list

class Repeater:
    def __init__(self, value):
        self.value = value
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        self.source = source
    def __next__(self):
        return self.source.value

repeater = Repeater('Hello')
iterator = iter(repeater)

#manually iterating. Every time you call next() the iterator is greeting
print(next(iterator))
print(next(iterator))

#Using StopIteration exception
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count +=1
        return self.value

repeater = BoundedRepeater('Hello Giorgi', 3)
for item in repeater:
    print(item)


#Generators
#With generators it is much more easier to iterate. It costs you less lines of code.
def repeater(value):
    while True:
        yield value

iterator = repeater('Hi')
print(next(iterator))
print(next(iterator))


def repeat_three_times(value):
    yield value
    yield value
    yield value

for x in repeat_three_times('Hey'):
    print(x)


def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count +=1
        yield value

for x in bounded_repeater('Good Morning', 2):
    print(x)











