class student:
    grade = 10
    print("I am a student of grade", grade)

ob = student()
print("\n")

class fellow:
    age = 14
    name = "Affan"

    def introduction(self):
        print("Hi i am a student")

    def details(self):
        print("My name is", self.name)
        print("My age is", self.age)

j = fellow()
j.introduction()
j.details()
print("\n")

class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return f"{self.name} sings {song}"
     
    def dance(self):
        return f"{self.name} is now dancing"

Blu = Parrot("Blu", 10)
Woo = Parrot("Woo",5)

print("Blu is a", Blu.species)
print("Woo is a", Woo.species)

print(Blu.name, "is", Blu.age, "years old")
print(Woo.name, "is", Woo.age, "years old")

print(Blu.sing("Last"))
print(Woo.dance())