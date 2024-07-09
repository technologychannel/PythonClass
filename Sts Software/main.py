from student import Student

total_sts = int(input("How many students data you want to insert: "))

for i in range(total_sts):
    n = input(f"Enter student {i+1} name: ")
    p = input(f"Enter student {i+1} phone: ")
    s = Student(name=n, phone=p)
    f = open("contact.csv","a")
    f.write(f"{s.name},{s.phone}\n")
    f.close()

### 
# Create program that save 10 product detail to file
# using user input. [id, name, qty, price]



