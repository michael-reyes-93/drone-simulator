# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 01:51:56 2019

@author: micha
"""

import numpy as np
from alexnet import alexnet

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'drone-{}-{}-{}-epochs.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH,HEIGHT,LR)

train_data = np.load('training_data_v2.npy', allow_pickle=True)

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = [i[1] for i in test]

model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}), 
    snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

# tensorboard --logdir=foo:C:/Users/H/Desktop/ai-gaming/log

model.save(MODEL_NAME)