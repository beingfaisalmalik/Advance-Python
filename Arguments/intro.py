#postional arguments

def sum(a,b,c,d,e,f):
    sums  = a+b+c+d+e+f
    return sums

print(sum(1,2,3,4,5,6))


#keyword arguments

def summ(a,b,c,d):
    return a+b+c+d

print(summ(a=1,b=2,c=3,d=4))


#no positional arguments allowed after the keyword arguments

#default arguments

def summm(a,b,c=4):
    return a+b+c

print(summm(1,2))