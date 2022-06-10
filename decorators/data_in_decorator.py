
def running_average(func):
    data = {"total": 0, "count": 0}

    def wrapper(*arg, **kwargs):
        val = func(*arg, **kwargs)
        data["total"] += val
        data["count"] += 1
        print(f"Average of {data['total']} of far: {data['count']},{func.__name__}")
        return func(*arg, **kwargs)
    # print("wrapper data",
    return wrapper

@running_average
def foo(x):
    return x+2

print(foo(2))
print(foo(2))