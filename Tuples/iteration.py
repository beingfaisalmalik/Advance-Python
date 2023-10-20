a = tuple([1,2,3,4])

#iteration using the for loop
for number in a:
    print(number)
    
    
#iteration using the while loop
print('Using the while loop')
start = 0
end = len(a)-1

while(start<=end):
    print(a[start])
    print(a[end])
    start +=1
    end -=1