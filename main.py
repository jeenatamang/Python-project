import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry 


root = tk.Tk()
root.title("Task Manager")


root.config(bg="lightblue")
root.geometry("500x500")
placeholder = "Hello! Enter your task here"


task_entry = tk.Entry(root, width=40, bg="white", fg="black", font=("comic sans", 12))
task_entry.insert(0, placeholder)
task_entry.pack(pady=10)


def on_entry_click(event):
    if task_entry.get() == placeholder:
        task_entry.delete(0, tk.END) 
        task_entry.config(fg='black')


def on_focusout(event):
    if task_entry.get() == '':
        task_entry.insert(0, placeholder)
        task_entry.config(fg='grey')

task_entry.bind('<FocusIn>', on_entry_click)
task_entry.bind('<FocusOut>', on_focusout)

priority_var = tk.StringVar(root)
priority_var.set("Low")  
priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
priority_menu.pack(pady=5)


due_date_entry = DateEntry(root, width=12, background='red', foreground='white', borderwidth=2)
due_date_entry.pack(pady=5)


tasks = tk.Listbox(root, width=70, height=10, bg="white", fg="black", font=("comic sans", 12))
tasks.pack(pady=10)


def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()

    if task and task != placeholder:
        task_string = f"{task} | Priority: {priority} | Due: {due_date}"
        tasks.insert(tk.END, task_string)
        task_entry.delete(0, tk.END)
        task_entry.config(fg='black')
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


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


button_style = {"bg": "lightgray", "fg": "black", "font": ("Comic sans", 10), "borderwidth": 2}


add_button = tk.Button(root, text="Add a Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 10), borderwidth=2) 
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove a Task", command=remove_task, bg="red", fg="white", font=("Arial", 10))
remove_button.pack(pady=5)

mark_button = tk.Button(root, text="Mark Task as Done", command=mark_task, bg="white", fg="black", font=("Arial", 10), borderwidth=2)
mark_button.pack(pady=5)


root.mainloop()
