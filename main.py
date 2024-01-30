import os
import cv2
import csv
from ultralytics import YOLO
import time

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

# Create a CSV file to store the position information
csv_file_path = 'goldfish_positions.csv'
with open(csv_file_path, mode='w', newline='') as csvfile:
    fieldnames = ['timestamp', 'x1', 'y1', 'x2', 'y2', 'score', 'class']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write header to the CSV file
    writer.writeheader()

    frame_number = 0
    start_time = time.time()

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

            if score > threshold and results.names[int(class_id)] == 'goldfish':
                # Draw rectangle and label on the frame
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

                # Check if one second has passed
                current_time = time.time()
                if current_time - start_time >= 1:
                    # Write position information to the CSV file
                    writer.writerow({'timestamp': current_time, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'score': score, 'class': 'goldfish'})
                    start_time = current_time

        # Display the resulting frame
        cv2.imshow('Real-Time Object Detection', frame)

        # Check if the user pressed the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the resources
cap.release()
cv2.destroyAllWindows()
