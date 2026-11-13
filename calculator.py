import tkinter as tk
from tkinter import messagebox

# ----------------------------
# Calculator Functions
# ----------------------------

expression = ""


def update_expression(value):
    global expression
    expression += str(value)
    display_var.set(expression)


def clear():
    global expression
    expression = ""
    display_var.set("")


def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)


def calculate(event=None):
    global expression
    try:
        # Replace % with /100
        expr = expression.replace("%", "/100")

        result = str(eval(expr))
        display_var.set(result)
        expression = result

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        expression = ""
        display_var.set("")

    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""
        display_var.set("")


# ----------------------------
# GUI
# ----------------------------

root = tk.Tk()
root.title("Python Calculator")
root.geometry("360x520")
root.resizable(False, False)
root.configure(bg="#e9e9e9")

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.FLAT,
    bg="white"
)

display.pack(fill="both", padx=10, pady=15, ipady=15)


button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(expand=True, fill="both")


def create_button(text, row, col, command=None, colspan=1):
    btn = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 18, "bold"),
        command=command if command else lambda: update_expression(text),
        bd=0,
        bg="#2d2d2d",
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        cursor="hand2"
    )

    btn.grid(
        row=row,
        column=col,
        columnspan=colspan,
        sticky="nsew",
        padx=4,
        pady=4,
        ipadx=10,
        ipady=15
    )


# Configure Grid
for i in range(6):
    button_frame.rowconfigure(i, weight=1)

for j in range(4):
    button_frame.columnconfigure(j, weight=1)


# Row 0
create_button("C", 0, 0, clear)
create_button("⌫", 0, 1, backspace)
create_button("%", 0, 2)
create_button("/", 0, 3)

# Row 1
create_button("7", 1, 0)
create_button("8", 1, 1)
create_button("9", 1, 2)
create_button("*", 1, 3)

# Row 2
create_button("4", 2, 0)
create_button("5", 2, 1)
create_button("6", 2, 2)
create_button("-", 2, 3)

# Row 3
create_button("1", 3, 0)
create_button("2", 3, 1)
create_button("3", 3, 2)
create_button("+", 3, 3)

# Row 4
create_button("(", 4, 0)
create_button("0", 4, 1)
create_button(")", 4, 2)
create_button(".", 4, 3)

# Row 5
create_button("=", 5, 0, calculate, colspan=4)


# ----------------------------
# Keyboard Support
# ----------------------------

allowed = "0123456789+-*/().%"


def key_press(event):
    global expression

    key = event.keysym

    if key == "Return":
        calculate()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()

    else:
        char = event.char

        if char in allowed:
            update_expression(char)


root.bind("<Key>", key_press)

display.focus_set()

root.mainloop()