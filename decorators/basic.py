def printlog(func):
    def wrapper(arg):
        print(f"CALLING: {func.__name__}")
        return func(arg)
    return wrapper


@printlog
def foo(x):
    print(x+2)
@printlog
def buz(x,y):
    print(x+y)
foo(2)
buz(3,4)