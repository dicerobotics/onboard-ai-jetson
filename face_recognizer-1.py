import cv2
import face_recognition
print(cv2.__version__)
image=face_recognition.load_image_file('/home/arshad/PyPro/demoimages/unknown/u1.jpg')
face_locations=face_recognition.face_locations(image)
print(face_locations)
image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
for (row1,col1,row2,col2) in face_locations:
    cv2.rectangle(image,(col1,row1),(col2,row2),(255,0,0),2)
cv2.imshow('myWindow',image)
cv2.moveWindow('myWindow',0,0)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()