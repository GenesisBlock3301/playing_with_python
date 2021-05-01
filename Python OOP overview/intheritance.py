class Bird:

    def __init__(self,name):
        self.name = name

    def whoisThis(self):
        print("This is bird")

    def swim(self):
        print('Swim faster')


class Penguin(Bird):
    def __init__(self,age):
        super().__init__(self)
        self.age = age
    def show(self):
        print("just for testing")


p = Penguin(10)
p.name = "Gulomulo"
p.swim()
print(p.name)
