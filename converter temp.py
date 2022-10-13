import tkinter as tk

# Declare global variables
temp_c = None
temp_f = None


# This function is called whenever the button is pressed
def convert():

    global temp_c
    global temp_f

    # Convert Celsius to Fahrenheit and update label (through textvariable)
    try:
        val = temp_c.get()
        temp_f.set((val * 9.0 / 5) + 32)
    except:
        pass


# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create the main container
frame = tk.Frame(root)

# Lay out the main container, specify that we want it to grow with window size
frame.pack(fill=tk.BOTH, expand=True)

# Allow middle cell of grid to grow when window is resized
frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

# Variables for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()

# Create widgets
entry_celsius = tk.Entry(frame, width=7, textvariable=temp_c, font=("calibri", 12, "bold"), bg="yellow")
label_unit_c = tk.Label(frame, text="°C", font=("calibri", 12, "bold"))
label_equal = tk.Label(frame, text="is equal to:", font=("calibri", 12, "bold", "underline"))
label_fahrenheit = tk.Label(frame, textvariable=temp_f, font=("calibri", 12, "bold"))
label_unit_f = tk.Label(frame, text="°F", font=("calibri", 12, "bold"))
button_convert = tk.Button(frame, text="Convert", command=convert, font=("calibri", 12, "bold"), bg="yellow", activebackground="brown", fg="brown")

# Lay out widgets
entry_celsius.grid(row=0, column=1, padx=5, pady=5)
label_unit_c.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
label_equal.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
label_fahrenheit.grid(row=1, column=1, padx=5, pady=5)
label_unit_f.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky=tk.E)

# Place cursor in entry box by default
entry_celsius.focus()

# Run forever!
root.mainloop()

