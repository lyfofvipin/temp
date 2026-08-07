class Item:

    def __init__(self, item_name, item_qty, item_price):
        self.name = item_name
        self.qty = item_qty
        self.price = item_price

    def total(self):
        return self.qty * self.price


cart = []
while True:

    action = input("Press 1 for continue shopping and 2 for checkout and 3 to stop: ")
    if action == "1":
        name = input("Enter Item Name: ")
        qty = int(input("Enter Qty: "))
        price = float(input("Enter Price Per Item: "))
        cart.append( Item(name, qty, price) )

    elif action == "2":
        for x in cart:
            print( f"{x.name}: {x.total()}")

    elif action == "3":
        for x in cart:
            print( f"{x.name}: {x.total()}")
        break
    else:
        print("Invalid Action.")
