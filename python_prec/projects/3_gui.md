## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class HotelRoom:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = str(room_number)
        self.room_type = room_type
        self.price = float(price_per_night)
        self.is_occupied = False
        self.guest_name = None

    def check_in(self, guest_name):
        if not self.is_occupied:
            self.is_occupied = True
            self.guest_name = guest_name
            return True, f"Room {self.room_number} checked in for {guest_name}."
        return False, f"Room {self.room_number} is already occupied!"

    def check_out(self):
        if self.is_occupied:
            g = self.guest_name
            self.is_occupied = False
            self.guest_name = None
            return True, f"Room {self.room_number} checked out. Guest was {g}."
        return False, f"Room {self.room_number} is already vacant."

class HotelAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management - CRUD GUI")
        self.root.geometry("720x520")
        self.root.configure(bg="#f1f5f9")

        self.rooms = [
            HotelRoom(101, "Standard Single", 99.00),
            HotelRoom(102, "Standard Double", 129.00),
            HotelRoom(201, "King Suite", 249.00)
        ]

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Hotel Reception Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f1f5f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inventory Table (Read)
        left_frame = ttk.LabelFrame(main_frame, text=" Room Directory ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.tree = ttk.Treeview(left_frame, columns=("Room", "Type", "Rate", "Status", "Guest"), show="headings", height=8)
        self.tree.heading("Room", text="Room #")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Rate", text="Rate ($)")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Guest", text="Guest Name")
        
        self.tree.column("Room", width=55, anchor=tk.CENTER)
        self.tree.column("Type", width=100)
        self.tree.column("Rate", width=65, anchor=tk.E)
        self.tree.column("Status", width=65, anchor=tk.CENTER)
        self.tree.column("Guest", width=85)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(left_frame, text="Refresh Rooms", command=self.update_display).pack(pady=5)

        # Right Frame: Actions (Create, Update, Delete)
        right_frame = ttk.LabelFrame(main_frame, text=" Front Desk Management ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        ttk.Label(right_frame, text="Room Number:").grid(row=0, column=0, sticky=tk.W, pady=6)
        self.r_num_ent = ttk.Entry(right_frame, width=20)
        self.r_num_ent.grid(row=0, column=1, sticky=tk.W, pady=6)

        ttk.Label(right_frame, text="Room Type / Guest Name:").grid(row=1, column=0, sticky=tk.W, pady=6)
        self.r_param_ent = ttk.Entry(right_frame, width=20)
        self.r_param_ent.grid(row=1, column=1, sticky=tk.W, pady=6)

        ttk.Label(right_frame, text="Price / Rate ($):").grid(row=2, column=0, sticky=tk.W, pady=6)
        self.r_price_ent = ttk.Entry(right_frame, width=20)
        self.r_price_ent.grid(row=2, column=1, sticky=tk.W, pady=6)

        btn_grid = ttk.Frame(right_frame)
        btn_grid.grid(row=3, column=0, columnspan=2, pady=15)

        ttk.Button(btn_grid, text="Add Room (Create)", command=self.handle_create).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Check-In", command=self.handle_checkin).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Check-Out", command=self.handle_checkout).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Delete Room", command=self.handle_delete).pack(side=tk.LEFT, padx=2)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.update_display()

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in self.rooms:
            status = "Occupied" if r.is_occupied else "Vacant"
            guest = r.guest_name if r.guest_name else "-"
            self.tree.insert("", tk.END, values=(r.room_number, r.room_type, f"{r.price:.2f}", status, guest))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            self.r_num_ent.delete(0, tk.END)
            self.r_num_ent.insert(0, vals[0])

    def find_room_obj(self, r_num):
        for r in self.rooms:
            if r.room_number == r_num:
                return r
        return None

    def handle_create(self):
        r_num = self.r_num_ent.get().strip()
        r_type = self.r_param_ent.get().strip()
        p_str = self.r_price_ent.get().strip()

        if not r_num or not r_type or not p_str:
            messagebox.showerror("Error", "All fields are required to add a room.")
            return
        if self.find_room_obj(r_num):
            messagebox.showerror("Error", "Room number already exists.")
            return
        try:
            price = float(p_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid price format.")
            return

        self.rooms.append(HotelRoom(r_num, r_type, price))
        self.update_display()
        messagebox.showinfo("Success", f"Room {r_num} added successfully.")

    def handle_checkin(self):
        r_num = self.r_num_ent.get().strip()
        guest = self.r_param_ent.get().strip()
        room = self.find_room_obj(r_num)
        if not room or not guest:
            messagebox.showerror("Error", "Valid room number and guest name required.")
            return

        success, msg = room.check_in(guest)
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_checkout(self):
        r_num = self.r_num_ent.get().strip()
        room = self.find_room_obj(r_num)
        if not room:
            messagebox.showerror("Error", "Room not found.")
            return

        success, msg = room.check_out()
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_delete(self):
        r_num = self.r_num_ent.get().strip()
        room = self.find_room_obj(r_num)
        if not room:
            messagebox.showerror("Error", "Room not found.")
            return
        if room.is_occupied:
            messagebox.showerror("Error", "Cannot delete an occupied room.")
            return

        self.rooms.remove(room)
        self.update_display()
        messagebox.showinfo("Success", f"Room {r_num} deleted from inventory.")

root = tk.Tk()
app = HotelAppGUI(root)
root.mainloop()

```