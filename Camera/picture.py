import cv2
import time

# Open the webcam
cap = cv2.VideoCapture(0)


ret, frame = cap.read()

# Save the image

cv2.imwrite(f'image123.png', frame)

# Release the webcam
cap.release()