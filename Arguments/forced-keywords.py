#once you add aterik before the arguments then they are forceful keyword arguments



def forced(a,b,*,c,d):
    print("I am forcing")
    
forced(1,2,c=3,d=4)