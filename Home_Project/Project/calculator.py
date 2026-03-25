import tkinter as tk
from tkinter import simpledialog, messagebox


def main():
    # Hide the main tkinter window as we only need dialog boxes
    root = tk.Tk()
    root.withdraw()

    first_number = 0.0
    second_number = 0.0
    valid_input = False

    # Loop to get and validate the first number
    while not valid_input:
        input1 = simpledialog.askstring("Input", "Input first number:")

        # Check if the user clicked 'Cancel' or closed the dialog
        if input1 is None:
            messagebox.showerror("Error", "Error, Closed program")
            return

        try:
            first_number = float(input1)
            valid_input = True
        except ValueError:
            # Handle non-numeric input (similar to NumberFormatException in Java)
            messagebox.showwarning("Warning", "Enter number only!")

    # Get the mathematical operation
    operation = simpledialog.askstring("Input", "Enter operation (+, -, *, /):")

    if operation is None:
        messagebox.showerror("Error", "Error, Closed program")
        return

    valid_input = False
    # Loop to get and validate the second number
    while not valid_input:
        input2 = simpledialog.askstring("Input", "Input second number:")

        if input2 is None:
            messagebox.showerror("Error", "Error, Closed program")
            return

        try:
            second_number = float(input2)
            valid_input = True
        except ValueError:
            messagebox.showwarning("Warning", "Enter number only!")

    result = 0.0

    # Calculation logic (equivalent to switch-case in Java)
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        # Handle division by zero
        if second_number == 0:
            messagebox.showerror("Error", "Can not divided by Zero!")
            return
        result = first_number / second_number
    else:
        # Handle invalid operators
        messagebox.showerror("Error", "Wrong operation")
        return

    # Format the result with comma separators and 2 decimal places
    # Equivalent to Java's DecimalFormat("#,###.00")
    formatted_result = "{:,.2f}".format(result)

    # Display the final output
    messagebox.showinfo(
        "Result", f"{first_number} {operation} {second_number} = {formatted_result}"
    )


if __name__ == "__main__":
    main()
