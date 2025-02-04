#common pattern of check in a variable is in or not in a list

flavors = ["chocolate", "vanilla", "lemon", "strawberry"]

response = input("What flavor would you like?")

while response.lower() not in flavors:
    response = input("Flavor not available. Please choose another flavor")

print(f"Ok {response} ice cream coming right up!") 
