#map function is for transforming the list items

numbers = [i for i in range(1,101)]
print(numbers)

a = list(map(lambda x : x if x%2==0 else 0,numbers))
print(a)