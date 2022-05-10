from importlib.resources import path
from pydoc import classname
from cv2 import waitKey
import numpy as np
import cv2
import face_recognition
import os

path="images"
images=[]
classnames=[]
database=os.listdir(path)
print(database)
for i in database:
    currentimage=cv2.imread(f'{path}/{i}')
    images.append(currentimage)
    classnames.append(os.path.splitext(i)[0])
print(classnames)

def findencoding(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)

    return encodelist

encodelist=findencoding(images)    
# print(encodelist)


cap=cv2.VideoCapture(0)

while True:
    istrue, img=cap.read()
    # imgS=cv2.resize(img(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facescurrent=face_recognition.face_locations(imgS)
    encodecurrent=face_recognition.face_encodings(imgS,facescurrent)

    for encode,location in zip(encodecurrent,facescurrent):
        matches=face_recognition.compare_faces(encodelist,encode)
        distance=face_recognition.face_distance(encodelist,encode) 
        matchindex=np.argmin(distance) 

        if(matches[matchindex]):
            print("authorized")
        else:
            print("unauthorized person") 

    cv2.imshow("image",img)         
    cv2.waitKey(0)   