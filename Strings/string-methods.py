name = 'Faisal'
print(name)

list_of_methods = name.__dir__()
print(list_of_methods)

#total number of methods in the 
for index, name_of_method in enumerate(list_of_methods):
    if '__' not in name_of_method:
        print(f'{index}: Name of Method {name}')
#encode method 

#replace method does not affects the original string returns a new string
replaced_letter = name.replace('F','A')
print(replaced_letter)
#original Word
print(name)

#using capitalize word
captial = name.capitalize()
print(captial)

#using the title method
title  = name.title()
print(title)

#using lower words
lower = name.lower()
print(lower)


# casefold method good for comparision
casefold = name.casefold()
print(casefold)

# turns every char into upper case
upper = name.upper()
print(upper)

# changes case from uppercase to lower case lower case to upper case of every char
swapped = name.swapcase()
print(swapped)


#boolens methods

#checks if char is upper
is_upper = name.isupper()
print(is_upper)

#checks if every char of the string is lower
is_lower = name.islower()
print(is_lower)

#checks if the strign is in the title case
is_title = name.istitle()
print(is_title)

# checks if the string is numeric or not
is_numeric = name.isnumeric()
print(is_numeric)

#checks if there are numbers and letters in the string
print(name.isalpha())

F_count = name.count('a')
print(F_count)

F_index = name.index('F')
print(F_index)

ai_index = name.find('i')
print(ai_index)


l = ['M','A','L','I','K']
last_name =''
full_name = last_name.join(l)
print(full_name)

nn = name.join(full_name)
print(nn)

splitter = ' F.A.I.S.A.L.....Malik' 
print(splitter.split('.'))
print(splitter)
#used for removign the whitespaces
print(splitter.lstrip('.'))


txt = ',,,,,Faisal,,aw..'
print(txt.lstrip(",aw."))

text =  '     Faisal'
print(text)
print(text.strip())