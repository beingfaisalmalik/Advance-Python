def foo(a,b,c,d,e):
    return a+b+c+d+e
l = [1,2,3,4,5]


print(foo(*l))



def foo2(a,b,c):
    print(a,b,c)
 
dic = {'a':1,'b':3,'c':4}   
foo2(**dic)