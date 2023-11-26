#Create my class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age
        
#Attributes and methods
    def greet(self):
        print("Hello, my name is", self.name)

#Inheritance
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    def study(self):
        print(self.name, "is studying", self.major)
