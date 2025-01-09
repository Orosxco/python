class Person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def Display(self):
        print(self.name)
        print(self.idnumber)
    
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)

a = Employee("James", 814, 124000, "RND")
a.Display()
print(a.salary, a.post)
print("\n")
