import cv2

# Open the camera connected to the CSI port (usually device 0 for Jetson)
# You may need to change the index based on your setup. Try 0, 1, etc.
cap = cv2.VideoCapture("/dev/video0")

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Start video capture loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame was successfully captured
    if ret:
        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to quit the video capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Failed to capture frame.")
        break

# Release the capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()
