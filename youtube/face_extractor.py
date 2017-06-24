import numpy as np
import cv2
import os
import re


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
os.chdir('video')


folders = os.listdir(os.getcwd())
print(folders)

for video in folders:
    if not os.path.isfile(str(video) + '/output.mp4'):
        continue
        images = os.listdir(os.getcwd() + '/' + str(video))

    video_file = cv2.VideoCapture(str(video) + '/output.mp4')
    frameRate = video_file.get(25)
    current_path = os.getcwd() + "/" + str(video)
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frameId % math.floor(frameRate) == 0):
            img = cv2.imread(image_file_name, 0)
            faces = face_cascade.detectMultiScale(img, 1.3, 5)
            print(faces)
            for f in faces:
                x, y, w, h = [ v for v in f ]
                #drop face if it is smaller than 40 px
                if w < 40 or h < 40:
                    continue
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))
                sub_face = img[y:y+h, x:x+w]

                eyes = eye_cascade.detectMultiScale(sub_face)


                resize_face = cv2.resize(sub_face, (48, 48))
                resize_face = cv2.equalizeHist(resize_face)

                id = re.findall(r'\d+', str(i))[0]

                face_file_name = current_path + "/" + str(id) + "face.jpg"
                cv2.imwrite(face_file_name, resize_face)
                print("saved" + face_file_name)
    cap.release()
