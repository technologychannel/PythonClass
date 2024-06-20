todo_list = ['Learn Python', 'Read 1 Book', 'Meditation', 'Meditation']

todo_list.append("Listen to Audibook")
#todo_list.clear()

# print(todo_list[3])

todo_list[3] = "Go to gym"

todo_list.pop() # Remove last item

for todo in todo_list:
    print(todo)