from itertools import product

prod = product([1, 2], [3, 4])
print(list(prod))

prod = product([1, 2], [3, 4] , repeat=2)
print(list(prod))