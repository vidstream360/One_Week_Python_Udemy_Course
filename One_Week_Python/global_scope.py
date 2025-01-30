animal = "Lemur" 
# ^^ global variable, everything has acess to the varaible
#available inside of functions and outside of functions

print("OUTSIDE OF FUNCTION: ", animal)

def func():
    print("INSIDE FUNC: ", animal)
    def inner_func():
        print("INSIDE INNER FUNC: ", animal)
    inner_func() 
    #^^ nested function, make sure to call it or it wont run

func()