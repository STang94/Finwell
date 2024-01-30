import os
import cv2
from ultralytics import YOLO

# Specify the path to the YOLO model weights
model_path = os.path.join('.', 'runs', 'detect', 'train2', 'weights', 'last.pt')

# Load the YOLO model
model = YOLO(model_path)

# Set the detection threshold
threshold = 0.5

# Open a connection to the webcam (you can specify the camera index, 0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get the webcam frame dimensions
width = int(cap.get(3))
height = int(cap.get(4))

# Create a VideoWriter object to save the output
out = cv2.VideoWriter('real_time_output.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 30.0, (width, height))

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform object detection on the frame
    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Real-Time Object Detection', frame)

    # Write the frame to the output video file
    out.write(frame)

    # Check if the user pressed the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the resources
cap.release()
out.release()
cv2.destroyAllWindows()
