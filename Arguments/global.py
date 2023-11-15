def foo():
    x = number
    print(f'The Number Is {x}')
number = 10
foo()


def foo2():
    global number 
    number =20
    print(f'The Number here is {number}')
    
foo2()