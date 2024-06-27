# Program that ask user to enter n no of todo and display it.
todos = []

total_todo = int(input("Enter total number of todo: "))

for i in range(1,total_todo+1):
    todo = input(f"Enter todo {i}: ")
    todos.append(todo) # Append 

print("\n------------\n")
print("All todos are: ")
# Display all result
for todo in todos:
    print(todo)
    

# Ask user to enter n number of fruits 
# and display all fruits


