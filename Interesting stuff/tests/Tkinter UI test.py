
from tkinter import *


root = Tk()  # nnotre main (principal)  window / frame
root.title("Application sécurisée")
#root.iconbitmap('')
xcoos = int(root.winfo_screenwidth()/1.3)
ycoos = int(root.winfo_screenheight()/1.3)
root.geometry("{}x{}".format(xcoos, ycoos))


frame_images = Frame(root, padx=250, pady=200, borderwidth=5, background=None, relief="sunken")
frame_buttons = Frame(root, padx=150, pady=200, bd=5, bg=None, relief="sunken")

frame_images.grid(row=0, column=0)
frame_buttons.grid(row=0, column=1)


label_1 = Label(frame_images, text="Display and Show here")
label_1.pack()

def cmd_1():
    global label_1
    label_1.pack_forget()
    label_1 = Label(frame_images, text="AAA")
    label_1.pack()

def cmd_2():
    global label_1
    label_1.pack_forget()
    label_1 = Label(frame_images, text="FFF")
    label_1.pack()

def cmd_3():
    global label_1
    label_1.pack_forget()
    label_1 = Label(frame_images, text="Show")
    label_1.pack()

def cmd_4():
    global label_1
    label_1.pack_forget()
    label_1 = Label(frame_images, text="Display")
    label_1.pack()

label_2 = Label(frame_buttons, text="b")
button_1 = Button(frame_buttons, text="Display AAA", command=cmd_1)
button_2 = Button(frame_buttons, text="Show FFF", command=cmd_2)
button_3 = Button(frame_buttons, text="Display Show", command=cmd_3)
button_4 = Button(frame_buttons, text="Show Display", command=cmd_4)


label_2.grid(row=0, column=0, columnspan=4)
button_1.grid(row=0, column=0)
button_2.grid(row=0, column=1)
button_3.grid(row=0, column=2)
button_4.grid(row=0, column=3)


root.mainloop()
