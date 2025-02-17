#Easier to ask for forgiveness than permission
#Assume things exist or will work and catch exceptions if youre wrong
#Coding style characterized by lots of try/except blocks in case youre wrong
#This apporach is more pythonic

# ex

try:
    year = int(input("Enter a year: ")) #Assume it wil work, try converting year to an integer
except ValueError: #Catch exception if youre wrong, this code runs if year cant be cast to an int
    year = 2025

