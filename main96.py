#get() method

name_for_userid = {
    388: 'Bob',
    456: 'George',
    769: "Bam"
}

def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')

print(greeting(769))


#items() and sorted() method

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}

print(sorted(xs.items()))

print(sorted(xs.items(), key = lambda x: x[1]))

print(sorted(xs.items(), key=lambda x: x[1], reverse=True))

#operator.itemgetter

import operator
print(sorted(xs.items(), key = operator.itemgetter(1)))

#how to avoid if-else chains

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y

print(dispatch_if('mul', 7, 99))

#absolutely same with dictionary

def dispatch_dict(operator, x, y):
    return{
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

print(dispatch_dict('div', 693, 7))