# 1. Add task
# 2. Remove task
# 3. View tasks
# 4. Quit
# Choose an option: 1
# Enter task: Buy milk
# Task added!

# Choose an option: 1
# Enter task: Call mom
# Task added!

# Choose an option: 3
# Your tasks:
# 1. Buy milk
# 2. Call mom

# Choose an option: 2
# Enter task to remove: Buy milk
# Task removed!

# Choose an option: 4
# Goodbye!


def add_item(tasks, item):
    # your code here
    tasks.append(item)
    print("Task added!")

def remove_item(tasks, item):
    # your code here — remember the found-flag pattern
    found = False
    for t in tasks:
        if t == item:
            tasks.remove(t)
            found = True
    if found:
        print("Task Removed!")
    else:
        print("Task not found!")

def view_items(tasks):
    # your code here
    for index, item in enumerate(tasks, start=1):
                print(index, item)


task = []

print("Enter a To-do:")
print("1. Add Task.")
print("2. Remove Task.")
print("3. View Task.")
print("4. Quit.")

while True:
    toDo = int(input("Enter a number from the list: "))
    if toDo == 1:
        newTask = input("Enter task to add: ")
        add_item(task, newTask)
    elif toDo == 2:
        newTask = input("Enter task to remove: ")
        remove_item(task, newTask)
    elif toDo == 3:
         view_items(task)
        
    elif toDo == 4:
        print("Goodbye")
        break
    else:
        print("Invalid Option, select an option between 1-4")
