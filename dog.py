from cat import Cat
class Dog:

    kind = "Corgi"
    #special method auto called during initialization.
    def __init__(self, name):
        self.name = name #instance variable

    #self: gives us access to attributes/methods in class
    def ageSet(self, age):
        self.age = age

d0 = Dog("Bingo")
d0.ageSet(5)
#d0.name - "Bingo"
print(d0.name, d0.kind, d0.age)
c0 = Cat("Shrimp")
print(c0.name)