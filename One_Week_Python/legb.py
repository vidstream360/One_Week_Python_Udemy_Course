#scopes order of operations
#legb: local enclosed global built-in

animal = "Nudibranch"

def outer():
    animal = "Echidna" 
    def inner():
        print("From Inner FUNC: ", animal)
    print("From Outer FUNC: ", animal)
    inner()
    
print("OUTSIDE OF FUNCTIONs", animal)
outer() #function will look for variables in local scope first, then enclosed, then global