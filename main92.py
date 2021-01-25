#Array data sturctures
import array

#List

arr = ['one', 'two', 'three',]

arr[1] = 99
del arr[2]
arr.append(2)

print(arr)

#str immutable arrays of unicode characters
st = 'abc1d' 
print(st)
print(st[1])
print(list('abcd'))
print(''.join(list('abcd')))

#bytes - Immutable arrays of single bytes(0-256)
#bytearray - mutable arrays of single bytes

by = bytes((0, 1, 2, 3))
print(bytes((0, 300))) #<- ValueError: bytes must be in range(0, 256)

print(by[1])





