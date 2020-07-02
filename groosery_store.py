available_items = { "Milk": 0, "Bread": 0, "Banana": 0, "Apple": 0}
purchased_item = { "Milk": [0, 0], "Bread": [0, 0], "Banana": [0, 0], "Apple": [0, 0]}
item_price = { "Milk": 3.97, "Bread": 2.17, "Banana": .99, "Apple": .89}
item_sale_price = { "Milk": 5.0, "Bread": 6.0 }
sale_on = {"Milk": 2, "Bread": 3}

items = raw_input("Please enter all the items purchased separated by a comma: ")

total ,amount_saved = 0, 0
for item in [ x.capitalize() for x in items.split(",")]:
    available_items[item] += 1
    purchased_item[item][0] += 1
    if item in sale_on and available_items[item] == sale_on[item]:
        total += item_sale_price[item]
        purchased_item[item][-1] += item_sale_price[item]
        available_items[item] = 0
        amount_saved += (item_price[item]*sale_on[item] - item_sale_price[item])

for item in available_items.keys():
    if available_items[item] != 0 : total += item_price[item]*available_items[item]

for key, values in purchased_item.items():
    if key.lower() in items.split(","): print("{0} \t {1} \t\t ${2} ".format(key, 1 if values[0] == 0 else values[0], item_price[key] if values[-1] not in sale_on.keys() else values[-1]))

print("Item \t Quantity \t Price \n" + "-"*30)
print("Total price : $" + str(total))
print("You saved $" + str(amount_saved) + " today.")






##########################################
# [vipikuma@kvy cit]$ python /home/vipikuma/test.py
# Please enter all the items purchased separated by a comma: milk,milk,bread,banana,bread,bread,bread,milk
# Banana 	 1 		 $0.99 
# Milk 	 3 		 $3.97 
# Bread 	 4 		 $2.17 
# Item 	 Quantity 	 Price 
# ------------------------------
# Total price : $18.13
# You saved $3.45 today.
# [vipikuma@kvy cit]$ python /home/vipikuma/test.py
# Please enter all the items purchased separated by a comma: milk,milk,bread,banana,bread,bread,bread,milk,milk
# Banana 	 1 		 $0.99 
# Milk 	 4 		 $3.97 
# Bread 	 4 		 $2.17 
# Item 	 Quantity 	 Price 
# ------------------------------
# Total price : $19.16
# You saved $6.39 today.
# [vipikuma@kvy cit]$ 
