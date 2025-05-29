import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(tk.END, f"[Done] {task}")
    else:
        messagebox.showwarning("Selection Error", "No task selected!")

# Main window
root = tk.Tk()
root.title("To-Do List")

# Entry widget for new task
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

done_button = tk.Button(button_frame, text="Mark as Done", command=mark_done)
done_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Listbox to show tasks
task_listbox = tk.Listbox(root, font=("Arial", 14), height=10)
task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
