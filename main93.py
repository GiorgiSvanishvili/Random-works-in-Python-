#data structures(set)

#Sets are mutable and allows dynamic insertions.
#frozensets are immutable version of set 


vowels = {'a', 'e', 'i', 'o', 'u' }

print('e' in vowels)

letters = set('Alice dance and Jack snores')

print(letters.intersection(vowels))


vowels.add('J')

print(vowels)

print(len(vowels))

#The Collections.Counter class implements a multiset.
#Allows elements in the set to have more than one occurrence

from collections import Counter

inventory = Counter()

loot = {'sword': 2, 'bread': 3}
inventory.update(loot)

print(inventory)

second_loot = {'wood': 4, 'sword': 5}
inventory.update(second_loot)

print(inventory)
print(len(inventory)) # <-Callin len() returns unique elements in the multiset
print(sum(inventory.values())) # <- Total number of elements