import cv2
import inference

ROBOFLOW_API_KEY = "XLGxYY7oZtBY0GZomIBs"
model = inference.get_roboflow_model("finwell/2", api_key=ROBOFLOW_API_KEY)


# Assuming you have a camera or video stream object (e.g., cv2.VideoCapture)
cap = cv2.VideoCapture(0)  # Use 0 for default camera, adjust as needed

while True:
    ret, frame = cap.read()

    # Perform object detection on the frame
    detections = model.predict(frame)

    # Draw bounding boxes on the frame based on the detections
    frame_with_boxes = inference.draw_boxes(frame, detections)

    # Display the frame with bounding boxes
    cv2.imshow("Real-Time Object Detection", frame_with_boxes)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
