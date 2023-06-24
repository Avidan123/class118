from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("disney")
root.geometry("400x400")

info={
      "story":"in a village there was a person who was not very rich",
      "character":"ramesh",
      "enemy":"rajesh"
      
          }
list1=[15000,10000,18000]

try:
    print(info["enem"])
    print(list1[10])
except KeyError:
    messagebox.showwarning("error","there was a keyerror")
except IndexError:
    messagebox.showinfo("error 2 ","another indexerror")

root.mainloop()

