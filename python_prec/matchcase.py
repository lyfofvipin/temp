amount = int(input("Kitne rs laye ho?? "))

# if amount == 20:
#     print("200ML")

# elif amount == 40:
#     print("750ML")

# elif amount == 50:
#     print("1L")

# elif amount == 90:
#     print("2.25L")

# else:
#     print("No cold drink.")


match amount:

    case 20:
        print("200ML")

    case 40:
        print("750ML")

    case 50:
        print("1L")
    
    case 90:
        print("2.5L")
    
    case _:
        print("No Cold Drink.")

