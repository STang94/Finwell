import cv2

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

# Capture a single frame
ret, frame = cap.read()

# Save the frame as an image
if ret == True:
    cv2.imwrite('output.jpg', frame)

# Release the webcam
cap.release()