# camera
import cv2
import numpy as np

def showVideo(dim=(224, 224)):
 

    camera = cv2.VideoCapture(0)
    ret, image = camera.read()

    if ret:
        try:
            image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
            #cv2.imshow("Webcam Image", image)
            return image
        except Exception as e:
            print(f"Error displaying frame: {e}")
            return False

    else:
        print("Failed to capture frame!")
        return False

# Main 
