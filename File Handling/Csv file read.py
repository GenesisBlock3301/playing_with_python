def lowercase_decorator(func):
    def wrapper():
        function = func()
        string_lower_case = function.lower()
        return string_lower_case

    return wrapper


def split_decorator(func):
    def wrapper():
        function = func()
        split_sentence = function.split()
        return split_sentence

    return wrapper


@split_decorator      #<- second execute
@lowercase_decorator  #<- first execute
def hello():
    return "Hello World"


# l = lowercase_decorator(hello)
# s = split_decorator(hello)
# print(l)
# print(s)
print(hello())
