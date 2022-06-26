class Employee(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
    
    def __eq__(self,other) -> bool:
        return self.age == other.age and self.name == other.name
    
    def __hash__(self) -> int:
        return hash((self.name,self.age))

e = Employee("sifat",25)
print(hash(e))