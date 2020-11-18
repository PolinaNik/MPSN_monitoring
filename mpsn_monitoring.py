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
        tree.insert("", "end", values=(router[key][0], "<><><>"), tags = ("green", ))

insert_to_table(dictionary.router1, tree1)
insert_to_table(dictionary.router2, tree2)
insert_to_table(dictionary.router3, tree3)
insert_to_table(dictionary.router4, tree4)

def mpsn_func(ip, tree, name, moxa, rx, tx,  updatetime, IT, add_in_table, rem_num):
    curenttime = datetime.datetime.today()
    text = "%s %s" %(name, strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    tree.heading("two", text=text)
    tree.column("two",minwidth=0,width=210, stretch=NO)
    remember = []
    upd_file = open("/sintez/sintez/moxa_monitoring/parameters/updatetime%s.pkl" %rem_num, "rb")
    updatetime = pickle.load(upd_file)
    upd_file.close()
    rx_file = open("/sintez/sintez/moxa_monitoring/parameters/rx%s.pkl" %rem_num, "rb")
    rx = pickle.load(rx_file)
    rx_file.close()
    tx_file = open("/sintez/sintez/moxa_monitoring/parameters/tx%s.pkl" %rem_num, "rb")
    tx = pickle.load(tx_file)
    tx_file.close()
    for key in moxa.keys():
        port = key+1
        curentrx = subprocess.check_output(['snmpget', '-c', 'public', '-v', '2c', '-O', 'qv', '%s' % ip, '.1.3.6.1.2.1.2.2.1.10.%s' % port]).rstrip()
        curenttx = subprocess.check_output(['snmpget', '-c', 'public', '-v', '2c', '-O', 'qv', '%s' % ip, '.1.3.6.1.2.1.2.2.1.16.%s' % port]).rstrip()
        if curentrx != rx[key] or curenttx != tx[key]:
            updatetime[key] = curenttime
            rx[key] = curentrx
            tx[key] = curenttx
            rx_file = open("/sintez/sintez/moxa_monitoring/parameters/rx%s.pkl" %rem_num, "wb")
            pickle.dump(rx, rx_file)
            rx_file.close()
            tx_file = open("/sintez/sintez/moxa_monitoring/parameters/tx%s.pkl" %rem_num, "wb")
            pickle.dump(tx, tx_file)
            tx_file.close()
            if curenttx != '0' and curentrx != '0':
                state = '<<< >>>'
                remember.append(key)
                lst = [key, moxa[key], state, 'green']
                d = {key: lst}
                add_in_table.update(d)
                upd_file = open("/sintez/sintez/moxa_monitoring/parameters/updatetime%s.pkl" %rem_num, "wb")
                pickle.dump(updatetime, upd_file)
                upd_file.close()
            if curentrx != '0' and key not in remember:
                state = '<<<'
                lst = [key, moxa[key], state, 'green']
                d = {key: lst}
                add_in_table.update(d)
                upd_file = open("/sintez/sintez/moxa_monitoring/parameters/updatetime%s.pkl" %rem_num, "wb")
                pickle.dump(updatetime, upd_file)
                upd_file.close()
            if curenttx != '0' and key not in remember:
                state = '>>>'
                lst = [key, moxa[key], state, 'green']
                d = {key: lst}
                add_in_table.update(d)
                upd_file = open("/sintez/sintez/moxa_monitoring/parameters/updatetime%s.pkl" %rem_num, "wb")
                pickle.dump(updatetime, upd_file)
                upd_file.close()
	    IT[key] = curenttime - updatetime[key]
        if IT[key] > datetime.timedelta(minutes=1) and IT[key] < datetime.timedelta(hours=12) and  moxa[key] !="":
            upd_file = open("/sintez/sintez/moxa_monitoring/parameters/updatetime%s.pkl" %rem_num, "wb")
            pickle.dump(updatetime, upd_file)
            upd_file.close()
            state = str(updatetime[key]).split(".")[0]
            lst = [key, moxa[key], state, 'red']
            d = {key: lst}
            add_in_table.update(d)
        if IT[key] > datetime.timedelta(hours=12) and  moxa[key] !="":
            state = str(updatetime[key]).split(".")[0]
            lst = [key, moxa[key], state, 'yellow']
            d = {key: lst}
            add_in_table.update(d)
        if moxa[key] == "":
            lst = [key, "", "", 'green']
            d = {key: lst}
            add_in_table.update(d)
        if datetime.timedelta(minutes=2) < IT[key] < datetime.timedelta(minutes =3) and moxa[key] != "" and moxa[key] !="Объединенная РЛИ для ВЕГА" :
            logit.warning('%s - %s пропал. Время пропадания - %s' %(name, moxa[key], updatetime[key].replace(microsecond=0)))
            os.system('/opt/csw/bin/mpg123 /sintez/sintez/moxa_monitoring/sound.mp3')
        if datetime.timedelta(minutes=30) < IT[key] < datetime.timedelta(minutes =31) and  moxa[key] =="Объединенная РЛИ для ВЕГА" :
            logit.warning('%s - %s пропал. Время пропадания - %s' %(name, moxa[key], updatetime[key].replace(microsecond=0)))
            os.system('/opt/csw/bin/mpg123 /sintez/sintez/moxa_monitoring/sound.mp3')
    add_in_table = collections.OrderedDict(sorted(add_in_table.items()))
    for key in add_in_table.keys():
	    num = key -1
            r = tree.get_children()[num]
            tree.item(r, values=(str(add_in_table[key][0]), str(add_in_table[key][1]), str(add_in_table[key][2])), tags=(add_in_table[key][3],))

def clean_func5():
    while True:
        try:
            moxa_func('moxa1', tree5, "MOXA-5", values.moxa5, values.rx5, values.tx5, values.updatetime5, values.IT5,
                      values.add_in_table5, 5)
            time.sleep(a)
        except:
            pass


root.mainloop()
