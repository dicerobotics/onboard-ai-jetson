import gi
import cv2

# Initialize GStreamer
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# Initialize GStreamer library
Gst.init(None)

# GStreamer pipeline
pipeline = "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1080,height=720,framerate=30/1, format=(string)NV12 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! appsink"

# Create GStreamer pipeline
cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

# Capture loop
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
