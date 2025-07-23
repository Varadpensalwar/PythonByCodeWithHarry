class Animal:
    country = "USA"

    def __init__(self, name):
        self.name = name

    def speak(name):
        print("Speaking now....")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("wooof")

e = Dog("shreu")
e.speak()
print(e.country)