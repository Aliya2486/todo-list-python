import tkinter as tk
from tkinter import simpledialog, messagebox

tasks = []

def add_task():
     task = entry.get()
     if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.End)
     else:
         messagebox.showwarning("Input Error", "Please enter a task")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showinfo("Select a task", "Please select a task to delete.")

def edit_task():
    selected = listbox.curselection()
    if selected:
        current_task = tasks[selected[0]]
        new_task = simpledialog.askstring("Edit Task", "Modify your task:", initialvalue=current_task)
        if new_task:
            tasks[selected[0]] = new_task
            update_listbox()
    else:
        messagebox.showinfo("Select a task", "Please select a task to edit.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# GUI Setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack(pady=20)

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()