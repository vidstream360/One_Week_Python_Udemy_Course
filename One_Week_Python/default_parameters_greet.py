#order matters and required parameters should go fisrt, defaults should go last

def greet(person, msg="Hi"):
    print(f"{msg}, {person}!")

greet("Tonya")