```# Pill Identification Project

## Introduction

This project aims to develop a real-time pill identification system using image detection technology. The system utilizes a pre-trained Keras model to analyze images captured from a camera interface and predict the name of the medicine pill with high accuracy. The user-friendly interface, developed using Tkinter, enhances accessibility and usability, making it suitable for various healthcare applications.

## Features

- Real-time pill identification through camera input.
- Integration of a pre-trained Keras model for accurate prediction.
- User-friendly interface developed with Tkinter.
- Ability to capture and predict single or continuous video frames.
- Display of prediction results including the pill name and confidence score.

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

- Ensure proper camera setup and lighting conditions for accurate predictions.
- The model and labels files must be placed in the specified directories for the application to function correctly.
- Future improvements may include integrating prescription information and expanding the dataset for enhanced prediction capabilities and integrating a text to voice model as well.




