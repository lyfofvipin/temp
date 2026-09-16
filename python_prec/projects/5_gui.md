## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = str(isbn)
        self.is_borrowed = False
        self.borrower = None

    def borrow_book(self, patron_name):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrower = patron_name
            return True, f"'{self.title}' checked out to {patron_name}."
        return False, f"'{self.title}' is already checked out!"

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrower = None
            return True, f"'{self.title}' returned successfully."
        return False, f"'{self.title}' was not checked out."

class LibraryAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management - CRUD GUI")
        self.root.geometry("740x520")
        self.root.configure(bg="#f8fafc")

        self.catalog = [
            Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565"),
            Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"),
            Book("1984", "George Orwell", "9780451524935")
        ]

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="Library Catalog Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inputs & Actions
        left_frame = ttk.LabelFrame(main_frame, text=" Book Operations ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        fields = ["Title:", "Author:", "ISBN:", "Patron Name:"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(left_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=6)
            ent = ttk.Entry(left_frame, width=20)
            ent.grid(row=i, column=1, sticky=tk.W, pady=6)
            self.entries[text] = ent

        btn_grid = ttk.Frame(left_frame)
        btn_grid.grid(row=len(fields), column=0, columnspan=2, pady=15)

        ttk.Button(btn_grid, text="Add Book", command=self.handle_create).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Check Out", command=self.handle_borrow).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Return", command=self.handle_return).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Delete", command=self.handle_delete).pack(side=tk.LEFT, padx=2)

        # Right Frame: Treeview Catalog View
        right_frame = ttk.LabelFrame(main_frame, text=" Library Book Catalog ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("ISBN", "Title", "Author", "Status", "Borrower"), show="headings", height=8)
        self.tree.heading("ISBN", text="ISBN")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Author", text="Author")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Borrower", text="Borrower")
        
        self.tree.column("ISBN", width=95)
        self.tree.column("Title", width=110)
        self.tree.column("Author", width=90)
        self.tree.column("Status", width=70, anchor=tk.CENTER)
        self.tree.column("Borrower", width=75)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(right_frame, text="Refresh Catalog", command=self.update_display).pack(pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.update_display()

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for b in self.catalog:
            status = "Borrowed" if b.is_borrowed else "Available"
            borrower_name = b.borrower if b.borrower else "-"
            self.tree.insert("", tk.END, values=(b.isbn, b.title, b.author, status, borrower_name))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            self.entries["ISBN:"].delete(0, tk.END)
            self.entries["ISBN:"].insert(0, vals[0])
            self.entries["Title:"].delete(0, tk.END)
            self.entries["Title:"].insert(0, vals[1])
            self.entries["Author:"].delete(0, tk.END)
            self.entries["Author:"].insert(0, vals[2])

    def find_book_obj(self, isbn):
        for b in self.catalog:
            if b.isbn == isbn:
                return b
        return None

    def handle_create(self):
        title = self.entries["Title:"].get().strip()
        author = self.entries["Author:"].get().strip()
        isbn = self.entries["ISBN:"].get().strip()

        if not all([title, author, isbn]):
            messagebox.showerror("Error", "All book fields are required.")
            return
        if self.find_book_obj(isbn):
            messagebox.showerror("Error", "A book with this ISBN already exists.")
            return

        self.catalog.append(Book(title, author, isbn))
        self.update_display()
        messagebox.showinfo("Success", f"'{title}' added to library catalog.")

    def handle_borrow(self):
        isbn = self.entries["ISBN:"].get().strip()
        patron = self.entries["Patron Name:"].get().strip()
        book = self.find_book_obj(isbn)
        if not book or not patron:
            messagebox.showerror("Error", "Valid ISBN and patron name are required.")
            return

        success, msg = book.borrow_book(patron)
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_return(self):
        isbn = self.entries["ISBN:"].get().strip()
        book = self.find_book_obj(isbn)
        if not book:
            messagebox.showerror("Error", "Book not found.")
            return

        success, msg = book.return_book()
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_delete(self):
        isbn = self.entries["ISBN:"].get().strip()
        book = self.find_book_obj(isbn)
        if not book:
            messagebox.showerror("Error", "Book not found.")
            return
        if book.is_borrowed:
            messagebox.showerror("Error", "Cannot delete a book that is checked out.")
            return

        self.catalog.remove(book)
        self.update_display()
        messagebox.showinfo("Success", f"Book ISBN {isbn} deleted.")

root = tk.Tk()
app = LibraryAppGUI(root)
root.mainloop()

```