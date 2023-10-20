t = tuple([i for i in range(0,100)])
print(t)

#even number of tuples
t = tuple(number for number in t if number%2==0)
print(t)