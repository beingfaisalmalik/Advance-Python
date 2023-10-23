s = 'Faisal'

#for rach loop
for letter in s:
    print(letter)

#for loop 
for i in range(len(s)):
    print(s[i])
    
#using while loop
start =0
end = len(s)-1
#using while loop
print('With While Loop')
while(start<=end):
    print(s[start])
    print(s[end])
    start +=1
    end -=1
    
    
#using if it will do single iteration
print('F' in s)