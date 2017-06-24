import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('sachin.jpg')

os.chdir('video')

folders = os.listdir(os.getcwd())
print folders

for video in folders:
	images = os.listdir(os.getcwd() + '/' + str(video))
	for i in images:
		img = cv2.imread(i)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)
