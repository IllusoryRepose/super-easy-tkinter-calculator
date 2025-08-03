import tkinter as tk
import math

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  
        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error " + str(e))

window = tk.Tk()
window.title("Calculator")
window.geometry("600x400")

entry = tk.Entry(window, width=30)
entry.pack()

calculate_button = tk.Button(window, text="Math ", command=calculate)
calculate_button.pack()

result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
