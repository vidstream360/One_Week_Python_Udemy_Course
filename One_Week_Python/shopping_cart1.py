print("***Welcome to Store***")

item = (input("What item are you buying?"))
#print(item)

price = input(f"What is the price of {item}?")
#print(price)

quantity = input(f"How many {item} are you buying?")
#print(quantity)

total = float(price)*float(quantity)

print(f"Added {quantity} {item}(s) to shopping cart")
print(f"Subtotal: ${total}")