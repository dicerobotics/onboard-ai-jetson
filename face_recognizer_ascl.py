import gi
import cv2
import face_recognition
import numpy as np

# # Initialize the camera (replace with the correct camera index if necessary)
# cap = cv2.VideoCapture("/dev/video0")

# Initialize GStreamer
gi.require_version('Gst', '1.0')
from gi.repository import Gst

# Initialize GStreamer library
Gst.init(None)

# GStreamer pipeline


# width=1280
# height=720
# flip=2
# pipeline = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=3280, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# pipeline = 'v4l2src device=/dev/video0 ! video/ax-raw,width='+str(width)+',height='+str(height)+',framerate=24/1 ! videoconvert ! appsink'
# pipeline = "nvarguscamerasrc ! video/x-raw(memory:NVMM),width=1280,height=720,framerate=30/1 ! nvvidconv ! video/x-raw, format=BGRx ! videoconvert ! appsink"

# Create GStreamer pipeline
# cap = cv2.VideoCapture(pipeline, cv2.CAP_GSTREAMER)


cap = cv2.VideoCapture("/dev/video0")
if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()


# Load known face images and encode them (You should use images of known individuals here)
# For example, known face images: 'person1.jpg', 'person2.jpg', etc.
known_face_encodings = []
known_face_names = []

# Load an image of a known person (add your images here)
image_of_person1 = face_recognition.load_image_file("./data/Bang_Hyochoong.jpg")
person1_encoding = face_recognition.face_encodings(image_of_person1)[0]
known_face_encodings.append(person1_encoding)
known_face_names.append("Bang_Hyochoong")

image_of_person2 = face_recognition.load_image_file("./data/Arshad_MA.jpg")
person2_encoding = face_recognition.face_encodings(image_of_person2)[0]
known_face_encodings.append(person2_encoding)
known_face_names.append("Arshad_MA")

image_of_person3 = face_recognition.load_image_file("./data/Mikael_Marin.jpg")
person3_encoding = face_recognition.face_encodings(image_of_person3)[0]
known_face_encodings.append(person3_encoding)
known_face_names.append("Mikael_Marin")


image_of_person4 = face_recognition.load_image_file("./data/Kim_Taeho.jpg")
person4_encoding = face_recognition.face_encodings(image_of_person4)[0]
known_face_encodings.append(person4_encoding)
known_face_names.append("Kim_Taeho")

image_of_person5 = face_recognition.load_image_file("./data/Zewge_Natnael.jpg")
person5_encoding = face_recognition.face_encodings(image_of_person5)[0]
known_face_encodings.append(person5_encoding)
known_face_names.append("Zewge_Natnael")

# Initialize variables for face locations and recognition
face_locations = []
face_encodings = []
face_names = []

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Convert the image from BGR (OpenCV format) to RGB (face_recognition format)
    rgb_frame = frame[:, :, ::-1]
    
    # Detect faces in the image using face_recognition
    face_locations = face_recognition.face_locations(rgb_frame)
    
    # Get face encodings for the detected faces
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each detected face and check if it matches any known face
    face_names = []
    for face_encoding in face_encodings:
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"  # Default name if no match is found

        # If a match is found, assign the name of the recognized person
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Display the results (face locations and names)
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        # Display the name of the person
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Show the video feed with face recognition results
    cv2.imshow("Face Recognition", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
