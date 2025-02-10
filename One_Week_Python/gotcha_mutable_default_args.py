#example, if you pass an empty list to a function intending to appending it, python will continually add to it, not write over it

def add_twice(val, lst=[]):
    lst.append(val)
    lst.append(val)
    print(lst) #or return lst

add_twice('yay')
add_twice('boo')

#work around, set the list to none instead of empty, and check it with an if statement
def add_twice(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    lst.append(val)
    print(lst)

add_twice('yay')
add_twice('boo')