from itertools import accumulate
import operator
fac = [1,2,3,4,5]
acc = accumulate(fac,func=operator.mul)
print(list(acc))


