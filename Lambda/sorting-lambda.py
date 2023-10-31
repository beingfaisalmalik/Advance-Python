a = [-1,1,-2,2,3,-3,4,-4,5,-5]
print(a)

sorted_numbers = sorted(a , key=lambda x:abs(x))
print(sorted_numbers)