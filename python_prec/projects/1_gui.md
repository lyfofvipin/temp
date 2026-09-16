
## 6. Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class BankAccount:
    def __init__(self, name, mobile, age, dob, balance=0.0):
        self.name = name
        self.mobile = mobile
        self.age = age
        self.dob = dob
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}"
        return False, "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be greater than zero."
        if amount <= self.balance:
            self.balance -= amount
            return True, f"Withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}"
        return False, f"Insufficient funds! Current balance: ${self.balance:.2f}"

class BankAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Management System - CRUD GUI")
        self.root.geometry("600x500")
        self.root.configure(bg="#f8fafc")
        
        self.accounts = []

        header = tk.Frame(self.root, bg="#1e293b", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="National Bank Portal (CRUD)", fg="white", bg="#1e293b", font=("Arial", 16, "bold")).pack(pady=15)

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_create = ttk.Frame(self.notebook)
        self.tab_manage = ttk.Frame(self.notebook)
        self.tab_view = ttk.Frame(self.notebook)

        self.notebook.add(self.tab_create, text="Create Account")
        self.notebook.add(self.tab_manage, text="Transactions / Update / Delete")
        self.notebook.add(self.tab_view, text="View Account")

        self.setup_create_tab()
        self.setup_manage_tab()
        self.setup_view_tab()

    def setup_create_tab(self):
        frame = ttk.LabelFrame(self.tab_create, text=" New Customer Registration ", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        fields = ["Customer Name:", "Mobile Number:", "Age:", "Date of Birth (DD-MM-YYYY):", "Initial Deposit ($):"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=6)
            ent = ttk.Entry(frame, width=28)
            ent.grid(row=i, column=1, sticky=tk.W, pady=6, padx=10)
            self.entries[text] = ent

        ttk.Button(frame, text="Create Account", command=self.create_account).grid(row=len(fields), column=0, columnspan=2, pady=15)

    def setup_manage_tab(self):
        frame = ttk.LabelFrame(self.tab_manage, text=" Account Operations (Update / Delete) ", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Mobile Number:").grid(row=0, column=0, sticky=tk.W, pady=6)
        self.m_mobile = ttk.Entry(frame, width=25)
        self.m_mobile.grid(row=0, column=1, sticky=tk.W, pady=6)

        ttk.Label(frame, text="Amount / New Name:").grid(row=1, column=0, sticky=tk.W, pady=6)
        self.m_param = ttk.Entry(frame, width=25)
        self.m_param.grid(row=1, column=1, sticky=tk.W, pady=6)

        btn_frame = ttk.Frame(frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="Deposit", command=lambda: self.do_trans("deposit")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Withdraw", command=lambda: self.do_trans("withdraw")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Delete Account", command=self.delete_account).pack(side=tk.LEFT, padx=5)

    def setup_view_tab(self):
        frame = ttk.LabelFrame(self.tab_view, text=" Account Search & Details ", padding=15)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        top_f = ttk.Frame(frame)
        top_f.pack(fill=tk.X, pady=5)

        ttk.Label(top_f, text="Mobile:").pack(side=tk.LEFT, padx=5)
        self.v_mobile = ttk.Entry(top_f, width=20)
        self.v_mobile.pack(side=tk.LEFT, padx=5)
        ttk.Button(top_f, text="Search", command=self.search_account_gui).pack(side=tk.LEFT, padx=5)

        self.info_box = tk.Text(frame, height=10, width=45, font=("Courier", 10))
        self.info_box.pack(fill=tk.BOTH, expand=True, pady=10)
        self.info_box.config(state=tk.DISABLED)

    def find_acc(self, mobile):
        for acc in self.accounts:
            if acc.mobile == mobile:
                return acc
        return None

    def create_account(self):
        name = self.entries["Customer Name:"].get().strip()
        mobile = self.entries["Mobile Number:"].get().strip()
        age_str = self.entries["Age:"].get().strip()
        dob = self.entries["Date of Birth (DD-MM-YYYY):"].get().strip()
        bal_str = self.entries["Initial Deposit ($):"].get().strip()

        if not all([name, mobile, age_str, dob, bal_str]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if self.find_acc(mobile):
            messagebox.showerror("Error", "Account with this mobile number already exists!")
            return

        try:
            age = int(age_str)
            bal = float(bal_str)
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer and balance a valid number.")
            return

        acc = BankAccount(name, mobile, age, dob, bal)
        self.accounts.append(acc)
        messagebox.showinfo("Success", f"Account created for {name}!")
        for ent in self.entries.values():
            ent.delete(0, tk.END)

    def do_trans(self, t_type):
        mobile = self.m_mobile.get().strip()
        val_str = self.m_param.get().strip()
        if not mobile or not val_str:
            messagebox.showerror("Error", "Mobile and amount are required.")
            return

        acc = self.find_acc(mobile)
        if not acc:
            messagebox.showerror("Error", "Account not found.")
            return

        try:
            amt = float(val_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return

        success, msg = acc.deposit(amt) if t_type == "deposit" else acc.withdraw(amt)
        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showwarning("Warning", msg)
        self.m_mobile.delete(0, tk.END)
        self.m_param.delete(0, tk.END)

    def delete_account(self):
        mobile = self.m_mobile.get().strip()
        acc = self.find_acc(mobile)
        if acc:
            self.accounts.remove(acc)
            messagebox.showinfo("Success", f"Account associated with {mobile} has been deleted.")
            self.m_mobile.delete(0, tk.END)
            self.m_param.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Account not found.")

    def search_account_gui(self):
        mobile = self.v_mobile.get().strip()
        acc = self.find_acc(mobile)
        self.info_box.config(state=tk.NORMAL)
        self.info_box.delete("1.0", tk.END)
        if acc:
            details = f"""========================================
         CUSTOMER ACCOUNT STATEMENT
========================================
 Customer Name : {acc.name}
 Mobile Number : {acc.mobile}
 Age           : {acc.age}
 Date of Birth : {acc.dob}
 Current Bal   : ${acc.balance:.2f}
========================================"""
            self.info_box.insert(tk.END, details)
        else:
            self.info_box.insert(tk.END, "No account found with this mobile number.")
        self.info_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAppGUI(root)
    root.mainloop()

```