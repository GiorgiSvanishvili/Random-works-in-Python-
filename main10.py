import collections 
from collections import defaultdict
from collections import ChainMap
from types import MappingProxyType

#Dictionaries
phonebook = {
    'David': 5558989,
    'Bam': 896799,
    'George': 7898585,
}

squares = {x: x * x for x in range(10)}

print(squares, phonebook['George'])



#OrderedDict
d = collections.OrderedDict(one = 1, two = 2, three = 3)

d['four'] = 4

print(d)
print(d.keys())



#defaultdict accesing a missing kea and creates it.
dd = defaultdict(list)

dd['dogs'].append('Hary')
dd['dogs'].append('Bary')
dd['dogs'].append('Lary')
dd['dogs'].append('Cury')

print(dd['dogs'])


#ChainMap searches each collection in the chain.
Dict1 = {'one': 1, 'two': 2}
Dict2 = {'three': 3, 'four': 4}
Dict3 = {'five': 5, 'six': 6}

chain = ChainMap(Dict1, Dict2, Dict3)

print(chain['five'])

#MappingProxyType creates immutable proxy versions of dictionaries.
writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])

read_only['one'] = 45
print(read_only['one']) #SOS<- TypeError: 'mappingproxy' object does not support item assignment

