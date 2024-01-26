import cv2
import inference

# Set your Roboflow API key and model ID
ROBOFLOW_API_KEY = "XLGxYY7oZtBY0GZomIBs"
MODEL_ID = "finwell/2"

# Initialize the model
model = inference.get_roboflow_model(MODEL_ID, api_key=ROBOFLOW_API_KEY)

# Open a video capture device (0 for default webcam, or provide the path to a video file)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Perform object detection
    detections = model.infer(image=frame)

    # Draw bounding boxes on the frame
    for detection in detections:
        x, y, w, h = detection['box']
        cv2.rectangle(frame, (int(x), int(y)), (int(x+w), int(y+h)), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Object Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
