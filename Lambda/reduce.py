#reduce is for sum and for factorial

from functools import reduce
numbers = [1,2,3,4,5]
print(numbers)

fac = reduce(lambda x,y:x*y,numbers)
print(fac)