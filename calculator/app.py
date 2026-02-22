import tkinter as tk
from tkinter import messagebox

def start_calculator() -> None:
    window = tk.Tk()
    window.title("Calculator")
    window.resizable(False, False)

    # --- helpers ---
    def read_inputs() -> tuple[float, float]:
        try:
            return float(first_input.get()), float(second_input.get())
        except ValueError as exc:
            raise ValueError("numbers only") from exc

    def show_result(value: float) -> None:
        if value.is_integer():
            result_text.config(text=f"Result: {int(value)}")
        else:
            result_text.config(text=f"Result: {value}")

    def input_error() -> None:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

    # --- operations ---
    def do_add() -> None:
        try:
            a, b = read_inputs()
            show_result(a + b)
        except ValueError:
            input_error()

    def do_subtract() -> None:
        try:
            a, b = read_inputs()
            show_result(a - b)
        except ValueError:
            input_error()

    def do_multiply() -> None:
        try:
            a, b = read_inputs()
            show_result(a * b)
        except ValueError:
            input_error()

    def do_divide() -> None:
        try:
            a, b = read_inputs()
            if b == 0:
                result_text.config(text="Error: Cannot divide by zero.")
                return
            show_result(a / b)
        except ValueError:
            input_error()

    def reset() -> None:
        first_input.delete(0, tk.END)
        second_input.delete(0, tk.END)
        result_text.config(text="Result:")
        first_input.focus_set()

    # --- UI ---
    tk.Label(window, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    first_input = tk.Entry(window)
    first_input.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(window, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    second_input = tk.Entry(window)
    second_input.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(window, text="Add", command=do_add, width=12).grid(row=2, column=0, padx=10, pady=5)
    tk.Button(window, text="Subtract", command=do_subtract, width=12).grid(row=2, column=1, padx=10, pady=5)
    tk.Button(window, text="Multiply", command=do_multiply, width=12).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(window, text="Divide", command=do_divide, width=12).grid(row=3, column=1, padx=10, pady=5)

    tk.Button(window, text="Clear", command=reset).grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    result_text = tk.Label(window, text="Result:")
    result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    window.bind("<Escape>", lambda _e: reset())

    first_input.focus_set()
    window.mainloop()


if __name__ == "__main__":
    start_calculator()
