
f = 'aisal'
print(f[::-1])


#check for palandrome
s = 'rotator'
print(s[::-1])
print(s[::])


print(s[::-1] == s[::])


# check for anagrams
a = 'slient'
b = 'listen'
aa = list(a)
bb = list(b)
aa.sort() 
bb.sort()

print(aa)
print(bb)


print(aa[::] == bb[::])

