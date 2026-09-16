## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class RestaurantTable:
    def __init__(self, table_number, capacity):
        self.table_number = str(table_number)
        self.capacity = int(capacity)
        self.is_reserved = False
        self.guest_name = None

    def reserve_table(self, guest_name, party_size):
        if not self.is_reserved:
            if int(party_size) <= self.capacity:
                self.is_reserved = True
                self.guest_name = guest_name
                return True, f"Table {self.table_number} reserved for {guest_name}."
            return False, f"Party size exceeds table capacity ({self.capacity})."
        return False, f"Table {self.table_number} is already reserved!"

    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            self.guest_name = None
            return True, f"Reservation for Table {self.table_number} cancelled."
        return False, f"Table {self.table_number} is not reserved."

class RestaurantAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Reservation - CRUD GUI")
        self.root.geometry("740x520")
        self.root.configure(bg="#f8fafc")

        self.floor_plan = [
            RestaurantTable(1, 2),
            RestaurantTable(2, 4),
            RestaurantTable(3, 6),
            RestaurantTable(4, 8)
        ]

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Restaurant Host Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Host Controls
        left_frame = ttk.LabelFrame(main_frame, text=" Floor Controls ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        fields = ["Table Number:", "Capacity / Party Size:", "Guest Name:"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(left_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=6)
            ent = ttk.Entry(left_frame, width=20)
            ent.grid(row=i, column=1, sticky=tk.W, pady=6)
            self.entries[text] = ent

        btn_grid = ttk.Frame(left_frame)
        btn_grid.grid(row=len(fields), column=0, columnspan=2, pady=15)

        ttk.Button(btn_grid, text="Add Table", command=self.handle_create).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Reserve", command=self.handle_reserve).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Cancel", command=self.handle_cancel).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Delete", command=self.handle_delete).pack(side=tk.LEFT, padx=2)

        # Right Frame: Treeview Table Status
        right_frame = ttk.LabelFrame(main_frame, text=" Restaurant Floor Plan ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("Table", "Capacity", "Status", "Guest"), show="headings", height=8)
        self.tree.heading("Table", text="Table #")
        self.tree.heading("Capacity", text="Capacity")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Guest", text="Guest Name")
        
        self.tree.column("Table", width=65, anchor=tk.CENTER)
        self.tree.column("Capacity", width=70, anchor=tk.CENTER)
        self.tree.column("Status", width=80, anchor=tk.CENTER)
        self.tree.column("Guest", width=95)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(right_frame, text="Refresh Floor Plan", command=self.update_display).pack(pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.update_display()

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for t in self.floor_plan:
            status = "Reserved" if t.is_reserved else "Available"
            guest = t.guest_name if t.guest_name else "-"
            self.tree.insert("", tk.END, values=(t.table_number, t.capacity, status, guest))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            self.entries["Table Number:"].delete(0, tk.END)
            self.entries["Table Number:"].insert(0, vals[0])
            self.entries["Capacity / Party Size:"].delete(0, tk.END)
            self.entries["Capacity / Party Size:"].insert(0, vals[1])

    def find_table_obj(self, t_num):
        for t in self.floor_plan:
            if t.table_number == str(t_num):
                return t
        return None

    def handle_create(self):
        t_num = self.entries["Table Number:"].get().strip()
        cap_str = self.entries["Capacity / Party Size:"].get().strip()

        if not t_num or not cap_str:
            messagebox.showerror("Error", "Table number and capacity are required.")
            return
        if self.find_table_obj(t_num):
            messagebox.showerror("Error", "Table number already exists.")
            return

        try:
            cap = int(cap_str)
        except ValueError:
            messagebox.showerror("Error", "Capacity must be an integer.")
            return

        self.floor_plan.append(RestaurantTable(t_num, cap))
        self.update_display()
        messagebox.showinfo("Success", f"Table {t_num} added to floor plan.")

    def handle_reserve(self):
        t_num = self.entries["Table Number:"].get().strip()
        party_str = self.entries["Capacity / Party Size:"].get().strip()
        guest = self.entries["Guest Name:"].get().strip()
        table = self.find_table_obj(t_num)

        if not table or not party_str or not guest:
            messagebox.showerror("Error", "Table number, party size, and guest name are required.")
            return

        success, msg = table.reserve_table(guest, party_str)
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_cancel(self):
        t_num = self.entries["Table Number:"].get().strip()
        table = self.find_table_obj(t_num)
        if not table:
            messagebox.showerror("Error", "Table not found.")
            return

        success, msg = table.cancel_reservation()
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_delete(self):
        t_num = self.entries["Table Number:"].get().strip()
        table = self.find_table_obj(t_num)
        if not table:
            messagebox.showerror("Error", "Table not found.")
            return
        if table.is_reserved:
            messagebox.showerror("Error", "Cannot delete a table with an active reservation.")
            return

        self.floor_plan.remove(table)
        self.update_display()
        messagebox.showinfo("Success", f"Table {t_num} deleted from floor plan.")

root = tk.Tk()
app = RestaurantAppGUI(root)
root.mainloop()

```