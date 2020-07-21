from tkinter import *
from tkinter import ttk
import random
from bubble import bubble_sort
from quick import quick_sort
from merge import merge_sort

root = Tk()
root.title('Visuals of Sorting Algorithms')  # Display Title
root.maxsize(900, 600)
# for background color of interface
root.config(bg='black')

# Cariable to store selected Algorithm name
selalg = StringVar()
data = []

# Function to plot bars


def drawbar(data, barcolor):
    box2.delete("all")
    eleheight = 380
    elewidth = 690
    xwidth = elewidth/(len(data)+1)
    offset = 30
    spacing = 10
    # Normalization of data wrt to largest value
    normalized_Data = [i/max(data) for i in data]
    for i, height in enumerate(normalized_Data):
        x0 = i*xwidth + offset + spacing
        y0 = eleheight - height*340
        x1 = (i+1)*xwidth + offset
        y1 = eleheight
        box2.create_rectangle(x0, y0, x1, y1, fill=barcolor[i])
        box2.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
    root.update_idletasks()

# Function to print the Algo selected


def Generate():
    global data
    print('Selected Algo :' + selalg.get())
    length = int(sizein.get())
    mini = int(minval.get())
    maxa = int(maxval.get())

    data = []
    for _ in range(length):
        data.append(random.randrange(mini, maxa+1))
    drawbar(data, ['red' for x in range(len(data))])


def StartAlgo():
    global data
    if not data:
        return
    if menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawbar, visualspeed.get())
    elif menu.get() == 'Merge Sort':
        merge_sort(data, drawbar, visualspeed.get())
    elif menu.get() == 'Bubble Sort':
        bubble_sort(data, drawbar, visualspeed.get())
    drawbar(data, ['green' for x in range(len(data))])


# Top Box for User Interface
box1 = Frame(root, width=600, height=200, bg='grey')
box1.grid(row=0, column=0, padx=10, pady=5)

# Bottom Box
box2 = Canvas(root, width=700, height=380, bg='white')
box2.grid(row=1, column=0, padx=10, pady=5)


# ROW 0 STARTS HERE
Label(box1, text="ALGORITHM : ", bg='grey').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)

# MENU
menu = ttk.Combobox(box1, textvariable=selalg, value=[
                    'Bubble Sort', 'Quick Sort', 'Merge Sort'])
menu.grid(row=0, column=1, padx=5, pady=5)
menu.current(0)  # Sets default to Index 0 element (Here Bubble Sort)
Label(box1, text=" TRANSITION TIME (sec) : ", bg='grey').grid(
    row=0, column=4, padx=5, pady=5, sticky=W)
visualspeed = Scale(box1, from_=0.1, to=2.0, length=200, digits=2,
                    resolution=0.2, orient=HORIZONTAL)
visualspeed.grid(row=0, column=5, padx=5, pady=5)
# ROW 0 ENDS HERE

# ROW 1 STARTS HERE
# Size Input
Label(box1, text="           SIZE : ", bg='grey').grid(
    row=1, column=0, padx=5, pady=5, sticky=W)
sizein = Entry(box1)
sizein.grid(row=1, column=1, padx=5, pady=5, sticky=W)

# Range Input
Label(box1, text="      LOWER LIMIT : ", bg='grey').grid(
    row=1, column=2, padx=5, pady=5, sticky=W)
minval = Entry(box1)
minval.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(box1, text="          UPPER LIMIT : ", bg='grey').grid(
    row=1, column=4, padx=5, pady=5, sticky=W)
maxval = Entry(box1)
maxval.grid(row=1, column=5, padx=5, pady=5, sticky=W)
# ROW 1 ENDS HERE
Button(box1, text="  GENERATE  ", command=Generate,
       bg='green').grid(row=2, column=1, padx=10, pady=5)
Button(box1, text="  START  ", command=StartAlgo,
       bg='red').grid(row=2, column=5, padx=10, pady=5)

root.mainloop()
