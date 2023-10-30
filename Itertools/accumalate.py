from itertools import accumulate
import operator
fac = [1,2,3,4,5]
acc = accumulate(fac,func=operator.mul)
print(list(acc))


a = [1,2,3,4,5]

a = accumulate(a,operator.mul)
print(list(a))