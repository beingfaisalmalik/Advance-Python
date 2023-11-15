

numbers = (1,2,3,4)

start , *end = numbers
print(start)
print(end)

*start , end = numbers
print(start)
print(end)

start, *middle , end = numbers

print(start)
print(middle)
print(end)