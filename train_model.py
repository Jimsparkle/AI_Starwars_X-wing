# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:11:10 2017

@author: User
"""

import numpy as np
from network import alexnet
import os

WIDTH = 300
HEIGHT = 179
LR = 1e-3
EPOCH = 10
MODEL_NAME = 'x-wing-{}-{}-{}-eponchs.model'.format(LR, 'alexnet', EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)

print('loading data')
train_data = np.load('training_data.npy')
print('data loaded')

if os.path.exists('{}.meta'.format(MODEL_NAME)):
    model.load(MODEL_NAME)
    print('model loaded!!')

train = train_data[:-5000]
test = train_data[-5000:]

print('dealing with data')
X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

print('test begin')

model.fit({'input': X}, {'targets':Y}, n_epoch= EPOCH, 
          validation_set=({'input': test_x}, {'targets': test_y}), snapshot_step=500,
          show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:"C:\Users\User\Desktop\Python\Self driving car\log"

model.save(MODEL_NAME)