import cv2
import time
from datetime import datetime

# Open the camera (0 represents the default camera, you can change it if you have multiple cameras)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

try:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Check if the frame is read successfully
        if not ret:
            print("Error: Couldn't read a frame.")
            break

        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Save the frame as an image file with a timestamp
        filename = f"Picture/camera_screenshot_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")

        # Wait for 10 seconds
        time.sleep(10)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Release the camera
    cap.release()

    # Close any open windows
    cv2.destroyAllWindows()
