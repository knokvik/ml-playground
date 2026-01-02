class MIT :
    clg = "Maharashtra Institute of Technology"

    def greet(self):
        print("Good Morning!")

class Student(MIT) : # Inheritance
    def __init__(self,name,age): # Constructor 
        self.name = name
        self.age= age

    def greet(self) :
        print("Ayy!")
        super().greet()

    def __del__(self): # Destructor
        print("Object Destroyed!")

s1 = Student("Neeraj",20) 
print(s1.name)
print(s1.age)
print(s1.clg)
s1.greet()