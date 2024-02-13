import functools


class Bottle:
    def __init__(self):
        self._content = None

    def __call__(self):
        return self._content

    def set_content(self, *a, **ka):
        self._content = a[0]

    def get_content(self):
        return self._content


bottle = Bottle()


# bottle.set_content("nas")

# Decorator function
def make_default_wrapper(name):
    method = getattr(bottle, name)

    def decorator(func):
        @functools.wraps(method)
        def wrapper(*a, **ka):
            if name == 'set_content':
                bottle.set_content(*a, **ka)
                print("get_content:", bottle.get_content())
            return func(bottle.get_content())
        return wrapper

    return decorator


route = make_default_wrapper("set_content")
# route = make_default_wrapper("get_content")


@route("Hello")
def greet(name):
    """This function greets a person by name"""
    return f"Hello, {name}"


result = greet("John")
print(result)
# print(result.__name__)
# print(result.__doc__)
