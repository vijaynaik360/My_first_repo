class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("some sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

dog1=Dog("Buddy")
dog1.sound()