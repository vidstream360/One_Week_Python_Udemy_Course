#Look Before You LEap
# Coding style where you explicitly test for pre-conditions before making calls or "leaping"
# Characterized by lots of if statements

#ex

year = input("Enter a year: ")
if year.isnumeric():  #LOOK check if year is numeric
    year = int(year)  #LEAP convert year to int once we know its safe
    print(type(year))
else:
    year = 2025
    print(year)

