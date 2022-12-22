from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter.font as font

# String to hold file name
current_file = ""

# Search for file via dialog box
def get_file():
    current_file = askopenfilename()
    if (current_file == ""):
        file_name.config(text = "Please select a file...")
    else:
        file_name.config(text = current_file)

# Check whether a file is valid (i.e. contains data bits)
def check_file(string):
    pass

# Basic tkinter layout
window = Tk()
window.title('Entropy Viewer')
window.geometry("600x400")

# Button to search for file
file_button = Button(
    master = window,
    command = get_file,
    height = 1, 
    width = 8, 
    text = "Open File", 
    font = ('Tahoma 14')
)

# Text to hold file name string
file_name = Label(
    master = window, 
    text = "Please select a file...",
    font = ('Tahoma 12')
)

# Blank overlay for bottom of app
blank_overlay = Frame(
     master = window,
     height = 340,
     width = 600,
     background = '#d5d5d5'
)

# Add widgets to window and run
file_button.place(x = 15, y = 10)
file_name.place(x = 120, y = 15)
blank_overlay.place(x = 0, y = 60)
window.mainloop()
