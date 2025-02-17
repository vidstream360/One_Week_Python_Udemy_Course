

# num = int(input("Enter a number: "))
# print(f"you entered a number")
# if you run this code and someone enters an integer it works
# if someone enters a letter it doesnt work
# if you suspect there could be an error you can put it inside a try

try:
    num = int(input("Enter a number: "))
except:
    print("EXPECT BLOCK RUNNING")
    print("I'll pick for you....")
    num = 7

print(f"you entered a number")