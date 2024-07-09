class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def display(self):
        print(f"Name: {self.name}, Phone: {self.phone}")
