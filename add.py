def add_two_number(request):
    def myfun (a,b):
        return a+b
    return myfun
@add_two_number
def hello(a,b):
    return a,b
print("Total values",hello(30,70))
