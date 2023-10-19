l1 = [1,2,3,4]

#iterate using if else
print('using if loop')
if 1 in l1:
    print('yes')
else:
    print('no')

print('using range with loop') 
#iterate using range function
for i in range(len(l1)):
    print(l1[i])

print('using for loop')
#iterate using for loop
for item in l1:
    print(item)
    
    
start =0
end = len(l1)-1

print('using while loop')
while(start<=end):
    print(l1[start])
    print(l1[end])
    start +=1
    end -=1
    
#iterating the array in reverse
print('Printing in reverse order')
for item in reversed(l1):
    print(item)
    
#pring using the enumerate
print('using enumerate')
for index,item in enumerate(l1):
    print(f' List Item : {item} At Index : {index} ')

print('Pring using the zip function')
#iterate using zip function
for item, item2 in zip(l1,l1):
    print(item,item2)

list(zip('abcdefg', range(3), range(4)))