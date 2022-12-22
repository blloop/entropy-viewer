from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

# String to hold file name
current_file = ''

# Search for file via dialog box
def get_file():

    global current_file
    current_file = askopenfilename()

    if (current_file == ''):
        file_name.config(text = 'Please select a file...')
    else:
        file_name.config(text = current_file)

# Check whether current file is valid (i.e. contains data bits)
def check_file():

    global current_file
    if (current_file == ''):
        start_text.config(text = 'ERROR: No file given!')
        return False
    elif (not (os.path.exists(current_file))):
        start_text.config(text = 'ERROR: Could not find file!')
        return False
    elif (not (os.path.isfile(current_file))):
        start_text.config(text = 'ERROR: Invalid file!')
        return False
    else:
        return True

# Analyze the file and create a plot from it
def analyze_file():

    global current_file
    if check_file():
        
        # Prepare variables for analysis
        num_bytes = os.stat(current_file).st_size
        start_text.config(text = 'Analyzing ' + str(num_bytes) + ' bytes')
        new_plot = Figure(
            figsize = (6, 3),
            dpi = 100
        )
        bytes_plot = new_plot.add_subplot(111)
        out_bytes = []

        # Open file and read 256 bytes at a time
        with open(current_file, 'rb') as f:
            for i in range(num_bytes // 256):
                
                bytes = [0] * 256
                uniques = 0

                for j in range(256):

                    # Calculate number of unique byte values in 256 bytes
                    one_byte = f.read(1)
                    if not one_byte:
                        break
                    if (bytes[int.from_bytes(one_byte, 'big') - 1] == 0):
                        uniques += 1
                        bytes[int.from_bytes(one_byte, 'big') - 1] = 1
        
                out_bytes.append(uniques / 256)

        # Create plot on canvas and add to UI
        bytes_plot.plot(out_bytes)
        canvas = FigureCanvasTkAgg(new_plot, master = window)
        canvas.draw()
        canvas.get_tk_widget().place(x = 0, y = 100)

# Basic tkinter layout
window = Tk()
window.title('Entropy Viewer')
window.geometry('600x400')
window.configure(background = '#d5d5d5')

# Button to search for file
file_button = Button(
    master = window,
    command = get_file,
    height = 1, 
    width = 8, 
    text = 'Open File', 
    font = ('Tahoma 12')
)

# Text to hold file name string
file_name = Label(
    master = window, 
    text = 'Please select a file...',
    font = ('Tahoma 12'),
    background = '#d5d5d5'
)

# Button to start analyzing file
start_button = Button(
    master = window,
    command = analyze_file,
    height = 1,
    width = 8, 
    text = 'Analyze',
    font = ('Tahoma 12')
)

# Text to display error messages
start_text = Label(
    master = window,
    text = '',
    font = ('Tahoma 12 bold'),
    background = '#d5d5d5'
)

# Bottom frame to contain graph
bottom_frame = Frame(
     master = window,
     height = 300,
     width = 600,
     background = '#eaeaea'
)

# Add widgets to window and run
file_button.place(x = 15, y = 10)
file_name.place(x = 110, y = 12)
start_button.place(x = 15, y = 55)
start_text.place(x = 110, y = 57)
bottom_frame.place(x = 0, y = 100)
window.mainloop()
