```# Pill Identification Project

## Introduction

This project aims to develop a real-time pill identification system using image detection technology. The project involves training a Keras model, to analyze images captured from a camera interface and predict the name of the medicine pill with high accuracy. The user-friendly interface, developed using Tkinter, enhances accessibility and usability, making it a great help for elderly and visually impaired persons.

## Features

- Real-time pill identification through camera input.
- Training Keras model for prediction.
- User-friendly interface developed with Tkinter.
- Display of prediction results including the pill name and confidence score.
-Storing the prescription of the medicine in a csv file, to display along with the medicine name afeter detection.

## Installation

1. Clone the repository from GitHub.
2. Ensure Python 3.x is installed on your system.
3. Install the required dependencies using pip:
  -pip install keras
  -pip install opencv-python
  -pip install tensorflow
  -pip install numpy
  -pip install tkinter
  -pip install ttkbootstrap

## Usage

1. Run `main.py` to launch the application.
2. Click the button to start the camera and capture images for prediction.
3. Press the spacebar to capture and predict the pill name.
4. The predicted pill name and confidence score will be displayed.
5. Press the 'Esc' key to exit the application.

## Additional Notes
- only a limited amount of pill_detection models have been trained, thus the program will be limited to paracetamol, amoxcylin etc
- Ensure proper camera setup and lighting conditions for accurate predictions.
- The model and labels files must be placed in the specified directories for the application to function correctly.

#Future improvements
-Integrating an image to text model as well to further improve the reliability of the project.
-Setting up voice to text conversion for visually impaired.
-Moving it to a mobile application, say on flutter, to provide an even better interface and feautures like notification system to remind the user regarding their medicine intake.




