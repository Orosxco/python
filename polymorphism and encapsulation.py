class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a cat, my name is {self.name}. I am {self.age} years old")
    
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"I am a dog, my name is {self.name}. I am {self.age} years old")
    
    def sound(self):
        print("Bark")

e = cat("Chloe", 2.5)
f = Dog("Max", 5)

for animal in(e,f):
    animal.sound()
    animal.info()