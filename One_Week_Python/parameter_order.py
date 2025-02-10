def display_info(person,*args, status="single", **kwargs): 
    print(f"person is: {person}")
    print(f"status is: {status}")
    print(f"kwargs is: {args}")
    print(f"kwargs is: {kwargs}")

#put args para before a default value, you can provide a new default value if you over ride it with a keyword
#example, if you dont input new value with keyword, status defaults to single
#kwargs should go last

display_info("colt", "purple", 4,5,6,7, status="married", bogos="binted")