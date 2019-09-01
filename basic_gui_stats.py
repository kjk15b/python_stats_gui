#!/bin/python3

'''
Author:	Kolby Kiesling
	kjk15b@acu.edu

For:	Carolina Ramirez

This program serves as a simple
calculator that finds the statistics
of given data sets.	
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np


data_array = list()


data_message = ""

pop_made = False


c_transform = 'na'
        
        
def show_stats(*args):
    try:
        global c_transform
        var = str(transform.get())
        if var != c_transform:
            msg = "////\n" + str(var) + " ////\n"
            dlist.insert(END, msg, '')
            c_transform = var
        std.set(np.std(data_array))
        avg.set(np.average(data_array))
        mx.set(np.amax(data_array))
        mn.set(np.amin(data_array))
        variance.set(np.var(data_array))
        co_var.set(np.std(data_array) / np.average(data_array) * 100)
        med.set(np.median(data_array))
        mn.set(np.amin(data_array))
        points.set(len(data_array))
        
    except ValueError:
        pass
    
    
def show_plot(*args):
    try:
        var = int(mute.get())
        if var > 0:
            ttl = str(title.get())
            yax = str(ylabel.get())
            xax = str(xlabel.get())
            plt.figure(1)
            fig, ax = plt.subplots()
            ax.hist(data_array)
            plt.xlabel(xax)
            plt.title(ttl)
            plt.ylabel(yax)
            textstr = '\n'.join((
                r'$\mathrm{median}=%.2f$' % (np.median(data_array), ),
                r'$\mathrm{average}=%.2f$' % (np.average(data_array), ),
                r'$\sigma=%.2f$' % (np.std(data_array), )))
    
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
            plt.pause(0.5)   
    
    except ValueError:
        pass

def clear_data(*args):
    dlist.insert(END, "----------\nCLEARED\n----------\n", '')
        
    data_array.clear()
    print(data_array)
    std.set(0)
    avg.set(0)
    mx.set(0)
    mx.set(0)
    variance.set(0)
    co_var.set(0)
    med.set(0)
    mn.set(0)
    points.set(0)
    data_message = ""
    
def save_data(*args):
    try:
        name = str(filename.get())
        fname = name + ".csv"
        r = open(fname, "w")
        for i in range(len(data_array)):
            line = str(data_array[i]) + "\n"
            r.write(line)
            print(".")
        data_file.set(str(fname) + ".csv")
    
    except ValueError:
        pass

def add_data(*args):
    try:
        tf = str(transform.get())
        index = len(data_array)
        value = float(data.get()) # fetch the data
        if tf == "sin":
            value = np.sin(value)
        elif tf == "cos":
            value = np.cos(value)
        elif tf == "tan":
            value = np.tan(value)
        elif tf == "exp":
            value = np.exp(value)
        print("Value:\t", str(value), "\n")
        data_array.append(value)
        show_stats()
        show_plot()
        head = "[" + str(index) + "]:\t" + str(data_array[index])
        dlist.insert(END, head, '')

                    
    except ValueError:
        pass
        

root = Tk()
root.title("Simple Laboratory Statistics Calculator")
mainframe = ttk.Frame(root, padding="3 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


pdata = StringVar()
data = StringVar()
std = StringVar()
avg = StringVar()
mx = StringVar()
mn = StringVar()
variance = StringVar()
co_var = StringVar()
med = StringVar()
points = StringVar()

xlabel = StringVar()
ylabel = StringVar()
title = StringVar()

filename = StringVar()

data_file = StringVar()

mute = IntVar()
sine = IntVar()

data_mute = IntVar()

scrollbar = Scrollbar(root)


scrollbar.grid(column=8, row=0, sticky='ns')
dlist = Listbox(root, yscrollcommand=scrollbar.set)
dlist.grid(column=8, row=0, sticky='ns')
scrollbar.config(command = dlist.yview)

data_entry = ttk.Entry(mainframe, width=4, textvariable=data)
data_entry.grid(column=0, row=0, stick=(W, E))

plt_title = ttk.Entry(mainframe, width=4, textvariable=title)
plt_title.grid(column=3, row=0, stick=(W, E))
ttk.Label(mainframe, text="Title").grid(column=4, row=0, sticky=(W, E))

plt_x = ttk.Entry(mainframe, width=4, textvariable=xlabel)
plt_x.grid(column=3, row=1, stick=(W, E))
ttk.Label(mainframe, text="X-Label").grid(column=4, row=1, sticky=(W, E))

plt_y = ttk.Entry(mainframe, width=4, textvariable=ylabel)
plt_y.grid(column=5, row=0, stick=(W, E))
ttk.Label(mainframe, text="Y-Label").grid(column=6, row=0, sticky=(W, E))

ttk.Label(mainframe, text="Data Entry").grid(column=1, row=0, sticky=(W, E))

plt_title = ttk.Entry(mainframe, width=4, textvariable=title)
plt_title.grid(column=4, row=2, stick=(W, E))
ttk.Label(mainframe, text="Filename").grid(column=5, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Save", command=save_data).grid(column=6, row=2, sticky=W)

ttk.Button(mainframe, text="Add", command=add_data).grid(column=2, row=0, sticky=W)
ttk.Button(mainframe, text="Clear", command=clear_data).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="Plot", command=show_plot).grid(column=6, row=1, sticky=W)

ttk.Label(mainframe, textvariable=std).grid(column=0, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Std-Dev").grid(column=1, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=avg).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="Average").grid(column=3, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=mx).grid(column=0, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Maximum").grid(column=1, row=3, sticky=(W, E))

ttk.Label(mainframe, textvariable=mn).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Minimum").grid(column=3, row=3, sticky=(W, E))

ttk.Label(mainframe, textvariable=variance).grid(column=0, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Variance").grid(column=1, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=co_var).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, text="Co-Variance [%]").grid(column=3, row=4, sticky=(W, E))

ttk.Label(mainframe, textvariable=med).grid(column=0, row=5, sticky=(W, E))
ttk.Label(mainframe, text="Median").grid(column=1, row=5, sticky=(W, E))

ttk.Label(mainframe, textvariable=points).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, text="# of Points").grid(column=3, row=5, sticky=(W, E))

ttk.Label(mainframe, textvariable=data_file).grid(column=5, row=3, sticky=(W, E))
ttk.Label(mainframe, text="Saved").grid(column=4, row=3, sticky=(W, E))

Checkbutton(mainframe, text="Show Graphs", variable=mute).grid(row=6, sticky=W)


MODES = [["No Transform", "Exponetial Transform", "Tangent Transform", "Cosine Transform", 
"Sine Transform"], ["na", "exp", "tan", "cos", "sin"]]

transform = StringVar()
transform.set(MODES[0][0])

for i in range(len(MODES[0])):
    b = Radiobutton(mainframe, text=MODES[0][i], variable=transform, value=MODES[1][i])
    b.grid(column=i, row=8, sticky='ns')

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

data_entry.focus()
root.bind('<Return>', add_data)
root.mainloop()

