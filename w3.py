from functools import reduce
l = [1, 2, 3, 4, 5]
l4 = reduce(lambda a,b: a+b, l)
print(l4)
