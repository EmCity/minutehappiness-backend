import cv2
import os
import re

face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface_improved.xml')
os.chdir('video')

big_face = False
ratio = 0.6

folders = os.listdir(os.getcwd())

for video in folders:
    images = os.listdir(os.getcwd() + '/' + str(video))
    current_path = os.getcwd() + "/" + str(video)
    for i in images:
        image_file_name = current_path + "/" + i
        img = cv2.imread(image_file_name, 0)
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        print(faces)
        t_h,t_w = img.shape
        for f in faces:
            x, y, w, h = [ v for v in f ]
            #drop face if it is smaller than 40 px
            if w < 40 or h < 40:
                continue
            #drop face if face relatively too small in screen
            if float(w)/flaot(t_w) <ratio or float(h)A/float(t_h)<ratio:
                continue
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))
            sub_face = img[y:y+h, x:x+w]

            resize_face = cv2.resize(sub_face, (48, 48))
            resize_face = cv2.equalizeHist(resize_face)

            id = re.findall(r'\d+', str(i))[0]

            face_file_name = current_path + "/" + str(id) + "face.jpg"
            cv2.imwrite(face_file_name, resize_face)
            print("saved" + face_file_name)

        #remove image file
        #os.remove(image_file_name) ##uncomment to clean !