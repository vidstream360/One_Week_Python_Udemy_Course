year = input("What year were you born in?")

if not year.isnumeric():
    year = input("That isnt a number. Try again please. What year were you born?")

year =int(year)

print(f"You were born {2025-year} years ago")