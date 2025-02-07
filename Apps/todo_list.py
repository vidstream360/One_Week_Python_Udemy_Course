header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)

todos =[]                                #step 3 add list
completed = []                          #step 5 make completed list
while True:                           #step 1 make while loop
    for i in range(len(todos)):                   #step3 continued - call list (call as a for / range to make it numbered)
        print(f"* {i+1}) {todos[i]}")               
    print("***********************************") # step 1 continued
    print("Enter a todo tasks. Enter task number to compelte task. Enter q to quit. Type 'h' for help: " ) 
    command = input("> ")
    if command == "q":
        break
    elif command == "h":                 #step 6 help menu
        print("Todo List Help")
        print("Enter q to quit")
        print("To add a todo task to the list, type it and hit enter")
        print("To complete a todo task enter its list number")
        print("To receive completed task list hit q to quit")
    elif command.isnumeric():         #step 4 delete feature
        idx = int(command) - 1
        if idx >= len(todos):
            print("There is no todo with that number!")
        else:
            done_todo = todos.pop(idx)
            completed.append(done_todo)    #step 5 continued consolidate
    else:                             #step 2 else / break
        todos.append(command)
if completed:                           #step 5 contined insert completed
    print(f"You completed {len(completed)} todos today")
    for todo in completed:
        print(f"*{todo}")

print("Goodbye")