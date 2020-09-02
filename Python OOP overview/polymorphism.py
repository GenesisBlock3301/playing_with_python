class Bird:

    def __init__(self,name):
        self.name = name

    def whoisThis(self):
        print("This is bird")



    def swim(self,place):
        print(f"swiming in the {place}")


class Penguin(Bird):
    def __init__(self,age):
        super().__init__(self)
        self.age = age
    def show(self):
        print("just for testing")

    def swim(self):
        print('Penguin Swim faster')

# b = Bird("Gulumulo")
# b.swim("pond")
p = Penguin(10)
p.swim()