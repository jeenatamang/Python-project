import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry 


root = tk.Tk()
root.title("Task Manager")


root.config(bg="lightblue")
root.geometry("500x500")


task_entry = tk.Entry(root, width=40, bg="white", fg="black", font=("comic sans", 12))
task_entry.pack(pady=10)


priority_var = tk.StringVar(root)
priority_var.set("Low")  # Default value
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.pack(pady=5)


due_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
due_date_entry.pack(pady=5)


tasks = tk.Listbox(root, width=70, height=10, bg="white", fg="black", font=("comic sans", 12))
tasks.pack(pady=10)


def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()

    if task:
        task_string = f"{task} | Priority: {priority} | Due: {due_date}"
        tasks.insert(tk.END, task_string)
        task_entry.delete(0, tk.END)  # Clear the task entry
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Define remove_task function to remove the selected task
def remove_task():
    try:
        task_index = tasks.curselection()[0]
        tasks.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to remove.")


def mark_task():
    try:
        task_index = tasks.curselection()[0]
        task = tasks.get(task_index)
        tasks.delete(task_index)
        tasks.insert(tk.END, task + " (Done)")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as done.")


button_style = {"bg": "lightgray", "fg": "black", "font": ("Arial", 10), "borderwidth": 2}


add_button = tk.Button(root, text="Add Task", command=add_task, **button_style)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, **button_style)
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark Task as Done", command=mark_task, **button_style)
mark_button.pack(pady=5)


root.mainloop()
