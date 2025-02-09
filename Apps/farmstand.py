prices = {
    "arugala" : 1.15,
    "basil" : 2.54,
    "blackberries" : 4.93,
    "blueberries" : 2.88,
    "coconut" : 7.15,
    "fennel" : 3.36,
}

#product = input("What product are you buying? ")
#if product in prices:
#    price = prices[product]
#   print(f"{product} is ${price}")
#else:
#    print("Sorry, we dont have that product today.")

product = input("What product are you buying? ")
price = prices.get(product)
if price:
    print(f"{product} is ${price}")
else:
    print("Sorry, we dont have that product today.")