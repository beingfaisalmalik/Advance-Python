import random

#generates a float number between 0 and 1
a = random.random()
print(a)

#uniform range
#generates a floating number between  the given uniform range more than 1 less then 10
a = random.uniform(1,10)
print(a)

#the last number is included in it and generates the integar number not the float number
ab = random.randint(1,10)
print(ab)


#last number will be excluded from the range
aabb = random.randrange(1,10)
print(aabb)

ss = random.choice(list('ABCDEF'))
print(ss)

ss = random.sample(list('ABCDEF'),3)
print(ss)

cc = random.choices(list('ADVFC'),k=3)
print(cc)

a = [1,2,3,4,5]
random.shuffle(a)
print(a)