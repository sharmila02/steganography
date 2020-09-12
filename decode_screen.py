# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:50:35 2020

@author: Sharmila Siram
"""

import tkinter 
from tkinter import filedialog
import tkinter.messagebox

import stegan

decode_screen = tkinter.Tk()

decode_screen.geometry("250x190")
decode_screen.title("Decode")

label1=tkinter.Label(decode_screen,text="Decode the message!",font=40,bg='#ffffff',fg='#4fc3e3')
label1.pack()

bg_img=tkinter.PhotoImage(file="open_lock.png")
bg_label=tkinter.Label(image=bg_img)
bg_label.place(relwidth=1,relheight=1)

def open_file(): 
    file = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                      filetypes = (("jpeg files","*.jpg"),("png files","*.png"))) 
    return file

def secret_msg():
   tkinter.messagebox.showinfo( "Secret Message!", stegan.decode(open_file()))
   
encode_btn=tkinter.Button(decode_screen,text="Decode",font=20,bg='#ffffff',fg='#4fc3e3',
    activebackground='#4fc3e3',activeforeground='#ffffff', command = lambda:secret_msg())
encode_btn.place(x=70,y=150)

decode_screen.mainloop()