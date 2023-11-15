def g(num):
    n=0
    while num > n:
        yield n
        n +=1
    
a = g(10)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
