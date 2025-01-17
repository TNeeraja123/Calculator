import tkinter as tk

# Function to update the input field when a button is pressed
def button_click(item):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(tk.END, current + str(item))

# Function to clear the input field
def button_clear():
    input_field.delete(0, tk.END)

# Function to evaluate the expression in the input field
def button_equal():
    try:
        result = str(eval(input_field.get()))
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, result)
    except:
        input_field.delete(0, tk.END)
        input_field.insert(tk.END, "Error")

# Creating the main window
root = tk.Tk()
root.title("Calculator")

# Input field for the calculator
input_field = tk.Entry(root, width=16, font=('Arial', 20), borderwidth=2, relief="solid")
input_field.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '+', '='
]

# Adding buttons to the window
row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 15),
                  command=button_clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 15),
                  command=button_equal).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, font=('Arial', 15),
                  command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()


