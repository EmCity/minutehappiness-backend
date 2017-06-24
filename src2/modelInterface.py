# import model_name
import numpy as np
import cv2
import os
import json
import pickle
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import emoCNN
import numpy as np
from PIL import Image

def processImage(model,img):
    img_array = cv2.imread(img,0)
    img_name = img.split('/')[3].split('.') 
    second = img_name[0]
    model_res = model(Variable(img_array.from_numpy())).data
    json_res = json.dumps([{'faceAttributes':{'smile':model_res[0]}}])
    return [img, json_res, second]
    
def processImagesBatch(imgs, model_name = './emoCNNtrivial.p'):
    model = torch.load(model_name)
    results = []
    for img in imgs:
        img_res = processImage(model,img)
        results.append(img_res)
    return results
