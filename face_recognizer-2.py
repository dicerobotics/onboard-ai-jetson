import cv2
import face_recognition
print(cv2.__version__)
 
donFace=face_recognition.load_image_file('/home/arshad/PyPro/demoimages/known/Donald Trump.jpg')
nancyFace=face_recognition.load_image_file('/home/arshad/PyPro/demoimages/known/Nancy Pelosi.jpg')
mikeFace=face_recognition.load_image_file('/home/arshad/PyPro/demoimages/known/Mike Pence.jpg')
 
donEncode=face_recognition.face_encodings(donFace)[0]
nancyEncode=face_recognition.face_encodings(nancyFace)[0]
mikeEncode=face_recognition.face_encodings(mikeFace)[0]
 
Encodings=[donEncode,nancyEncode,mikeEncode]
Names=['Donald Trump','Nancy Pelosi','Mike Pence']
 
font=cv2.FONT_HERSHEY_SIMPLEX/home/arshad/PyPro/demoimages
 
testImage=face_recognition.load_image_file('/home/arshad/PyPro/demoimages/unknown/u11.jpg')
 
facePositions=face_recognition.face_locations(testImage)
allEncodings=face_recognition.face_encodings(testImage,facePositions)
 
testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)
for (top,right,bottom,left), face_encoding in zip(facePositions,allEncodings):
    name='Unknown Life Form'
    matches=face_recognition.compare_faces(Encodings,face_encoding)
    if True in matches:
        first_match_index=matches.index(True)
        name=Names[first_match_index]
    
    cv2.rectangle(testImage,(left,top),(right,bottom),(255,0,0),2)
    cv2.rectangle(testImage,(left,top),(left+200, top+30),(0,255,255),-1)
    cv2.putText(testImage,name,(left,top+20),font,.75,(255,0,0),2)
cv2.imshow('myWindow',testImage)
cv2.moveWindow('myWindow',0,0)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()