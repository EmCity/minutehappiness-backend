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
gpu_device = 0
torch.cuda.set_device(gpu_device)
print('Chosen GPU device: ' + str(torch.cuda.current_device()))

def processImage(model,img):
    img_array = cv2.imread(img,0)
    img_name = img.split('/')[3].split('.') 
    #img_name = 'test'
    second = img_name[0]
    tensor = torch.from_numpy(img_array).float().unsqueeze(0).unsqueeze(0)
    model_res = model(Variable(tensor).cuda(0))
    model_res = model_res.data.cpu()
    json_res = json.dumps([{'faceAttributes':{'smile':model_res[0,0]}}])
    return [img, json_res, second]
    
def processImagesBatch(imgs, model_name = './emoCNNtrivial.p',model = None):
    if model == None:
        model = torch.load(model_name)
    results = []
    for img in imgs:
        img_res = processImage(model,img)
        results.append(img_res)
    return results
