def get_total(price, qty=1, tax=0.02, discount=0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))

get_total(9.75, 5, 0.01, 0.5)
get_total(price=9.75, qty=5, tax=0.01, discount=0.5)
get_total(price=9.75, discount=0.5, qty=5, tax=0.01) #when you use keyword arugments the order doesnt matter

get_total(8.99)
get_total(8.99, tax=0.025) #to get value for one specific keyword argument you need to label it

get_total(tax=0.025, 8.99) #no positional arguements can follow keyword arguements