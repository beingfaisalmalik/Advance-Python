l1 = [1,2,3,4]
print(l1)
l2 = [i for i in l1]
l1.append(1)
print(l1)
print(l2)


#extracting even numbers using list comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

#using only if
even = [number  for number in numbers if number%2==0 ]
print(even)

#using else and if 
even = [number if number%2==0  else 0 for number in numbers  ]
print(even)
