# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 16:05:53 2017

@author: User
"""

import numpy as np
import cv2
from grabscreen import grab_screen
import time
from getkeys import key_check
import os

#define key to output to be a one-hot vector
def keys_to_output(keys):
    #[W,S,I,J,K,L,1]
    output = [0,0,0,0,0,0,0]
    
    if 'W' in keys:
        output[0] = 1
    elif 'S' in keys:
        output[1] = 1
    elif 'I' in keys:
        output[2] = 1
    elif 'J' in keys:
        output[3] = 1
    elif 'K' in keys:
        output[4] = 1
    elif 'L' in keys:
        output[5] = 1
    elif '1' in keys:
        output[6] = 1
        
    return output

#save the key
file_name = 'training_data24.npy'

if os.path.isfile(file_name):
    print("File exists, loading data!")
    training_data = list(np.load(file_name))
else:
    print("starting a new one")
    training_data = []

def main(): 
    for i in range(4):
        print(i+1)
        time.sleep(1)
        
#    last_time = time.time()
    paused = False
    
    while(True):
        
        if not paused:
        
            printscreen = grab_screen(region=(0,40,1260,750))
            printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
            printscreen = cv2.resize(printscreen,(300,179))
            
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([printscreen, output])
    #        print('respond time: ', time.time()-last_time)
    #        last_time = time.time()
    
            if len(training_data) % 500 == 0:
                print(len(training_data))
            if len(training_data) % 4500 ==0:
                np.save(file_name, training_data)
                print("Saved, please re")
                
        if 'T' in keys:
            if paused:
                paused = False
                print('Start again')
                time.sleep(2)
            else:
                paused = True
                print('Paused')
                time.sleep(2)


if __name__ == '__main__':
    main()