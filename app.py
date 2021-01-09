import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    str_title=str(title)
    todos.append(str_title)
    print("Your to'do has been added successfully")
     
def print_list():
    global todos
    print(f"This is your to'do list:")
    count=1
    for todo in todos:
        print(str(count)+'. '+str(todos[count-1]))
        count=count+1
    print(f"You have= {str(len(todos))} to'do added")

def delete_task(number_to_delete):
    todos.pop(int(number_to_delete)-1)
    print (f"Your to'do list {number_to_delete} has been delete successfully")

def save_todos():
    with open('todoslist.csv','w', newline='') as f:
        writer= csv.writer(f,delimiter="\n")
        writer.writerow(todos)
        
def load_todos():
    with open('todoslist.csv', newline='') as f:
        reader = csv.reader(f,delimiter="\n")
        todos.clear
        for row in reader:
            print(', '.join(row))

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            print ("Good bye")
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")