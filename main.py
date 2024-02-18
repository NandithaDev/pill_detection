# main
from kin import *
from const_camera import *
from camera import *
import tkinter as tk
from tkinter import messagebox
from const_camera import showVideo
from kin import capture_and_predict
#from tkinter import ttk
import ttkbootstrap as ttk

# Window ================================================
#window = tk.Tk()
window = ttk.Window(themename = "yeti")
window.title("Window and widgets")
window.geometry("450x200")#eg:- "800x700" at least at the start

# Tkinter variables ================================================


# Functions ================================================

"""
def func2():
	print("button 2 pressed")
	image = showVideo((500, 500))
	cv2.imshow("Webcam Image", image)  # Display the captured image
	cv2.waitKey(5000)
"""
def capture_and_predict_wrapper():
        try:
            image = showVideo()
            class_name, confidence_score = capture_and_predict()
            messagebox.showinfo("Prediction", f"Class Name: {class_name}\nConfidence Score: {confidence_score}%")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def func3():
	if continuous_camera(True) == "const":
		image = showVideo((500, 500))
		capture_and_predict_wrapper()
		
		# print(f"{capture_and_predict()}")
		cv2.imshow("Webcam Image", image)  # Display the captured image
		cv2.waitKey(1000)


# Widgets ================================================


#Button Widget
def button_func2():
	func3()
button_str2 = tk.StringVar(value = "Click to start camera")
button2 = ttk.Button(
	master = window,
	text = "Button",
	command = lambda: button_func2(),
	textvariable = button_str2
	)
button2.pack()
#----------------------------------------button
#Label Widget
label_str = tk.StringVar(value = "PRESS SPACE TO CAPTURE AND PREDICT")
label = ttk.Label(
	master = window,
	text = "Label ",
	textvariable = label_str,
	font = "Calibri 16"
	)
label.pack() 
#----------------------------------------label

"""
#Button Widget
def button_func1():
	pass
	
button_str1 = tk.StringVar(value = "PRESS SPACE to Predict")
button1 = ttk.Button(
	master = window,
	text = "Button",
	command = lambda: button_func1(),
	textvariable = button_str1
	)
button1.pack()
"""
#----------------------------------------button


# Events ================================================
# window.bind("<KeyPress-c>",lambda event: print(f"{capture_and_predict()}"))

# RUN ================================================
 
window.mainloop()

























