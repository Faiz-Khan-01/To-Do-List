# A CLI Based Simple To-Do List app

tasks = [] # stores the tasks
completed_tasks = [] # stores the completed tasks

def list_features(): # Will list out all the features
    print('''Press appropriate number to perform an action.
1 : Add a New Task
2 : Mark a Task Done
3 : Remove a Task
4 : List Tasks
5 : List Completed Tasks
6 : Clear All Tasks
7 : Exit\n''')

def add_task() : # Adds a New task 
    new = input("Add a New Task.\n")
    tasks.append(new.capitalize())
    print("New Task Added!\n")
    
def complete_task() : # Completes a task
    complete = input("Enter the Task Name.\n")
    completed_tasks.append(complete)
    tasks.remove(complete.capitalize())
    print("Task Completed Successfully!\n")

def remove_task() : # Removes a task
    delete = input("Enter the Task Name.\n")
    complete_task.append(complete)
    tasks.remove(delete.capitalize())
    print("Task Removed.\n")

def list_tasks() : # Lists all the tasks
    if len(tasks) == 0 :
        print("The Task List is Empty.\n")
    else :
        print("Tasks List:") 
        for i in tasks :
            print("-",i)
        print()

def list_completed_tasks() : # lists completed tasks
    if len(completed_tasks) == 0 :
        print("Do Something first!\n")
    else :
        print("Tasks Completed: ")
        for j in completed_tasks :
            print(f"- {j}")
        print()

def clear_tasks() : # Clear all the tasks
    tasks.clear()
    completed_tasks.clear()
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
    elif command == 6 :
        clear_tasks()
    elif command == 5 :
        list_completed_tasks()
    elif command == 7 :
        print("Exiting the program...")
        break
    else :
        list_features()