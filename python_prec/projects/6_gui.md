## Tkinter GUI Application Implementation (Full CRUD)

```python
import tkinter as tk
from tkinter import messagebox, ttk

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = str(student_id)
        self.grades = {}  # {subject: score}

    def add_grade(self, subject, score):
        try:
            val = float(score)
            if 0 <= val <= 100:
                self.grades[subject] = val
                return True, f"Grade recorded for {subject}."
            return False, "Score must be between 0 and 100."
        except ValueError:
            return False, "Invalid score number format."

    def remove_grade(self, subject):
        if subject in self.grades:
            del self.grades[subject]
            return True, f"Subject {subject} removed."
        return False, "Subject not found."

    def calculate_gpa(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class StudentAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Management - CRUD GUI")
        self.root.geometry("750x520")
        self.root.configure(bg="#f8fafc")

        self.database = [
            Student("Alice Cooper", "S101"),
            Student("Bob Smith", "S102")
        ]

        header = tk.Frame(self.root, bg="#0f172a", height=60)
        header.pack(fill=tk.X)
        tk.Label(header, text="University Student Portal (CRUD)", fg="white", bg="#0f172a", font=("Arial", 15, "bold")).pack(pady=15)

        main_frame = tk.Frame(self.root, bg="#f8fafc")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Left Frame: Inputs & Control Panel
        left_frame = ttk.LabelFrame(main_frame, text=" Academic Controls ", padding=15)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        fields = ["Student ID:", "Student Name:", "Subject Name:", "Score (0-100):"]
        self.entries = {}

        for i, text in enumerate(fields):
            ttk.Label(left_frame, text=text).grid(row=i, column=0, sticky=tk.W, pady=6)
            ent = ttk.Entry(left_frame, width=20)
            ent.grid(row=i, column=1, sticky=tk.W, pady=6)
            self.entries[text] = ent

        btn_grid = ttk.Frame(left_frame)
        btn_grid.grid(row=len(fields), column=0, columnspan=2, pady=15)

        ttk.Button(btn_grid, text="Enroll", command=self.handle_enroll).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Add/Update", command=self.handle_grade).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Del Sub", command=self.handle_del_subject).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_grid, text="Exp Student", command=self.handle_delete_student).pack(side=tk.LEFT, padx=2)

        # Right Frame: Treeview Database View
        right_frame = ttk.LabelFrame(main_frame, text=" Enrolled Students Directory ", padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(right_frame, columns=("ID", "Name", "Subjects Count", "GPA"), show="headings", height=8)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Student Name")
        self.tree.heading("Subjects Count", text="Subjects")
        self.tree.heading("GPA", text="GPA (%)")
        
        self.tree.column("ID", width=65, anchor=tk.CENTER)
        self.tree.column("Name", width=110)
        self.tree.column("Subjects Count", width=65, anchor=tk.CENTER)
        self.tree.column("GPA", width=65, anchor=tk.E)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=8)

        ttk.Button(right_frame, text="Refresh Directory", command=self.update_display).pack(pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.update_display()

    def update_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for s in self.database:
            gpa = s.calculate_gpa()
            self.tree.insert("", tk.END, values=(s.student_id, s.name, len(s.grades), f"{gpa:.2f}"))

    def on_select(self, event):
        selected = self.tree.selection()
        if selected:
            vals = self.tree.item(selected, "values")
            self.entries["Student ID:"].delete(0, tk.END)
            self.entries["Student ID:"].insert(0, vals[0])
            self.entries["Student Name:"].delete(0, tk.END)
            self.entries["Student Name:"].insert(0, vals[1])

    def find_student_obj(self, s_id):
        for s in self.database:
            if s.student_id == s_id:
                return s
        return None

    def handle_enroll(self):
        s_id = self.entries["Student ID:"].get().strip()
        name = self.entries["Student Name:"].get().strip()

        if not all([s_id, name]):
            messagebox.showerror("Error", "Student ID and Name are required.")
            return
        if self.find_student_obj(s_id):
            messagebox.showerror("Error", "Student ID already exists.")
            return

        self.database.append(Student(name, s_id))
        self.update_display()
        messagebox.showinfo("Success", f"Enrolled student {name}.")

    def handle_grade(self):
        s_id = self.entries["Student ID:"].get().strip()
        sub = self.entries["Subject Name:"].get().strip()
        score_str = self.entries["Score (0-100):"].get().strip()
        student = self.find_student_obj(s_id)

        if not student or not sub or not score_str:
            messagebox.showerror("Error", "Student ID, Subject name, and Score are required.")
            return

        success, msg = student.add_grade(sub, score_str)
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_del_subject(self):
        s_id = self.entries["Student ID:"].get().strip()
        sub = self.entries["Subject Name:"].get().strip()
        student = self.find_student_obj(s_id)
        if not student or not sub:
            messagebox.showerror("Error", "Student ID and Subject name are required.")
            return

        success, msg = student.remove_grade(sub)
        if success:
            messagebox.showinfo("Success", msg)
            self.update_display()
        else:
            messagebox.showwarning("Warning", msg)

    def handle_delete_student(self):
        s_id = self.entries["Student ID:"].get().strip()
        student = self.find_student_obj(s_id)
        if not student:
            messagebox.showerror("Error", "Student ID not found.")
            return

        self.database.remove(student)
        self.update_display()
        messagebox.showinfo("Success", f"Student ID {s_id} record removed.")

root = tk.Tk()
app = StudentAppGUI(root)
root.mainloop()

```