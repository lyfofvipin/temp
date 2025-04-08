#Write a Python class BankAccount with attributes like:>>>>
#  account_number, balance,  date_of_opening and  customer_name, 
# and methods like >>>>
# deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs.{amount}. New balance is Rs.{self.balance}.")
        else:
            print("Invalid deposit amount.")


    def widthdraw(self, amount):
        if amount>0 and amount<= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance is Rs.{self.balance}.")
        else:
            print("Insufficient balance.")
