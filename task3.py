from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors game')
root.config(bg ='#12ccfd')
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'light green').pack()
user_take = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = '#D55bbD').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = user_take , bg = '#defcba').place(x=90 , y = 130)
comp_ch = random.randint(1,3)
if comp_ch== 1:
    comp_ch = 'rock'
elif comp_ch ==2:
    comp_ch = 'paper'
else:
    comp_ch = 'scissors'


Res = StringVar()
def play():
    user_ch = user_take.get()
    if user_ch == comp_ch:
        Res.set('tie,you both select same')
    elif user_ch == 'rock' and comp_ch == 'paper':
        Res.set('you loose,computer select paper')
    elif user_ch == 'rock' and comp_ch == 'scissors':
        Res.set('you win,computer select scissors')
    elif user_ch == 'paper' and comp_ch == 'scissors':
        Res.set('you loose,computer select scissors')
    elif user_ch == 'paper' and comp_ch == 'rock':
        Res.set('you win,computer select rock')
    elif user_ch == 'scissors' and comp_ch == 'rock':
        Res.set('you loose,computer select rock')
    elif user_ch == 'scissors' and comp_ch == 'paper':
        Res.set('you win ,computer select paper')
    else:
        Res.set("invalid: choose any one -- rock, paper, scissor")



def Exit():
    root.destroy()



Entry(root, font = 'arial 10 bold', textvariable = Res, bg ='yellow',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='#8902fd' ,command = play).place(x=150,y=190)
root.mainloop()
