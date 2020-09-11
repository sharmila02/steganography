# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:43:56 2020

@author: DELL
"""

import tkinter as tk
window=tk.Tk()
window.title("Steganography")
canvas=tk.Canvas(window,height=300,width=300,bg='#631b19')
canvas.pack(fill="both")
bg_img=tk.PhotoImage(file="onlyone.png")
bg_label=tk.Label(image=bg_img)
bg_label.place(relwidth=1,relheight=1)
#frame=tk.Frame(window,height=250,width=250,bg='#b5807f')
#frame.place(x=30,y=30)
#label1=tk.Label(window,text="Welcome!",font=40,bg='#ffffff',fg='#4fc3e3')
#label1.place(x=100,y=0)
label1=tk.Label(window,text="Welcome!",font=40,bg='#ffffff',fg='#4fc3e3')
label1.place(x=100,y=0)
label2=tk.Label(text="Please choose",font=10,bg='#ffffff',fg='#4fc3e3')
label2.place(x=80,y=40)
button1=tk.Button(window,text="Encode",font=40,bg='#ffffff',fg='#4fc3e3',activebackground='#4fc3e3',activeforeground='#ffffff')
button1.place(x=40,y=240)
button2=tk.Button(window,text="Decode",font=40,bg='#ffffff',fg='#4fc3e3',activebackground='#4fc3e3',activeforeground='#ffffff')
button2.place(x=180,y=240)
#bg_img=tk.PhotoImage(file="project.png")
#bg_label=tk.Label(image=bg_img)
#bg_label.place(relwidth=1,relheight=1)
window.mainloop()