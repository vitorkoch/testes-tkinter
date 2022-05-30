import tkinter as tk
from calc import calc_window
from feature import feature_window

menu = tk.Tk()
menu.title('IFPA Project')
menu.geometry('200x100')
menu.resizable(0, 0)

calculator_button = tk.Button(
    menu, text='Calculator', command=calc_window, width=15)
calculator_button.pack(pady=1)

features_button = tk.Button(
    menu, text='Fun Features', command=feature_window, width=15)
features_button.pack(pady=1)

menu.mainloop()
