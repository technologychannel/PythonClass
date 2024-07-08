# OOP: Object Oriented Programming. In OOP we use class and object to
# design computer programs
# Class: Blueprint to Create Object
# Object: Instance of Class
### How to create class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name}")    
        print(f"Age is {self.age}")    

### How to create object
st1 = Student(name="Ajaya", age=30)
st1.display()

st2 = Student("Bijay", age=23)
st2.display()
# Create Class Teacher with parameter name and salary, and display method
# Create 3 object of Teacher and Display details
