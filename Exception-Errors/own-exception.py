class ValueTooHigh(Exception):
    def __init__(self,value,message):
        self.message =message
        self.value =value

def test(a):
    if a >500:
        raise ValueTooHigh(a,'Value Is Too High')
    else:
        print(a)
test(600)
