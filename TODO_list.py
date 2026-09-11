# A CLI Based Simple To-Do List app

Items = [] # List that will store the Data

def list_features(): # Will list out all the features
    print('''Press appropriate number to perform an action.
1 : Add a New Task
2 : Mark a Task Done
3 : Remove a Task
4 : List Tasks
5 : Clear All Tasks
6 : Exit\n''')

def add_task() : # Adds a New task 
    new = input("Add a New Task.\n")
    Items.append(new.capitalize())
    print("New Task Added!\n")
    
def complete_task() : # Completes a task
    complete = input("Enter the Task Name.\n")
    Items.remove(complete.capitalize())
    print("Task Completed Successfully!\n")

def remove_task() : # Removes a task
    delete = input("Enter the Task Name.\n")
    Items.remove(delete.capitalize())
    print("Task Removed.\n")

def list_tasks() : # Lists all the tasks
    if len(Items) == 0 :
        print("The Task List is Empty.\n")
    else :
        print("Tasks List:")
        for i in Items :
            print("-",i)
        print()

def clear_tasks() : # Clear all the tasks
    Items.clear()
    print("All Tasks Removed.\n")

list_features()

while True : # Will take commands and perform actions
    command = int(input())
    if command == 1 :
        add_task()
    elif command == 2 :
        complete_task()
    elif command == 3 :
        remove_task()
    elif command == 4 :
        list_tasks()
    elif command == 5 :
        clear_tasks()
    elif command == 6 :
        print("Exiting the program...")
        break
    else :
        list_features()
