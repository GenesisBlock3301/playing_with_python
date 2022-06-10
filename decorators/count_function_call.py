count = 0
def count_func(func):

    def wrapper(*args, **kwargs):
        global count
        count+=1
        print("calls",count)
        return func(*args,**kwargs)
    return wrapper


@count_func
def countt():
    pass
for i in range(5):
    countt()