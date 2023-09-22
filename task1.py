from tkinter import *
import tkinter.font as font
root = Tk()
root.geometry("340x430")
root.title("SIMPLE CALCULATOR")
root.resizable(0, 0)
ip = StringVar()
fnt = font.Font(size=25)
scr = Entry(root, text=ip, width=30, justify='right', font=(10), bd=4)
scr.grid(row=0, columnspan=4, padx=15,pady=15, ipady=10)
 #list of button numbers
r= [["c","/","*","-"],
    ["9", "8","7", "+"],
    ["6", "5","4", "="],
    ["3", "2","1","0"]]
 
bt_dict = {}
ans = 0
def Calculate(event):
   btn= event.widget.cget("text")
   global r, ip, ans
   try:
      if btn == "c":  
            ip.set("")
      elif btn == "=":  
            ans= str(eval(ip.get()))
            ip.set(ans)
      else:
            ip.set(ip.get()+str(btn))
   except:
        ip.set("Invalid Operation")
 
for n in range(len(r)): 
    for m in range(len(r[n])): 
        bt_dict["btn_"+str(r[n][m])] = Button(
            root, bd=1, text=str(r[n][m]), font=fnt)
         
        bt_dict["btn_"+str(r[n][m])].grid(
        row=n+1, column=m, padx=5, pady=5, ipadx=5, ipady=5)
         
        bt_dict["btn_"+str(r[n][m])].bind('<Button-1>', Calculate)
 
root.mainloop()




