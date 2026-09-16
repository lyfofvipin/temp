## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class ShoppingCart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = {}  # {item_name: price}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def update_item(self, item_name, price):
        if item_name in self.items:
            self.items[item_name] = price
            return True
        return False

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            return True
        return False

    def calculate_total(self, tax_rate=0.08):
        subtotal = sum(self.items.values())
        tax = subtotal * tax_rate
        total = subtotal + tax
        return subtotal, tax, total

class ShoppingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Commerce Storefront & Cart - CRUD GUI")
        self.root.geometry("700x520")
        self.root.configure(bg="#f8fafc")

        self.cart = ShoppingCart("Shopper_01")

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Online Retail Store & Cart (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inputs (Create / Update)
        left_frame = ttk.LabelFrame(main_frame, text=" Manage Cart Items ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        ttk.Label(left_frame, text="Product Name:").grid(row=0, column=0, sticky=tk.W, pady=8)
        self.name_ent = ttk.Entry(left_frame, width=22)
        self.name_ent.grid(row=0, column=1, sticky=tk.W, pady=8)

        ttk.Label(left_frame, text="Price ($):").grid(row=1, column=0, sticky=tk.W, pady=8)
        self.price_ent = ttk.Entry(left_frame, width=22)
        self.price_ent.grid(row=1, column=1, sticky=tk.W, pady=8)

        btn_frame = ttk.Frame(left_frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=15)

        ttk.Button(btn_frame, text="Add (Create)", command=self.handle_add).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_frame, text="Update Price", command=self.handle_update).pack(side=tk.LEFT, padx=3)
        ttk.Button(btn_frame, text="Remove (Delete)", command=self.handle_remove).pack(side=tk.LEFT, padx=3)

        # Right Frame: Cart Table (Read)
        right_frame = ttk.LabelFrame(main_frame, text=" Shopping Cart Summary ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("Item", "Price"), show="headings", height=8)
        self.tree.heading("Item", text="Product Name")
        self.tree.heading("Price", text="Price ($)")
        self.tree.column("Item", width=130)
        self.tree.column("Price", width=70, anchor=tk.E)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)

        self.total_lbl = ttk.Label(right_frame, text="Subtotal: $0.00 | Tax (8%): $0.00 | Total: $0.00", font=("Arial", 9, "bold"))
        self.total_lbl.pack(pady=8)

        ttk.Button(right_frame, text="Proceed to Checkout", command=self.handle_checkout).pack(pady=5)

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for name, price in self.cart.items.items():
            self.tree.insert("", tk.END, values=(name, f"{price:.2f}"))

        sub, tax, total = self.cart.calculate_total()
        self.total_lbl.config(text=f"Subtotal: ${sub:.2f} | Tax: ${tax:.2f} | Total: ${total:.2f}")

    def handle_add(self):
        name = self.name_ent.get().strip()
        p_str = self.price_ent.get().strip()
        if not name or not p_str:
            messagebox.showerror("Error", "Product name and price are required.")
            return
        try:
            price = float(p_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return

        self.cart.add_item(name, price)
        self.update_display()
        messagebox.showinfo("Success", f"Added '{name}' to cart.")
        self.name_ent.delete(0, tk.END)
        self.price_ent.delete(0, tk.END)

    def handle_update(self):
        name = self.name_ent.get().strip()
        p_str = self.price_ent.get().strip()
        if not name or not p_str:
            messagebox.showerror("Error", "Product name and new price are required.")
            return
        try:
            price = float(p_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return

        if self.cart.update_item(name, price):
            self.update_display()
            messagebox.showinfo("Success", f"Updated price for '{name}'.")
        else:
            messagebox.showerror("Error", "Item not found in cart.")

    def handle_remove(self):
        selected = self.tree.selection()
        if selected:
            item_name = self.tree.item(selected, "values")[0]
        else:
            item_name = self.name_ent.get().strip()

        if not item_name:
            messagebox.showerror("Error", "Select an item from the table or type its name to remove.")
            return

        if self.cart.remove_item(item_name):
            self.update_display()
            messagebox.showinfo("Success", f"Removed '{item_name}' from cart.")
        else:
            messagebox.showerror("Error", "Item not found in cart.")

    def handle_checkout(self):
        if not self.cart.items:
            messagebox.showwarning("Warning", "Your cart is empty.")
            return
        sub, tax, total = self.cart.calculate_total()
        messagebox.showinfo("Order Confirmation", f"Order placed successfully!\n\nSubtotal: ${sub:.2f}\nTax: ${tax:.2f}\nTotal Billed: ${total:.2f}")
        self.cart.items.clear()
        self.update_display()

root = tk.Tk()
app = ShoppingAppGUI(root)
root.mainloop()

```