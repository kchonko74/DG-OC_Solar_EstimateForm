import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

#OC SOLAR - INTERACTIVE SOLAR ESTIMATOR FORM

#Declare root, title, and widget size
root = Tk()
root.title('OC Solar Installation Estimator')
root.geometry('500x500')

#Create horizontal slider for home square footage
def show():
    mylabel = Label(root, text = var.get()).pack()

    
Label(root, text= 'What is the square footage of your home?', justify = tk.LEFT, padx = 20).pack()    
sqFt = Scale(root,from_ = 0,to = 5000, orient = HORIZONTAL)
sqFt.pack()
def slide():
    myLabel = Label(root, text = sqFt.get()).pack()
#mybtn = Button(root, text = 'Calculate Install Price', command = slide).pack()

#Create horizontal slider for monthly electric bill
Label(root, text= 'What is your average monthly electric bill?', justify = tk.LEFT, padx = 20).pack()    
eb = Scale(root, from_ = 0, to = 500, orient = HORIZONTAL)
eb.pack()
def slider():
    myLabel = Label(root, text = eb.get()).pack()
#mybtn2 = Button(root, text = 'Show Electric Bill', command = slider).pack()

#RadioButton - for EV's
Label(root, text = 'How many Electric Vehicles do you own?', justify = tk.LEFT, padx = 20).pack()

q = IntVar()
q.set(0)
def clickme(value):
    myLabel = Label(root, text = value).pack()
    
Radiobutton(root, text = 'Zero EVs', variable = q, value = 0).pack()
Radiobutton(root, text = '1 EV', variable = q, value = 1).pack()
Radiobutton(root, text = '2 EVs', variable = q, value = 2).pack()
Radiobutton(root, text = '3+ EVs', variable = q, value = 3).pack()
#myButton = Button(root, text = 'Number of Electric Vehicles?', command = lambda:clickme(q.get())).pack()



#RadioButton - for Battery Y/N
Label(root, text= 'Do you want a battery?', justify = tk.LEFT, padx = 20).pack()

r = IntVar()
r.set(1)

def clickme(value):
    myLabel = Label(root, text = value).pack()
    
Radiobutton(root, text = 'Yes', variable = r, value = 1).pack()
Radiobutton(root, text = 'No', variable = r, value = 0).pack()
#myButton = Button(root, text = 'Do you want a battery?', command = lambda:clickme(r.get())).pack()

def finalcost():
    myLabel1 = float(sqFt.get()*5.8 + (eb.get())*1.18 + (q.get() * 1.05 * eb.get()) + (14000*r.get()))
    myLabel2 = float(sqFt.get()*8.1 + (eb.get())*1.34 + (q.get() * 1.12 * eb.get()) + (14500*r.get()))
    priceLow = Label(root, text = "Your estimated install price is between $%d" %myLabel1).pack()
    priceHigh = Label(root, text = " and $%d." %myLabel2).pack()
Calc = Button(root, text = 'Get Estimate', command = finalcost).pack()


"""Create input field for customer to enter their email"""
# import re

# regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# def signIn():
#     if(re.fullmatch(regex, entry_var2.get())):
#         print("Valid Email")
#     else:
#         print("Invalid Email")

root.mainloop()