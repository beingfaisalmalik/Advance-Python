#function with returning the function


def external():
    def internal():
        print('hey')
    return internal

hy = external()
hy()


#function with internal function callign inside the external function

def external2():
    def internal2():
        return 2
    print(internal2())
external2()