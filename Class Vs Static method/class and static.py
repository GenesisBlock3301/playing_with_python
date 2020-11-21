class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #     you can change class state
    @classmethod
    def class_method(cls,name,age):
        return C(name,age)

    # @staticmethod


c = C.class_method("sifat",23)
print(c)