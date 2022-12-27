import os
import math
import sys
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def main(argv):

    if (len(sys.argv) < 2):
        print("Usage: python " + sys.argv[0] + " input_file")
        exit()
    else:
        current_file = sys.argv[1]

        if (not (os.path.exists(current_file))):
            print("ERROR: Could not find specified file!")
            exit()
        elif (not (os.path.isfile(current_file))):
            print("ERROR: Could not open path as file!")
            exit()
        else:

            # Basic tkinter layout
            window = Tk()
            window.title('Entropy Viewer')
            window.geometry('600x300')
            window.configure(background = '#d5d5d5')

            # Prepare variables for analysis
            num_bytes = os.stat(current_file).st_size
            new_plot = Figure(
                figsize = (6, 3),
                dpi = 100
            )
            bytes_plot = new_plot.add_subplot(111)      
            bytes_plot.set_ylim([0, 1])
            out_bytes = []
            

            # Open file and read 256 bytes at a time
            with open(current_file, 'rb') as f:
                for i in range(num_bytes // 256):
                    
                    e_bytes = [0] * 256
                    entropy = 0.0

                    # Calculate list of counts of unique byte values (0-255)
                    for j in range(256):
                        one_byte = f.read(1)
                        e_bytes[int.from_bytes(one_byte, 'big')] += 1
                    
                    # Calculate entropy based on all positive list values
                    for k in e_bytes:
                        if (k == 0):
                            continue
                        p = (k / 256)
                        entropy = entropy - (p * (math.log(p, 256)))

                    # Add entropy value to our output list
                    out_bytes.append(entropy)

            # Create plot on canvas and add to UI
            bytes_plot.plot(out_bytes)
            canvas = FigureCanvasTkAgg(new_plot, master = window)
            canvas.draw()
            canvas.get_tk_widget().place(x = 0, y = 0)
            
            # Run UI loop to produce graph
            window.mainloop()

if __name__ == "__main__":
   main(sys.argv[1:])