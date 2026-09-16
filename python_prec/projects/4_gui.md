## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class RideRequest:
    def __init__(self, rider_name, pickup_location, dropoff_location):
        self.rider = rider_name
        self.pickup = pickup_location
        self.dropoff = dropoff_location
        self.driver = None
        self.status = "Searching for driver"

    def assign_driver(self, driver_name):
        self.driver = driver_name
        self.status = "Driver en route"

    def update_dropoff(self, new_dropoff):
        self.dropoff = new_dropoff

    def complete_ride(self, distance_miles):
        self.status = "Completed"
        fare = 2.50 + (float(distance_miles) * 1.75)
        return fare

class RideAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ride-Sharing Dispatch System - CRUD GUI")
        self.root.geometry("720x520")
        self.root.configure(bg="#f8fafc")

        self.rides = []

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Ride-Sharing Dispatch Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inputs (Create / Update)
        left_frame = ttk.LabelFrame(main_frame, text=" Trip Control Panel ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        fields = ["Rider Name:", "Pickup Location:", "Dropoff Location:", "Driver / Miles:"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(left_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=6)
            ent = ttk.Entry(left_frame, width=20)
            ent.grid(row=i, column=1, sticky=tk.W, pady=6)
            self.entries[text] = ent

        btn_grid = ttk.Frame(left_frame)
        btn_grid.grid(row=len(fields), column=0, columnspan=2, pady=15)

        ttk.Button(btn_grid, text="Request (Create)", command=self.handle_create).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Assign Driver", command=self.handle_assign).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Complete", command=self.handle_complete).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Cancel", command=self.handle_delete).pack(side=tk.LEFT, padx=2)

        # Right Frame: Active Rides Treeview (Read)
        right_frame = ttk.LabelFrame(main_frame, text=" Active Rides Directory ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("Rider", "Pickup", "Dropoff", "Driver", "Status"), show="headings", height=8)
        self.tree.heading("Rider", text="Rider")
        self.tree.heading("Pickup", text="Pickup")
        self.tree.heading("Dropoff", text="Dropoff")
        self.tree.heading("Driver", text="Driver")
        self.tree.heading("Status", text="Status")
        
        self.tree.column("Rider", width=80)
        self.tree.column("Pickup", width=80)
        self.tree.column("Dropoff", width=80)
        self.tree.column("Driver", width=70)
        self.tree.column("Status", width=100)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(right_frame, text="Refresh Rides List", command=self.update_display).pack(pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in self.rides:
            driver_name = r.driver if r.driver else "-"
            self.tree.insert("", tk.END, values=(r.rider, r.pickup, r.dropoff, driver_name, r.status))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            self.entries["Rider Name:"].delete(0, tk.END)
            self.entries["Rider Name:"].insert(0, vals[0])

    def find_ride_obj(self, rider_name):
        for r in self.rides:
            if r.rider.lower() == rider_name.lower():
                return r
        return None

    def handle_create(self):
        rider = self.entries["Rider Name:"].get().strip()
        pickup = self.entries["Pickup Location:"].get().strip()
        dropoff = self.entries["Dropoff Location:"].get().strip()

        if not all([rider, pickup, dropoff]):
            messagebox.showerror("Error", "Rider, pickup, and dropoff are required.")
            return
        if self.find_ride_obj(rider):
            messagebox.showerror("Error", "An active ride already exists for this rider.")
            return

        self.rides.append(RideRequest(rider, pickup, dropoff))
        self.update_display()
        messagebox.showinfo("Success", f"Ride requested for {rider}.")

    def handle_assign(self):
        rider = self.entries["Rider Name:"].get().strip()
        driver = self.entries["Driver / Miles:"].get().strip()
        ride = self.find_ride_obj(rider)
        if not ride or not driver:
            messagebox.showerror("Error", "Rider name and driver name required.")
            return

        ride.assign_driver(driver)
        self.update_display()
        messagebox.showinfo("Success", f"Driver {driver} assigned to {rider}.")

    def handle_complete(self):
        rider = self.entries["Rider Name:"].get().strip()
        miles_str = self.entries["Driver / Miles:"].get().strip()
        ride = self.find_ride_obj(rider)
        if not ride or not miles_str:
            messagebox.showerror("Error", "Rider name and distance in miles required.")
            return

        try:
            miles = float(miles_str)
        except ValueError:
            messagebox.showerror("Error", "Invalid distance number format.")
            return

        fare = ride.complete_ride(miles)
        self.update_display()
        messagebox.showinfo("Ride Complete", f"Trip finished!\nBilled fare to {rider}: ${fare:.2f}")

    def handle_delete(self):
        rider = self.entries["Rider Name:"].get().strip()
        ride = self.find_ride_obj(rider)
        if not ride:
            messagebox.showerror("Error", "Active ride not found.")
            return

        self.rides.remove(ride)
        self.update_display()
        messagebox.showinfo("Success", f"Ride request for {rider} cancelled.")

root = tk.Tk()
app = RideAppGUI(root)
root.mainloop()

```