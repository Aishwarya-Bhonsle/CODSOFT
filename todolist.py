import tkinter as tk
from tkinter import messagebox
import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="#f0f0f0")  # Set background color of window

        self.tasks = []  # List to store tasks
        
        # Set up the window layout with a background color and font style
        self.task_entry = tk.Entry(self.root, width=40, bg="#ffffff", font=("Arial", 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=20, command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15, bg="#ffffff", font=("Arial", 12), selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=20, command=self.delete_task, bg="#f44336", fg="white", font=("Arial", 12))
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.mark_button = tk.Button(self.root, text="Mark as Completed", width=20, command=self.mark_completed, bg="#2196F3", fg="white", font=("Arial", 12))
        self.mark_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task_text = self.task_entry.get()
        if task_text != "":
            task = {"task": task_text, "completed": False}
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task!")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

    def mark_completed(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

    def update_task_list(self):
        """Updates the Listbox with the current tasks and tick marks for completed tasks."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["task"]
            if task["completed"]:
                task_text = f"✓ {task_text}"  # Add checkmark for completed tasks
            self.task_listbox.insert(tk.END, task_text)


# Create the main window
root = tk.Tk()

# Create an instance of the ToDoApp
todo_app = ToDoApp(root)

# Run the application
root.mainloop()
