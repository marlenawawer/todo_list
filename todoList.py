from tabulate import tabulate
import os
import json

action = {"1": "Add a new task.",
          "2": "Show list of tasks.",
          "3": "Mark task as done.",
          "4": "Delete a task from the list.",
          "5": "Export todo list to JSON file",
          "6": "Import new tasks from JSON file",
          "7": "Exit"
}

todo_list = []

##################### Change here #############################
folderPath = r'C:\Users\marle\OneDrive\Pulpit\todo\tasks_lists'
###############################################################

def create_task(task, priority):
    if len(todo_list) == 0:
        i=1
    else:
        i = todo_list[-1][0]+1
    new_task = [i, task, priority, False]
    return new_task


while True:
    choice = 0
    print("\n")
    while choice not in action:
        for key, value in action.items():
            print(f"{key}. {value}")
        choice = input("What do you want to do: ")
    else:
        if choice == "1":
            task = input("Insert a task: ")
            try:
                priority = int(input(f"Insert task priority (1-3): '{task}' - "))
            except ValueError as e:
                print(f"Invalid input: {e}")
            else:
                if priority in range(1,4):
                    new_task = create_task(task, priority)
                    todo_list.append(new_task)
                    print("The new task has been successfully added to your list.")
                else:
                    print(f"Invalid input: {priority}")
        if choice == "2":
            print(tabulate(todo_list, headers=["Task number", "Description", "Priority", "Done"])+"\n")
        if choice == "3":
            task_completed = input("Which task do you want to mark as 'completed'? Enter a task number: ")
            for task in todo_list:
                if task_completed == str(task[0]):
                    task[3] = True
                    print(f"Task {task_completed} has been marked as 'completed")
                    break
            else:
                print("Invalid input\n")
        if choice == "4":
            task_to_delete = input("Which task do you want to delete? Enter a task number: ")
            for task in todo_list:
                if task_to_delete == str(task[0]):
                    todo_list.remove(task)
                    print(f"Task {task_to_delete} has been deleted")
                    break
            else:
                print("Invalid input\n")
        if choice == "5":
            fileName = input("Enter a file name: ")
            fullPath = os.path.join(folderPath, fileName+".json")
            with open(fullPath, 'w', encoding='utf-8') as jsonFile:
                json.dump(todo_list, jsonFile)
            print(f"Your list has been saved as {fileName}.json")
        if choice == "6":
            list_of_files = []
            files = os.listdir(folderPath)
            for index, file_name in enumerate(files, start=1):
                file = [index, file_name]
                list_of_files.append(file)
            print(tabulate(list_of_files, headers=['File number', 'File name']))
            fileNumber = input("Which file do you want to import? Enter a file number: ")
            try:
                fullPath = os.path.join(folderPath, files[int(fileNumber)-1])
            except IndexError as e:
                print(f"Invalid input: {e}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            else:
                with open(fullPath, encoding='utf-8') as jsonFile:
                    additional_tasks = json.load(jsonFile)
                    for argument in additional_tasks:
                        if len(todo_list) == 0:
                            todo_list.append(argument)
                        else:
                            argument[0] = todo_list[-1][0]+1
                            todo_list.append(argument)
                print("Your file has been imported successfully.")
        if choice == "7":
            print("See you soon!")
            break



