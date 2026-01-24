"""
Desktop Calculator Application

A simple GUI-based calculator built using Python and Tkinter.
Supports basic arithmetic operations with input validation.

Author: Samuel Zizzo
"""

# ----------------------------
# Imports
# ----------------------------

import tkinter as tk
from tkinter import messagebox


# ----------------------------
# Arithmetic Operation Functions
# ----------------------------

def add():
    """
    Adds the two numbers entered by the user.
    Displays the result or an error message if input is invalid.
    """
    try:
        result = float(entry1.get()) + float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def subtract():
    """
    Subtracts the second number from the first number.
    Displays the result or an error message if input is invalid.
    """
    try:
        result = float(entry1.get()) - float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def multiply():
    """
    Multiplies the two numbers entered by the user.
    Displays the result or an error message if input is invalid.
    """
    try:
        result = float(entry1.get()) * float(entry2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


def divide():
    """
    Divides the first number by the second number.
    Handles division-by-zero and invalid input cases.
    """
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if num2 == 0:
            label_result.config(text="Error! Cannot Divide by Zero.")
        else:
            result = num1 / num2
            label_result.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")


# ----------------------------
# Utility Functions
# ----------------------------

def clear():
    """
    Clears both input fields and resets the result label.
    """
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    label_result.config(text="Result: ")


# ----------------------------
# Application Runner
# ----------------------------

def run_app():
    """
    Initializes and runs the calculator GUI application.
    """
    global root, entry1, entry2, label_result

    # Create the main application window
    root = tk.Tk()
    root.title("Calculator")

    # ----------------------------
    # Input Fields
    # ----------------------------

    tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    # ----------------------------
    # Operation Buttons
    # ----------------------------

    tk.Button(root, text="Add", command=add).grid(row=2, column=0, padx=10, pady=5)
    tk.Button(root, text="Subtract", command=subtract).grid(row=2, column=1, padx=10, pady=5)
    tk.Button(root, text="Multiply", command=multiply).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(root, text="Divide", command=divide).grid(row=3, column=1, padx=10, pady=5)

    # ----------------------------
    # Clear Button
    # ----------------------------

    tk.Button(root, text="Clear", command=clear).grid(
        row=4, column=0, columnspan=2, padx=10, pady=5
    )

    # ----------------------------
    # Result Display
    # ----------------------------

    label_result = tk.Label(root, text="Result: ")
    label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    # Start the Tkinter event loop
    root.mainloop()


# ----------------------------
# Script Entry Point
# ----------------------------

if __name__ == "__main__":
    run_app()
