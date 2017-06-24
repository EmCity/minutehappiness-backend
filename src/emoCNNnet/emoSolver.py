from random import shuffle
import numpy as np

import torch
from torch.autograd import Variable

class emoSolver(object):
    default_adam_args = {"lr": 1e-4,
                         "betas": (0.9, 0.999),
                         "eps": 1e-8,
                         "weight_decay": 0.0}

    def __init__(self, optim=torch.optim.Adam, optim_args={},
                 loss_func=torch.nn.CrossEntropyLoss):
        optim_args_merged = self.default_adam_args.copy()
        optim_args_merged.update(optim_args)
        self.optim_args = optim_args_merged
        self.optim = optim
        self.loss_func = loss_func()
        self._reset_histories()

    def _reset_histories(self):
        """
        Resets train and val histories for the accuracy and the loss.
        """
        self.train_loss_history = []
        self.train_acc_history = []
        self.val_acc_history = []
        
    def get_acc(self, x_out, y):
        xx = np.argmax(x_out.data.numpy(),axis=1)
        yy = y.data.numpy()
        return(np.mean(xx == yy))
        
    def get_valid_stats(self, model, val_loader):
        divisor = 0.0
        v_loss = 0.0
        v_acc = 0.0
        for valid_x_batch, valid_y_batch in val_loader:
            xxx = Variable(valid_x_batch, requires_grad=False)
            yyy = Variable(valid_y_batch, requires_grad=False)
            xxx_out = model(xxx)
            v_loss+= self.loss_func(xxx_out, yyy)
            v_acc+= self.get_acc(xxx_out,yyy)
            divisor+=1.0
        v_loss/=divisor
        v_acc/=divisor
        return((v_loss,v_acc))

    def train(self, model, train_loader, val_loader, num_epochs=10, log_nth=0):
        optim = self.optim(model.parameters(), **self.optim_args)
        self._reset_histories()
        
        iter_per_epoch = len(train_loader)
        num_iter = iter_per_epoch*num_epochs
        print('START TRAIN.')
      
        optim.zero_grad()
        i = 0
        for epoch in range(num_epochs):
            for x_batch, y_batch in train_loader:
                x = Variable(x_batch, requires_grad=False)
                y = Variable(y_batch, requires_grad=False)
                x_out = model(x)
                loss = self.loss_func(x_out, y)
                loss.backward()
                optim.step()
                self.train_loss_history.append(loss.data[0])
                
                if i%log_nth == 0:
                    print("[iteration %d/%d] TRAIN loss : %f"%(i, num_iter, loss.data[0]))
                    
                if i%(log_nth) == 0:
                    (v_loss,v_acc) = self.get_valid_stats(model,val_loader)                    
                    self.val_acc_history.append(v_acc)
                    print("[iteration %d/%d] VALID acc/loss : %f/%f"%(i, num_iter,v_acc,v_loss.data[0]))
                    if v_acc > model.best_val_acc:
                        model.best_val_acc = v_acc
                        model.best_parameters = model.parameters
                i+=1
                
            t_acc = self.get_acc(x_out, y)
            self.train_acc_history.append(t_acc)
            print("[Epoch %d/%d] TRAIN acc/loss : %f/%f"%(epoch,num_epochs,t_acc,loss.data[0]))
            (v_loss,v_acc) = self.get_valid_stats(model, val_loader)                    
            self.val_acc_history.append(v_acc)
            print("[Epoch %d/%d] VALID acc/loss : %f/%f"%(epoch,num_epochs,v_acc,v_loss.data[0]))
            if v_acc > model.best_val_acc:
                model.best_val_acc = v_acc
                model.best_parameters = model.parameters
        model.parameters = model.best_parameters
        print 'FINISH.'
