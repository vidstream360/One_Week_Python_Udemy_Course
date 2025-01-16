print("***Welcome to Store***")
print("*" * 25)

item = (input("What item are you buying: "))

price = input(f"What is the price of {item}: ")

quantity = input(f"How many {item} are you buying: ")

total = float(price)*float(quantity)

print(f"Added {quantity} {item}(s) to shopping cart")
print(f"Subtotal: ${total}")
