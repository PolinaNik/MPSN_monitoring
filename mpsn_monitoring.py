import tkinter as tk
from tkinter import *
from tkinter import ttk
import datetime
import time
from time import gmtime, strftime
import subprocess
from threading import Thread
import os
import logging, logging.handlers
import tkinter.scrolledtext as scrolledtext
from tkcalendar import *
import collections
import pickle
#Мои модули
import dictionary

logit = logging.getLogger('logit')
handler = logging.handlers.RotatingFileHandler("moxa.log", maxBytes=20000, backupCount=5, mode = 'a')
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logging.Formatter.converter = time.gmtime
logit.addHandler(handler)

root = tk.Tk()
root.title("Мониторинг состояния каналов МПСН")

def insert_text():
    win = tk.Toplevel()
    win.wm_title("Просмотр лога")
    text = scrolledtext.ScrolledText(win)
    text.pack(expand=True, fill = 'both')
    with open('/sintez/sintez/moxa_monitoring/moxa.log', 'r') as log:
        file_log = log.readlines()
        text.delete(1.0, tk.END)
        for element in file_log:
            text.insert(tk.END, element)
    but = tk.Button(win, text='Закрыть лог', command =win.destroy, activebackground='salmon')
    but.pack()

menu_bar = tk.Menu(root)
menu_bar.add_command(label="Показать лог", command= lambda: insert_text())
menu_bar.add_command(label="Exit", command= lambda: root.destroy())
root.config(menu=menu_bar)


frame1 = tk.Frame(root, bg='gray64')
frame1.pack()
frame2 = tk.Frame(root, bg='gray64')
frame2.pack(side=LEFT)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="gray7",
                fieldbackground="gray7", foreground="white", font='Calibri 10', rowheight=20)
style.configure("Treeview.Heading", font='Calibri 10')

tree1 = ttk.Treeview(frame1)
tree1["columns"] = ("two", "three")
tree1.heading("#0", text="")
tree1.column("#0",minwidth=0,width=5, stretch=NO)
tree1.heading("three", text="State")
tree1.column("three",minwidth=0,width=150, stretch=YES)
tree1['height'] = 18
tree1.tag_configure('green', background='gray7', foreground='green2')
tree1.tag_configure('red', background='gray7', foreground='red2')
tree1.tag_configure('blue', background='gray7', foreground='RoyalBlue')
tree1.tag_configure('yellow', background='gray7', foreground='yellow')
tree1.tag_configure('ready', background='gray7', foreground='white')
tree1.pack(side=LEFT, anchor=SE)

tree2 = ttk.Treeview(frame2)
tree2["columns"] = ("two", "three")
tree2.heading("#0", text="")
tree2.column("#0",minwidth=0,width=5, stretch=NO)
tree2.heading("three", text="State")
tree2.column("three",minwidth=0,width=150, stretch=YES)
tree2['height'] = 10
tree2.tag_configure('green', background='gray7', foreground='green2')
tree2.tag_configure('red', background='gray7', foreground='red2')
tree2.tag_configure('blue', background='gray7', foreground='RoyalBlue')
tree2.tag_configure('yellow', background='gray7', foreground='yellow')
tree2.tag_configure('ready', background='gray7', foreground='white')
tree2.pack()

tree3 = ttk.Treeview(frame2)
tree3["columns"] = ("two", "three")
tree3.heading("#0", text="")
tree3.column("#0",minwidth=0,width=5, stretch=NO)
tree3.heading("three", text="State")
tree3.column("three",minwidth=0,width=150, stretch=YES)
tree3['height'] = 6
tree3.tag_configure('green', background='gray7', foreground='green2')
tree3.tag_configure('red', background='gray7', foreground='red2')
tree3.tag_configure('blue', background='gray7', foreground='RoyalBlue')
tree3.tag_configure('yellow', background='gray7', foreground='yellow')
tree3.tag_configure('ready', background='gray7', foreground='white')
tree3.pack()

tree4 = ttk.Treeview(frame2)
tree4["columns"] = ("two", "three")
tree4.heading("#0", text="")
tree4.column("#0",minwidth=0,width=5, stretch=NO)
tree4.heading("three", text="State")
tree4.column("three",minwidth=0,width=150, stretch=YES)
tree4['height'] = 3
tree4.tag_configure('green', background='gray7', foreground='green2')
tree4.tag_configure('red', background='gray7', foreground='red2')
tree4.tag_configure('blue', background='gray7', foreground='RoyalBlue')
tree4.tag_configure('yellow', background='gray7', foreground='yellow')
tree4.tag_configure('ready', background='gray7', foreground='white')
tree4.pack()

def insert_to_table(router, tree):
    for key in router.keys():
        tree.insert("", "end", values=(router[key], "<><><>"), tags = ("green", ))

insert_to_table(dictionary.router1, tree1)
insert_to_table(dictionary.router2, tree2)
insert_to_table(dictionary.router3, tree3)
insert_to_table(dictionary.router4, tree4)



root.mainloop()
