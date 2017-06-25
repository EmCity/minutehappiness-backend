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
from make_dataloader import *
from PIL import Image
gpu_device = 0
torch.cuda.set_device(gpu_device)
print('Chosen GPU device: ' + str(torch.cuda.current_device()))

def processImage(model,csv_a):
    video_name = csv_a.split('/')[3].split('.') 
    path = csv_a
    csv_a_time = csv_a[:-12] + "/time_stamps.csv"
    #print(csv_a_time)
    df_time = pd.read_csv(csv_a_time,delimiter = ',',header=None)
    #print(df_time.head())
    loader = make_dataloader(only_two = False, batch_size = 50, file_name = csv_a,predict=True,shuffle=False)['train_loader']
    all_res = []
    i = 0
    for im_batch, label in loader:
        model_res = model(Variable(im_batch,requires_grad=False).cuda(0)).cpu()
        model_res = model_res.data.cpu()
        for res in model_res:
            json_res = json.dumps([{'faceAttributes':{'smile':res[0]}}])
            all_res.append([csv_a, json_res, df_time[0][i]])
            i+=1
    return all_res
    
def processImagesBatch(csv_address, model_name = './emoCNNtrivial.p',model = None):
    if model == None:
        model = torch.load(model_name)
    results = []
    for csv_a in csv_address:
        img_res = processImage(model,csv_a)
        results.extend(img_res)
    return results

def get_csv_test_addr():
    pass

#csv_address = ['../youtube/video/2aU4wRgl_0E/testcsv.csv']
#res = processImagesBatch(csv_address)
#print(res)
#processImage(torch.load('./emoCNNtrivial.p'),p)
