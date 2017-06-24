# import model_name
import numpy as np
import cv2
import os
import json
import pickle
import torch
import torch.nn.functional as F
from torch.autograd import Variable

'''
def processImage(img):
    img_array = cv2.imread(img,0)
    img_name = img.split('/')[3].split('.') 
    second = img_name[0]
    model_res = [0.5, 0.5]
    # model_res = model_name.predict(img_array)
    json_res = json.dumps([{'faceAttributes':{'smile':model_res[0]}}])
    return [img, json_res, second]
    
def processImagesBatch(imgs):
    results = []
    for img in imgs:
        img_res = processImage(img)
        results.append(img_res)
    return results
'''
model = pickle.load('emoCNNnet/emoCNNtrivial.p')
def processImagesBatch(imgs):
	for img in imgs:
		print(processImage(img))

def processImage()):
	print(np.fromfile(fname, dtype=dt))
	score = model(Variable(img.from_numpy()))
