#File:    newcalculator
#Purpose: Simple number calculator
#Author:  Jacob Romero, jrom876

'''
	Copyright (C) 4/28/2024 
	Jacob Romero, Creative Engineering Solutions, LLC
	cesllc876@gmail.com
 
	This program is free software; you can redistribute it
	and/or modify it under the terms of the GNU General Public  
	License as published by the Free Software Foundation, version 2.

	This program is distributed in the hope that it will be
	useful, but WITHOUT ANY WARRANTY; without even the implied 
	warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
	
	See the GNU General Public License for more details.
	
	You should have received a copy of the GNU General Public
	License along with this program; if not, write to:
	The Free Software Foundation, Inc.
	59 Temple Place, Suite 330
	Boston, MA 02111-1307 USA
 
	References:	
		
'''

import tkinter as tk
from math import factorial

# Function to update the display
def update_display(value):
    current_text = display_var.get()
    if current_text == "0":
        display_var.set(value)
    else:
        display_var.set(current_text + value)

# Function to clear the display
def clear_display():
    display_var.set("0")

# Function to evaluate the expression and display the result
def calculate_result():
    try:
        result = eval(display_var.get())
        display_var.set(result)
    except Exception as e:
        display_var.set("Error")

# Function to calculate the Factorial of a number
def fac(): 
	try: 
	   result = factorial(int(display_var.get())) 
	   clear_display()
	   display_var.set(result) 
	except Exception as e: 
	   clear_display()

# Create the main window
parent = tk.Tk()
parent.title("Calculator")

# Create a variable to store the current display value
display_var = tk.StringVar()
display_var.set("0")

# Create the display label
display_label = tk.Label(parent, textvariable=display_var, font=("Arial", 24), anchor="e", bg="lightgray", padx=10, pady=10)
display_label.grid(row=0, column=0, columnspan=4)

pi = 3.14159265358979
exp = 2.718281828459

button_layout = [
	("0", 5, 0), (".", 5, 2), ("/", 5, 3), ("exp", 5, 4), ("**2", 5, 5), ("=", 6, 3),
    ("7", 4, 0),  ("8", 4, 1), ("9", 4, 2), ("*", 4, 3),  ("(", 4, 4),  (")",  4, 5), 
    ("4", 3, 0),  ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),  ("%", 3, 4),  ("**", 2, 5),
    ("1", 2, 0),  ("2", 2, 1), ("3", 2, 2), ("+", 2, 3),  ("pi",2, 4),       
] 

# Create and place the buttons
for (text, row, col) in button_layout:
    button = tk.Button(parent, text=text, padx=20, pady=20, font=("Arial", 18),
                       command=lambda t=text: update_display(t) if t != "=" else calculate_result())
    button.grid(row=row, column=col)

# Create a Clear button
clear_button = tk.Button(parent, text="C", padx=20, pady=20, font=("Arial", 18), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=3)

# Create a Factorial button
factorial_button = tk.Button(parent, text="x!", padx=20, pady=20, font=("Arial", 18), command=fac)
factorial_button.grid(row=3, column=5, columnspan=3)

# Start the Tkinter event loop
parent.mainloop()
