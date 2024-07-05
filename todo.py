### Ask user to enter todos and print all todo
total_todo = int(input("Enter total todo: "))
todos = []

### Ask 
for i in range(0, total_todo):
    todo = input(f"Enter todo {i+1}: ")
    todos.append(todo)

### Display
for todo in todos:
    print(todo) 


### Ask user to enter n number of people names
### And print all names start with B
### If there is no name, it should say "No Name Found"
### If there is/are names, it should display all names.
