# kin

import cv2
from keras.models import load_model
import numpy as np
from PIL import Image, ImageTk

camera = cv2.VideoCapture(0)  # Open default camera


# Load model and labels once
model = load_model("converted_keras/keras_Model.h5", compile=False)
class_names = open("converted_keras/labels.txt", "r").readlines()

class_names = open("converted_keras/labels.txt", "r").readlines()
def capture_and_predict():
    ret, frame = camera.read()
    if ret:
        # Preprocess image
        image_array = np.array(frame)
        image_array = cv2.resize(image_array, (224, 224))
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB)
        image_array = image_array / 255.0
        image_array = image_array[np.newaxis, ...]

        # Run prediction
        prediction = model.predict(image_array, verbose=0)
        index = np.argmax(prediction)
        class_name = class_names[index]
        
        confidence_score = prediction[0][index]

        #print(f"item: {class_name} {np.round(confidence_score * 100)}%")
        return [class_name[2:-1],np.round(confidence_score * 100)]
