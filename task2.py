from tkinter import *
from tkinter import messagebox

def newTask():
    task = e.get()
    if task != "":
        lb.insert(END, task)
        e.delete(0, "end")
    else:
        messagebox.showwarning("warning", "PLEASE ENTER TASK")

def deleteTask():
    lb.delete(ANCHOR)

rutu = Tk()
rutu.geometry('500x450+500+200')
rutu.title('To-Do List')
rutu.config(bg='cyan')
rutu.resizable(width=True, height=False)

frame = Frame(rutu)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='purple',
    highlightthickness=0,
    selectbackground='yellow',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

taskList = [
    'WAKE UP',
    'DRINK WATER',
    'GO to walking',
    'STUDY',
    'READY FOR COLLEGE',
    'GO TO COLLEGE',
    'LEARN SOMETHING',
    ]

for item in taskList:
    lb.insert(END, item)

sc= Scrollbar(frame)
sc.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sc.set)
sc.config(command=lb.yview)

e = Entry(
    rutu,
    font=('times', 24)
    )

e.pack(pady=20)

btnFrame = Frame(rutu)
btnFrame.pack(pady=20)

addBtn = Button(
    btnFrame,
    text='ADD',
    font=('times 14'),
    bg='green',
    padx=20,
    pady=10,
    command=newTask
)
addBtn.pack(fill=BOTH, expand=True, side=RIGHT)

delBtn = Button(
    btnFrame,
    text='DELETE',
    font=('times 14'),
    bg='blue',
    padx=20,
    pady=10,
    command=deleteTask
)
delBtn.pack(fill=BOTH, expand=True, side=RIGHT)


rutu.mainloop()
