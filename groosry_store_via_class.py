item_purchased_by_customer = { 
    "Milk": {"quantity": 0, "amount": 0},
    "Bread": {"quantity": 0, "amount": 0},
    "Banana": {"quantity": 0, "amount": 0},
    "Apple": {"quantity": 0, "amount": 0}
    }
each_item_prise = { "Milk": 3.97, "Bread": 2.17, "Banana": .99, "Apple": .89}
item_price_on_sale = { "Milk": 5.0, "Bread": 6.0 }
item_on_sale = {"Milk": 2, "Bread": 3}

class my_groosry:

    def __init__(self, item_purchased_by_customer, each_item_prise, item_price_on_sale, item_on_sale):
        self.item_purchased_by_customer = item_purchased_by_customer
        self.each_item_prise = each_item_prise
        self.item_price_on_sale = item_price_on_sale
        self.item_on_sale = item_on_sale
        self.amount_saved = 0
        self.total = 0

    def get_item_list(self):
        items = raw_input("Please enter all the items purchased separated by a comma: ")
        return  [ item.capitalize() for item in items.split(",")]

    def get_item_quantity(self):
        items = self.get_item_list()
        for item in items:
            self.item_purchased_by_customer[item]["quantity"] += 1

    def calculate_prise(self):
        items_quantity = self.get_item_quantity()
        for item in self.item_purchased_by_customer.keys():
            quantity = self.item_purchased_by_customer[item]["quantity"]
            if item in self.item_on_sale.keys():
                self.item_purchased_by_customer[item]["amount"] = (quantity//self.item_on_sale[item])*item_price_on_sale[item] + (quantity%self.item_on_sale[item])*each_item_prise[item]
            else:
                self.item_purchased_by_customer[item]["amount"] = quantity*each_item_prise[item]
        return self.item_purchased_by_customer, self.amount_saved

    def calculate_total(self):
        self.calculate_prise()
        for item in self.item_purchased_by_customer.keys():
            self.total += self.item_purchased_by_customer[item]["amount"]
        return self.total

    def calculate_saved_amount(self):
        for item in self.item_purchased_by_customer.keys():
            if item in self.item_on_sale.keys():
                quantity = self.item_purchased_by_customer[item]["quantity"]
                self.amount_saved += quantity//self.item_on_sale[item]*self.item_on_sale[item]*each_item_prise[item] - (quantity//self.item_on_sale[item])*item_price_on_sale[item]
        return self.amount_saved

    def display_output(self):
        total = self.calculate_total()
        saved_amount = self.calculate_saved_amount()
        print("Item \t Quantity \t Price \n" + "-"*30)
        for item in self.item_purchased_by_customer.keys():
            if self.item_purchased_by_customer[item]["quantity"] != 0:
                print("{0} \t {1} \t\t ${2} ".format(item, self.item_purchased_by_customer[item]["quantity"], self.item_purchased_by_customer[item]["amount"]))
        print("Total price : $" + str(total))
        print("You saved $" + str(saved_amount) + " today.")


calculate = my_groosry(item_purchased_by_customer, each_item_prise, item_price_on_sale, item_on_sale)
calculate.display_output()

# [vipikuma@kvy work_data]$ echo -e "milk,milk,bread,banana,bread,bread,bread,milk" | python /home/vipikuma/test.py
# Please enter all the items purchased separated by a comma: Item 	 Quantity 	 Price 
# ------------------------------
# Banana 	 1 		 $0.99 
# Milk 	 3 		 $8.97 
# Bread 	 4 		 $8.17 
# Total price : $18.13
# You saved $3.45 today.
# [vipikuma@kvy work_data]$ echo -e "milk,milk,bread,banana,bread,bread,bread,milk,apple,apple" | python /home/vipikuma/test.py
# Please enter all the items purchased separated by a comma: Item 	 Quantity 	 Price 
# ------------------------------
# Banana 	 1 		 $0.99 
# Apple 	 2 		 $1.78 
# Milk 	 3 		 $8.97 
# Bread 	 4 		 $8.17 
# Total price : $19.91
# You saved $3.45 today.
# [vipikuma@kvy work_data]$ echo -e "milk,milk,bread,banana,bread,bread,bread,milk,apple,apple,milk" | python /home/vipikuma/test.py
# Please enter all the items purchased separated by a comma: Item 	 Quantity 	 Price 
# ------------------------------
# Banana 	 1 		 $0.99 
# Apple 	 2 		 $1.78 
# Milk 	 4 		 $10.0 
# Bread 	 4 		 $8.17 
# Total price : $20.94
# You saved $6.39 today.
# [vipikuma@kvy work_data]$ 
