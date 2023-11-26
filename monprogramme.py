#Create my class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =age
        
#Attributes and methods
    def greet(self):
        print("Hello, my name is", self.name)

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self.__age = age

#Inheritance
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    
    def study(self):
        print(self.name, "is studying", self.major)

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def teach(self):
        print(self.name, "is teaching", self.subject)
