first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

full_len = len(first_name) + len(last_name)

if full_len > 12:
    print(f"{first_name} {last_name} is longer than average length of an American name.")
elif full_len == 12:
    print(f"{first_name} {last_name} is equal to the average length of an American name.")
else:
    print(f"{first_name} {last_name} is shorter than average length of an American name.")
