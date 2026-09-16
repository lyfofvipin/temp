## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class MovieTicket:
    def __init__(self, booking_id, movie_title, seat_number, patron_name, price):
        self.booking_id = str(booking_id)
        self.movie_title = movie_title
        self.seat_number = str(seat_number)
        self.patron_name = patron_name
        self.price = float(price)

    def update_details(self, seat, patron):
        self.seat_number = str(seat)
        self.patron_name = patron

class MovieAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking - CRUD GUI")
        self.root.geometry("750x520")
        self.root.configure(bg="#f8fafc")

        self.bookings = [
            MovieTicket("B101", "Interstellar", "A-12", "Alice Smith", 14.50),
            MovieTicket("B102", "Inception", "B-05", "Bob Jones", 12.00)
        ]

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Cinema Box Office Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inputs & Control Panel
        left_frame = ttk.LabelFrame(main_frame, text=" Box Office Controls ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        fields = ["Booking ID:", "Movie Title:", "Seat Number:", "Patron Name:", "Price ($):"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(left_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=5)
            ent = ttk.Entry(left_frame, width=20)
            ent.grid(row=i, column=1, sticky=tk.W, pady=5)
            self.entries[text] = ent

        btn_grid = ttk.Frame(left_frame)
        btn_grid.grid(row=len(fields), column=0, columnspan=2, pady=12)

        ttk.Button(btn_grid, text="Book", command=self.handle_create).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Update", command=self.handle_update).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Cancel", command=self.handle_delete).pack(side=tk.LEFT, padx=2)

        # Right Frame: Treeview Booking Directory
        right_frame = ttk.LabelFrame(main_frame, text=" Active Bookings Directory ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("ID", "Movie", "Seat", "Patron", "Price"), show="headings", height=8)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Movie", text="Movie")
        self.tree.heading("Seat", text="Seat")
        self.tree.heading("Patron", text="Patron")
        self.tree.heading("Price", text="Price ($)")
        
        self.tree.column("ID", width=50, anchor=tk.CENTER)
        self.tree.column("Movie", width=100)
        self.tree.column("Seat", width=55, anchor=tk.CENTER)
        self.tree.column("Patron", width=85)
        self.tree.column("Price", width=60, anchor=tk.E)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(right_frame, text="Refresh Bookings", command=self.update_display).pack(pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.update_display()

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for b in self.bookings:
            self.tree.insert("", tk.END, values=(b.booking_id, b.movie_title, b.seat_number, b.patron_name, f"{b.price:.2f}"))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            keys = list(self.entries.keys())
            for i, val in enumerate(vals):
                if i < len(keys):
                    self.entries[keys[i]].delete(0, tk.END)
                    self.entries[keys[i]].insert(0, val)

    def find_booking_obj(self, b_id):
        for b in self.bookings:
            if b.booking_id == str(b_id):
                return b
        return None

    def handle_create(self):
        b_id = self.entries["Booking ID:"].get().strip()
        movie = self.entries["Movie Title:"].get().strip()
        seat = self.entries["Seat Number:"].get().strip()
        patron = self.entries["Patron Name:"].get().strip()
        p_str = self.entries["Price ($):"].get().strip()

        if not all([b_id, movie, seat, patron, p_str]):
            messagebox.showerror("Error", "All booking fields are required.")
            return
        if self.find_booking_obj(b_id):
            messagebox.showerror("Error", "Booking ID already exists.")
            return

        try:
            price = float(p_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid price number format.")
            return

        self.bookings.append(MovieTicket(b_id, movie, seat, patron, price))
        self.update_display()
        messagebox.showinfo("Success", f"Ticket booked for {patron}.")

    def handle_update(self):
        b_id = self.entries["Booking ID:"].get().strip()
        seat = self.entries["Seat Number:"].get().strip()
        patron = self.entries["Patron Name:"].get().strip()
        booking = self.find_booking_obj(b_id)

        if not booking or not seat or not patron:
            messagebox.showerror("Error", "Booking ID, Seat, and Patron name are required.")
            return

        booking.update_details(seat, patron)
        self.update_display()
        messagebox.showinfo("Success", f"Booking {b_id} updated successfully.")

    def handle_delete(self):
        b_id = self.entries["Booking ID:"].get().strip()
        booking = self.find_booking_obj(b_id)
        if not booking:
            messagebox.showerror("Error", "Booking ID not found.")
            return

        self.bookings.remove(booking)
        self.update_display()
        messagebox.showinfo("Success", f"Booking {b_id} cancelled.")

root = tk.Tk()
app = MovieAppGUI(root)
root.mainloop()

```