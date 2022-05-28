import tkinter
import random
import tkinter.messagebox
import mysql.connector as m

mysql = m.connect()

root = tkinter.Tk()

root.configure(bg='#E8A87C')
root.geometry('500x300')
root.title('To-Do List')

tasks = []


# defining all functions
def clear_listbox():
    listbox_tasks.delete(0, "end")


def update_listbox():
    clear_listbox()
    for task in tasks:
        listbox_tasks.insert("end", task)


def add_task():
    task = text_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        lable_display['text'] = 'Task Added'
    else:
        tkinter.messagebox.showwarning('Warning', 'Please enter a task!')
    text_input.delete(0, 'end')


def delete_all():
    confirmation = tkinter.messagebox.askyesno('Warning!', 'Do you really want to delete all tasks?')
    if confirmation is True:
        global tasks
        tasks = []
        update_listbox()
        lable_display['text'] = 'All tasks are deleted!'
    else:
        lable_display['text'] = 'Tasks not deleted!'


def delete_one():
    task = listbox_tasks.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox()
    lable_display['text'] = 'Task Deleted'


def sort_asc():
    tasks.sort()
    update_listbox()
    lable_display['text'] = 'Tasks are sorted'


def sort_desc():
    tasks.sort(reverse=True)
    update_listbox()
    lable_display['text'] = 'Tasks are sorted'


def pick_random():
    task = random.choice(tasks)
    lable_display['text'] = task


def show_total_tasks():
    lable_display['text'] = 'Number of Tasks :- %s' % len(tasks)


# playing with the GUI to make buttons, labels, input and list boxes
# noinspection SpellCheckingInspection
lable_title = tkinter.Label(text="To-Do List", bg='#E8A87C', font=25)
lable_title.grid(row=0, column=1)

# noinspection SpellCheckingInspection
lable_display = tkinter.Label(text="Hello", fg='white', bg='indigo', font=25)
lable_display.grid(row=1, column=1)

text_input = tkinter.Entry(width=30)
text_input.grid(row=2, column=1)

# noinspection SpellCheckingInspection
btn_addtask = tkinter.Button(text="Add Task", fg='white', bg='red', font=25, command=add_task)
btn_addtask.grid(row=4, column=3)

btn_delete_all = tkinter.Button(text="Delete All Tasks", fg='white', bg='red', font=25, command=delete_all)
btn_delete_all.grid(row=5, column=3)

btn_delete_one = tkinter.Button(text="Delete", fg='white', bg='red', font=25, command=delete_one)
btn_delete_one.grid(row=4, column=0)

btn_sort_asc = tkinter.Button(text="Sort in Ascending", fg='white', bg='red', font=25, command=sort_asc)
btn_sort_asc.grid(row=5, column=0)

btn_sort_desc = tkinter.Button(text="Sort in Descending", fg='white', bg='red', font=25, command=sort_desc)
btn_sort_desc.grid(row=6, column=0)

btn_pick_random = tkinter.Button(text="Pick one random task", fg='white', bg='red', font=25, command=pick_random)
btn_pick_random.grid(row=6, column=3)

btn_total_tasks = tkinter.Button(text="Total Tasks", fg='white', bg='red', font=25, command=show_total_tasks)
btn_total_tasks.grid(row=7, column=0)

btn_exit = tkinter.Button(text="Quit", fg='white', bg='red', font=25, command=exit)
btn_exit.grid(row=7, column=3)

listbox_tasks = tkinter.Listbox(root)
listbox_tasks.grid(row=3, column=1, rowspan=7)

root.mainloop()
