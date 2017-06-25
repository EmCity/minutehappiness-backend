import os

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
#import torch.nn.init as weight_init
#weight_init.xavier_normal(self.double_fc_encoder[0].weight.data)
import numpy as np
from collections import OrderedDict
import pickle


class emoCNNnet(nn.Module):
    """
        Structure

    """

    def __init__(self, input_dim=(1, 48, 48), hidden_dim=100, num_classes=2, 
                 dropout=0.0,stride=1, kernels = (64,128)):
        super(emoCNNnet, self).__init__()
        self.input_dim = input_dim
        self.best_val_acc = 0.0    
        channels, height, width = input_dim
        k1,k2 = kernels
        self.feature = nn.Sequential(
                nn.Conv2d(channels,k1,kernel_size=7,padding=3, bias=True).cuda(0),
                nn.BatchNorm2d(k1).cuda(0),
                nn.ReLU(),
                nn.Conv2d(k1,k1,kernel_size=7,padding=3, bias=True).cuda(0),
                nn.BatchNorm2d(k1).cuda(0),
                nn.ReLU(),
                nn.MaxPool2d(2, stride = 2,return_indices=False).cuda(0),
                nn.Conv2d(k1,k2,kernel_size=5,padding=2,bias=True).cuda(0),
                 nn.BatchNorm2d(k2).cuda(0),
                 nn.ReLU(),
                 nn.Conv2d(k2,k2,kernel_size=5,padding=2,bias=True).cuda(0),
                 nn.BatchNorm2d(k2).cuda(0),
                 nn.ReLU(),
                 nn.MaxPool2d(2, stride = 2,return_indices=False).cuda(0),
                )
        # self.feature = nn.Sequential(nn.Conv2d(channels,k1,kernel_size=7,padding=3, bias=True).cuda(0),
        #         nn.BatchNorm2d(k1).cuda(0),
        #         nn.ReLU(),
        #         nn.Conv2d(k1,k1,kernel_size=7,padding=3, bias=True).cuda(0),
        #         nn.BatchNorm2d(k1).cuda(0),
        #         nn.ReLU())
        lin_input = self.get_lin_input()
        self.classifier = nn.Sequential(
                nn.Linear(lin_input,hidden_dim).cuda(0),
                nn.BatchNorm1d(hidden_dim).cuda(0),
                nn.ReLU(),
                nn.Linear(hidden_dim,2).cuda(0)
                )
        self.best_parameters = self.parameters
        print(self.parameters)

    def get_lin_input(self):
        f = self.feature(Variable(torch.ones(1,*self.input_dim)).cuda(0))
        return(int(np.prod(f.size()[:])))
    
    def forward(self, x):
        """
        Forward pass of the convolutional neural network. Should not be called
        manually but by calling a model instance directly.
        """
        x = self.feature(x)
        x = x.view(x.size(0),-1)
        out = self.classifier(x)
        return out

    def save(self, path):
        """
        Save model with its parameters to the given path. Conventionally the
        path should end with "*.model".

        Inputs:
        - path: path string
        """
        print('Saving model... %s' % path)
        torch.save(self, path)
