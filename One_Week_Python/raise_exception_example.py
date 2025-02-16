#raise is used to stop code if theres a problem
#useful for properly documenting
#example two functions, one relying on another 

def get_user_name():
    inp = input("please enter your name: ")
    if not inp.isalpha():
        raise ValueError("alpha chars only") # better than returning none or a string
    return inp

def register_user():
    user = get_user_name()
    Database.save(user)