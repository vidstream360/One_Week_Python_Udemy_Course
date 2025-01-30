def outer():
    animal = "Secretary Bird"
    def inner():
        print("Inside Inner Func: ", animal)
        def third():
            print("Inside Third Nested Func: ", animal)
        third()
    inner()

outer()
animal() 