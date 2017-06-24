import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.chdir('video')

folders = os.listdir(os.getcwd())

for video in folders:
    images = os.listdir(os.getcwd() + '/' + str(video))
    current_path = os.getcwd() + "/" + str(video)
    for i in images:
        img = cv2.imread(current_path + "/" + i, 0)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        print(faces)
        for f in faces:
            x, y, w, h = [ v for v in f ]
            #drop face if it is smaller than 40 px
            if w < 40 or h < 40:
                continue
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))
            sub_face = img[y:y+h, x:x+w]
            resize_face = cv2.resize(sub_face, (48, 48))
            face_file_name = current_path + "/" + str(i) + "face.jpg"
            cv2.imwrite(face_file_name, resize_face)
            print("saved" + face_file_name)

