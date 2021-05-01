class Parrot:
    species = "bird" #class varibale

    #constructor
    def __init__(self,name,age):
        self.name = name #instance variable
        self.age = age

    def show(self):
        return self.name

    def __str__(self):
        return "This is name "+self.name+" age is "+str(self.age)





#instantiate / object

blu = Parrot('Blue',10)
# gre = Parrot('Green',15)
# print(f"Blue is {blu.__class__.species}")
# print(f"Blue is {Parrot.species}")
# print(f"Blue is {blu.species}")
##########
print(blu)
