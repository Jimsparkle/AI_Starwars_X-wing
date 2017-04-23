# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:17:48 2017

@author: User
"""

import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

#show data as video
show_data = False
'''
if show_data:
    for data in train_data:
        img = data[0]
        choice = data[1]
        cv2.imshow('test',img)
        print(choice)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
'''        
#Bbalancing data
'''
Count all the kye press

df = pd.DataFrame(train_data)
#print(df.head())
print(Counter(df[1].apply(str)))
'''


forwards = []
backwards = []
up = []
left = []
down = []
right = []
shield = []
static = []

for num in range(25)[1:]:
    train_file = 'training_data'+str(num)+'.npy'
    print('open file number '+str(num))
    train_data = np.load(train_file)
    shuffle(train_data)
    
    for data in train_data:
        img = data[0]
        choice = data[1]
        
        if choice == [1,0,0,0,0,0,0,0]:
            forwards.append([img,[1,0,0,0,0,0,0]])
        elif choice == [0,1,0,0,0,0,0,0]:
            backwards.append([img,[0,1,0,0,0,0,0]])
        elif choice == [0,0,1,0,0,0,0,0]:
            up.append([img,[0,0,1,0,0,0,0]])
        elif choice == [0,0,0,1,0,0,0,0]:
            left.append([img,[0,0,0,1,0,0,0]])
        elif choice == [0,0,0,0,1,0,0,0]:
            down.append([img,[0,0,0,0,1,0,0]])
        elif choice == [0,0,0,0,0,1,0,0]:
            right.append([img,[0,0,0,0,0,1,0]])
        elif choice == [0,0,0,0,0,0,1,0]:
            shield.append([img,[0,0,0,0,0,0,1]])
        else :
            static.append([img,[0,0,0,0,0,0,0]])
    
    print('len of static before trim: ', len(static))
    static = static[:int((len(static)/3))]
    print('len of forwards after trim: ',len(static))
    
    
final_data = forwards + backwards + up + left + down + right + shield + static
print(len(final_data))
shuffle(final_data)
np.save('training_data.npy', final_data)

