def zoo ():
    animal = "Harlequin Shrimp" #variable is local to zoo function, it is scoped to that function
    number = 77
    print("Inside ZOO Function: ", animal, number)

zoo()

print("Outside Function: ", animal) #calling local varialbe outside function wont work
print(number)