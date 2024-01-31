import time
import cv2

# Open a connection to the webcam
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object for MP4 output
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # or use 'XVID'
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

start_time = time.time()

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Write the frame into the file 'output.avi'
        out.write(frame)

        # Break the loop after 1 minute
        if time.time() - start_time > 60:
            break
    else:
        break

# Release everything when job is finished
cap.release()
out.release()
cv2.destroyAllWindows()