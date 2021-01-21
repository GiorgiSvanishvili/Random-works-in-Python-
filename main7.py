#Cloning objects
#Shallow and deep copy

#Shallow copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)

xs[1][1] = 'X'
print(xs)
print(ys)


#Deep Copy
import copy 

ds = [[6, 5, 4], [3, 2, 1], [9, 8, 7]]
zs = copy.deepcopy(ds)

ds[1][2] = 'XX'
print(ds)
print(zs)