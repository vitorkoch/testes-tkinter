import tkinter as tk
from tkinter import messagebox


def calc_window():
    calculator = tk.Tk()
    calculator.title("Calculator")
    calculator.resizable(0, 0)
    calculator.configure(background="#525252")

    e = tk.Entry(calculator, width=40, borderwidth=5)
    e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    # Functions -------------------

    def button_click(number):
        current = e.get()
        e.delete(0, tk.END)
        e.insert(0, str(current) + str(number))

    def clear():
        e.delete(0, tk.END)

    def add():
        number_1 = e.get()
        global num1
        global math
        math = "add"
        num1 = float(number_1)
        e.delete(0, tk.END)

    def subtract():
        number_1 = e.get()
        global num1
        global math
        math = "subtract"
        num1 = float(number_1)
        e.delete(0, tk.END)

    def multiply():
        number_1 = e.get()
        global num1
        global math
        math = "multiply"
        num1 = float(number_1)
        e.delete(0, tk.END)

    def divide():
        number_1 = e.get()
        global num1
        global math
        math = "divide"
        num1 = float(number_1)
        e.delete(0, tk.END)

    def equal():
        try:
            num2 = float(e.get())
            e.delete(0, tk.END)

            if math == "add":
                result = num1 + num2
                e.insert(0, result)
            elif math == "subtract":
                result = num1 - num2
                e.insert(0, result)
            elif math == "multiply":
                result = num1 * num2
                e.insert(0, result)
            elif math == "divide":
                result = num1 / num2
                e.insert(0, result)
        except:
            messagebox.showerror("Error", "Try again")

    # Buttons ------------------------
    button_add = tk.Button(
        calculator, text="+", command=add, padx=25, pady=20, background="#C1C1C1")
    button_subtract = tk.Button(
        calculator, text="-", command=subtract, padx=28, pady=20, background="#C1C1C1")
    button_multiply = tk.Button(
        calculator, text="x", command=multiply, padx=26, pady=20, background="#C1C1C1")
    button_divide = tk.Button(
        calculator, text="÷", command=divide, padx=25, pady=20, background="#C1C1C1")

    button_equal = tk.Button(calculator, text="=", command=equal,
                             padx=24, pady=50, background="#C1C1C1")
    button_clear = tk.Button(calculator, text="C", command=clear,
                             padx=25, pady=50, background="#C1C1C1")

    button_1 = tk.Button(calculator, text="1", padx=25, pady=20,
                         command=lambda: button_click(1), background="#C1C1C1")
    button_2 = tk.Button(calculator, text="2", padx=25, pady=20,
                         command=lambda: button_click(2), background="#C1C1C1")
    button_3 = tk.Button(calculator, text="3", padx=25, pady=20,
                         command=lambda: button_click(3), background="#C1C1C1")
    button_4 = tk.Button(calculator, text="4", padx=25, pady=20,
                         command=lambda: button_click(4), background="#C1C1C1")
    button_5 = tk.Button(calculator, text="5", padx=25, pady=20,
                         command=lambda: button_click(5), background="#C1C1C1")
    button_6 = tk.Button(calculator, text="6", padx=25, pady=20,
                         command=lambda: button_click(6), background="#C1C1C1")
    button_7 = tk.Button(calculator, text="7", padx=25, pady=20,
                         command=lambda: button_click(7), background="#C1C1C1")
    button_8 = tk.Button(calculator, text="8", padx=25, pady=20,
                         command=lambda: button_click(8), background="#C1C1C1")
    button_9 = tk.Button(calculator, text="9", padx=25, pady=20,
                         command=lambda: button_click(9), background="#C1C1C1")
    button_0 = tk.Button(calculator, text="0", padx=95, pady=19,
                         command=lambda: button_click(0), background="#C1C1C1")

    # Positions of buttons --------------
    button_add.grid(column=3, row=1)
    button_subtract.grid(column=3, row=2)
    button_multiply.grid(column=3, row=3)
    button_divide.grid(column=3, row=4)

    button_1.grid(column=0, row=3)
    button_2.grid(column=1, row=3)
    button_3.grid(column=2, row=3)

    button_4.grid(column=0, row=2)
    button_5.grid(column=1, row=2)
    button_6.grid(column=2, row=2)

    button_7.grid(column=0, row=1)
    button_8.grid(column=1, row=1)
    button_9.grid(column=2, row=1)
    button_0.grid(column=0, row=4, columnspan=3)
    button_clear.grid(column=4, row=1, rowspan=2)
    button_equal.grid(column=4, row=3, rowspan=2)

    calculator.mainloop()


if __name__ == "__main__":
    calc_window()
