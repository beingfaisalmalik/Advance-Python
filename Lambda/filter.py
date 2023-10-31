# Filter is used for selecting the elements 
numbers = [i for i in range(1,101)]
print(numbers)

print("List Of Even Numbers")
even_numbers = list(filter(lambda x: (x%2==0),numbers))
print(even_numbers)