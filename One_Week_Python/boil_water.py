unit = input("What unit are you using? F C or K?  " )
temp = int(input("What temperature is the water?  "))

unit = unit.upper()

if unit == 'F':
    if temp == 212:
        print("Water is boiling!")
    else:
        print("Water is not boiling. Must Hit 212F")
elif unit == 'C':
    if temp == 100:
        print("Water is boiling!")
    else:
        print("Water is not boiling. Must Hit 100C")
elif unit == 'K':
    if temp == 373:
        print("Water is boiling")
    else:
        print("Water is not boiling. Must hit 373K.")
else:
    print("I dont know those units")