# camera.py
import cv2

def continuous_camera(show_video=True):
 
    camera = cv2.VideoCapture(0)

    try:
        while True:
            ret, image = camera.read()

            if not ret:
                print("Failed to capture frame!")
                continue

            image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_AREA)

            if show_video:
                cv2.imshow("Webcam Image", image)

                # Wait for a key press or escape to break the loop
                key = cv2.waitKey(1) & 0xFF
                if key == 32:
                    return "const"

            else:  # Capture and display a single image
                cv2.imshow("Captured Image", image)
                cv2.waitKey(0) 
                return image # Wait indefinitely for a key press
                

    except Exception as e:
        print(f"Error: {e}")

    finally:
        camera.release()
        cv2.destroyAllWindows()

# Call the function to start either video or single image capture
# continuous_camera(True)  # For continuous video
# continuous_camera(True)  # For single image capture

























