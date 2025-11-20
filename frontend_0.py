import tkinter as tk

root = tk.Tk()# Create the main application window

root.title("Simple Tkinter App")
root.geometry("200x100") # Set Window size

# function to print "Hello, World!" in the console
def say_hello():
    print("Hello World!")

# Create a button that triggers the say_hello funciton
hello_button = tk.Button(root, text="Click Me", command=say_hello)
hello_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()