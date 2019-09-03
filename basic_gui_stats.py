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
import re


data_array = list()

xy_array = [[], []]

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
            #fig, ax = plt.subplots()
            ax.hist(data_array, color='red')
            plt.xlabel(xax)
            plt.title(ttl)
            plt.ylabel(yax)
            textstr = '\n'.join((
                r'$\mathrm{median}=%.2f$' % (np.median(data_array), ),
                r'$\mathrm{average}=%.2f$' % (np.average(data_array), ),
                r'$\mathrm{Entries}=%.2f$' % (len(data_array), ),
                r'$\sigma=%.2f$' % (np.std(data_array), )))
    
            props = dict(boxstyle='round', facecolor='wheat', alpha=1)
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
        
def clear_xy():
    global xy_array
    xy_array = [[], []]
    print(xy_array)
    xstd.set(0)
    xavg.set(0)
    xmx.set(0)
    xmn.set(0)
    xvariance.set(0)
    xco_var.set(0)
    xmed.set(0)
    xmn.set(0)
    xpoints.set(0)
    ystd.set(0)
    yavg.set(0)
    ymx.set(0)
    ymn.set(0)
    yvariance.set(0)
    yco_var.set(0)
    ymed.set(0)
    ymn.set(0)
    ypoints.set(0)
    
def stats_xy():
    xstd.set(np.std(xy_array[0]))
    xavg.set(np.average(xy_array[0]))
    xmx.set(np.amax(xy_array[0]))
    xmn.set(np.amin(xy_array[0]))
    xvariance.set(np.var(xy_array[0]))
    xco_var.set(np.std(xy_array[0]) / np.average(xy_array[0]) * 100)
    xmed.set(np.median(xy_array[0]))
    xmn.set(np.amin(xy_array[0]))
    xpoints.set(len(xy_array[0]))
    
    ystd.set(np.std(xy_array[1]))
    yavg.set(np.average(xy_array[1]))
    ymx.set(np.amax(xy_array[1]))
    ymn.set(np.amin(xy_array[1]))
    yvariance.set(np.var(xy_array[1]))
    yco_var.set(np.std(xy_array[1]) / np.average(xy_array[1]) * 100)
    ymed.set(np.median(xy_array[1]))
    ymn.set(np.amin(xy_array[1]))
    ypoints.set(len(xy_array[1]))

def add_xy(*args):
    try:
        g = int(xy_mute.get())
        ret = str(xydata.get())
        ret = re.findall(r"[-+]?\d*\.\d+|\d+", ret)
        ret = list(map(float, ret))
        xy_array[0].append(ret[0])
        xy_array[1].append(ret[1])
        print("X:\t", str(ret[0]), "\tY:\t", str(ret[1]), "\n")
        stats_xy()
        if g > 0:
            plot_xy()
    except ValueError:
        pass

def plot_xy(*args):
    xind, yind = len(xy_array[0]) - 1, len(xy_array[1]) - 1
    plt.scatter(xy_array[0][xind], xy_array[1][yind], color='red', marker='^')
    plt.pause(0.05)


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

xydata = StringVar()


scrollbar.grid(column=8, row=0, sticky='ns')
dlist = Listbox(root, yscrollcommand=scrollbar.set)
dlist.grid(column=8, row=0, sticky='ns')
scrollbar.config(command = dlist.yview)

data_entry = ttk.Entry(mainframe, width=4, textvariable=data)
data_entry.grid(column=0, row=0, stick=(W, E))

data_xy = ttk.Entry(mainframe, width=4, textvariable=xydata)
data_xy.grid(column=0, row=9, stick=(W, E))
ttk.Label(mainframe, text="X & Y Data").grid(column=1, row=9, sticky=(W, E))
ttk.Label(mainframe, text="Format: 'X, Y'").grid(column=2, row=9, sticky=(W, E))


ttk.Button(mainframe, text="Clear", command=clear_xy).grid(column=3, row=9, sticky=W)
# For XY Data Format

xstd = StringVar()
xavg = StringVar()
xmx = StringVar()
xmn = StringVar()
xvariance = StringVar()
xco_var = StringVar()
xmed = StringVar()
xpoints = StringVar()

ystd = StringVar()
yavg = StringVar()
ymx = StringVar()
ymn = StringVar()
yvariance = StringVar()
yco_var = StringVar()
ymed = StringVar()
ypoints = StringVar()

xy_mute = IntVar()

Checkbutton(mainframe, text="XY Graph", variable=xy_mute).grid(column=4, row=9, sticky=W)

ttk.Label(mainframe, textvariable=xstd).grid(column=0, row=10, sticky=(W, E))
ttk.Label(mainframe, text="[X] Std-Dev").grid(column=1, row=10, sticky=(W, E))

ttk.Label(mainframe, textvariable=xavg).grid(column=0, row=11, sticky=(W, E))
ttk.Label(mainframe, text="[X] Average").grid(column=1, row=11, sticky=(W, E))

ttk.Label(mainframe, textvariable=xmx).grid(column=0, row=12, sticky=(W, E))
ttk.Label(mainframe, text="[X] Maximum").grid(column=1, row=12, sticky=(W, E))

ttk.Label(mainframe, textvariable=xmn).grid(column=0, row=13, sticky=(W, E))
ttk.Label(mainframe, text="[X] Minimum").grid(column=1, row=13, sticky=(W, E))

ttk.Label(mainframe, textvariable=xvariance).grid(column=0, row=14, sticky=(W, E))
ttk.Label(mainframe, text="[X] Variance").grid(column=1, row=14, sticky=(W, E))

ttk.Label(mainframe, textvariable=xco_var).grid(column=0, row=15, sticky=(W, E))
ttk.Label(mainframe, text="[X] Co-Variance [%]").grid(column=1, row=15, sticky=(W, E))

ttk.Label(mainframe, textvariable=xmed).grid(column=0, row=16, sticky=(W, E))
ttk.Label(mainframe, text="[X] Median").grid(column=1, row=16, sticky=(W, E))

ttk.Label(mainframe, textvariable=xpoints).grid(column=0, row=17, sticky=(W, E))
ttk.Label(mainframe, text="[X] # of Points").grid(column=1, row=17, sticky=(W, E))

ttk.Label(mainframe, textvariable=ystd).grid(column=2, row=10, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Std-Dev").grid(column=3, row=10, sticky=(W, E))

ttk.Label(mainframe, textvariable=yavg).grid(column=2, row=11, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Average").grid(column=3, row=11, sticky=(W, E))

ttk.Label(mainframe, textvariable=ymx).grid(column=2, row=12, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Maximum").grid(column=3, row=12, sticky=(W, E))

ttk.Label(mainframe, textvariable=ymn).grid(column=2, row=13, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Minimum").grid(column=3, row=13, sticky=(W, E))

ttk.Label(mainframe, textvariable=yvariance).grid(column=2, row=14, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Variance").grid(column=3, row=14, sticky=(W, E))

ttk.Label(mainframe, textvariable=yco_var).grid(column=2, row=15, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Co-Variance [%]").grid(column=3, row=15, sticky=(W, E))

ttk.Label(mainframe, textvariable=ymed).grid(column=2, row=16, sticky=(W, E))
ttk.Label(mainframe, text="[Y] Median").grid(column=3, row=16, sticky=(W, E))

ttk.Label(mainframe, textvariable=ypoints).grid(column=2, row=17, sticky=(W, E))
ttk.Label(mainframe, text="[Y] # of Points").grid(column=3, row=17, sticky=(W, E))


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
root.bind('<Tab>', add_xy)

fig, ax = plt.subplots()

plt.figure(10)

root.mainloop()

