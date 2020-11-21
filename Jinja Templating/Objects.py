from jinja2 import Template


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age

    def getName(self):
        return self.name

person = Person('Sifat',24)

tm = Template("My name is {{person.getName()}} and I am {{person.getAge()}}")
msg = tm.render(person=person)
print(msg)