import cv2
import numpy as np

# Load the pre-trained MobileNet SSD model and its configuration file
net = cv2.dnn.readNetFromCaffe("deploy.prototxt", "mobilenet_iter_73000.caffemodel")

# Open a video capture object (0 represents the default camera, you can change it if you have multiple cameras)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Couldn't open the camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Couldn't read a frame.")
        break

    # Resize the frame for faster processing (you can adjust the dimensions)
    resized_frame = cv2.resize(frame, (300, 300))

    # Prepare the frame for object detection by normalizing pixel values
    blob = cv2.dnn.blobFromImage(resized_frame, 0.007843, (300, 300), 127.5)

    # Set the input to the pre-trained model
    net.setInput(blob)

    # Perform object detection
    detections = net.forward()

    # Initialize the position variables
    fish_position = None

    # Loop over the detected objects
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Confidence threshold (you can adjust this value)
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])

            # Check if the detected object is a fish (you may need to customize class labels)
            if class_id == 1:
                box = detections[0, 0, i, 3:7] * np.array([300, 300, 300, 300])
                (startX, startY, endX, endY) = box.astype("int")

                # Store the position of the detected fish
                fish_position = ((startX + endX) // 2, (startY + endY) // 2)

                # Draw a bounding box around the detected fish
                cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the frame with the detected fish
    cv2.imshow("Fish Detection", frame)

    # Print the fish position
    if fish_position:
        print("Fish Position:", fish_position)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
