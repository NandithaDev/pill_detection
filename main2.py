
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
def submit(label1_text, label2_text):
    d={}
    pill_name = label1_text.get()
    dosage = label2_text.get()
    
    
    d[pill_name] = dosage
    
    print("Dictionary updated:", d)

    #writing into dict
    

    # Do something with the user input, e.g., process it or display it elsewhere
def display_box():
   add_button.destroy()
  
   '''  add_window = tk.Toplevel()
    add_window.title("Text Input Example")'''

    # Create the main window
    #window = tk.Tk()
    #window.title("Text Input Example")

    # Create a label1
   label1 = tk.Label(window, text="Enter the pill name:")
   label1.pack()

    # Create an entry widget for text input
   label1_text = tk.StringVar()
   entry1 = tk.Entry(window, textvariable=label1_text)
   entry1.pack()
    #button 2


    # Create a label
   label2 = tk.Label(window, text="Enter the dosage:")
   label2.pack()

# Create an entry widget for text inpu
   label2_text = tk.StringVar()
   entry2 = tk.Entry(window, textvariable=label2_text)
   entry2.pack()
#entry = tk.Entry(window)
#entry.pack()

# Create a button to submit the input
   submit_button = tk.Button(window, text="Submit", command=lambda: submit(label1_text, label2_text))
   submit_button.pack()
   
    
    
    
    
# Create the main window
# window = tk.Tk()
window = ttk.Window(themename = "lumen")
window.title("Text Input Example")



add_button = tk.Button(window,text="Add",command=display_box)

add_button.pack()


window.mainloop()

# Run the Tkinter event loop
