#@charles Gaydon
#preprocessing of fer2013
#save dataloader into a pickle file

import pandas as pd
import numpy as np
from torch.utils import data
import torch
import pickle

def make_dataloader(only_two = True):
    df = pd.read_csv('fer2013/fer2013.csv', delimiter=',',dtype={'emotion':np.int32, 'pixels':str, 'Usage':str})
    #df.head()
    def makeArray(text):
        return np.fromstring(text,sep=' ')
    df['pixels'] = df['pixels'].apply(makeArray)
    #df.head()
    #df.Usage.unique()
    
    #turn to two classes
    if only_two:
        def emo_binary(emo_id):
            if emo_id==3:
                return 0
            else:
                return 1
        df['emotion'] = df['emotion'].apply(emo_binary)
    
    
    train_df = df[df['Usage'] == 'Training']
    valid_df = df[df['Usage'] == 'PublicTest']
    test_df = df[df['Usage'] == 'PrivateTest']
    
    train_labels = train_df.emotion.values
    train_data = np.vstack(train_df.pixels.values)
    valid_labels = valid_df.emotion.values
    valid_data = np.vstack(valid_df.pixels.values)
    test_labels = test_df.emotion.values
    test_data = np.vstack(test_df.pixels.values)
    
    
    T_train_data = torch.from_numpy(train_data.reshape(train_data.shape[0],1,48,48)).float()
    T_train_labels = torch.from_numpy(train_labels)
    valid_t = data.TensorDataset(T_train_data,T_train_labels)
    T_valid_data = torch.from_numpy(valid_data.reshape(valid_data.shape[0],1,48,48)).float()
    T_valid_labels = torch.from_numpy(valid_labels)
    valid_t = data.TensorDataset(T_valid_data,T_valid_labels)
    T_test_data = torch.from_numpy(test_data.reshape(test_data.shape[0],1,48,48)).float()
    T_test_labels = torch.from_numpy(test_labels)
    test_t = data.TensorDataset(T_test_data,T_test_labels)
    
    batch_size = 64
    train_loader = torch.utils.data.DataLoader(valid_t, batch_size=batch_size, shuffle=False, num_workers=4,
                                               drop_last = True)
    valid_loader = torch.utils.data.DataLoader(valid_t, batch_size=batch_size, shuffle=False, num_workers=4,
                                               drop_last = True)
    test_loader = torch.utils.data.DataLoader(test_t, batch_size=batch_size, shuffle=False, num_workers=4,
                                               drop_last = True)
    
    #save them
    
    loaders = {'train_loader':train_loader,
               'valid_loader':valid_loader,
               'test_loader':test_loader}
    pickle.dump(loaders, open('./fer2013/fer2013Loaders.p',"wb"))
    print("Fer2013 preprocessed and loaders saved in :")
    print('./fer2013/fer2013Loaders.p')
