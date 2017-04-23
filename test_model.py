# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:52:54 2017

@author: User
"""
import numpy as np
import cv2
from grabscreen import grab_screen
import time
import threading
from getkeys import key_check
from network import alexnet
from directkey import PressKey, ReleaseKey, W, S, SPACE, J, K, L, I, ONE


#Set key
t_time = 0.09

def straight():
    PressKey(W)
    time.sleep(t_time)
    ReleaseKey(S)
    
def attack():
    PressKey(S)
    time.sleep(t_time)
    PressKey(SPACE)
    time.sleep(t_time)
    time.sleep(0.1)
    ReleaseKey(S)
    ReleaseKey(SPACE)
    
def left():
    PressKey(J)
    time.sleep(t_time)
    ReleaseKey(I)
    ReleaseKey(K)
    ReleaseKey(L)


def right():
    PressKey(L)
    time.sleep(t_time)
    ReleaseKey(I)
    ReleaseKey(J)
    ReleaseKey(K)   


def up():
    PressKey(I)
    time.sleep(t_time)
    ReleaseKey(J)
    ReleaseKey(K)
    ReleaseKey(L)    

    
def down():
    PressKey(K)
    time.sleep(t_time)
    ReleaseKey(J)
    ReleaseKey(I)
    ReleaseKey(L)  

    


 

#set model
WIDTH = 300
HEIGHT = 179
LR = 1e-3
EPOCH = 10
MODEL_NAME = 'x-wing-{}-{}-{}-eponchs.model'.format(LR, 'alexnet', EPOCH)

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)



def main(): 
    for i in range(4):
        print(i+1)
        time.sleep(1)
        
#    last_time = time.time()
    paused = False
    
    def shield():
        threading.Timer(15,shield).start()
        if paused == False:
            PressKey(ONE)
            ReleaseKey(ONE)
    
    while(True):
        
        if not paused:
            printscreen =  grab_screen(region=(0,40,1260,750))
            printscreen = cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
            printscreen = cv2.resize(printscreen,(300,179))
            
            prediction = model.predict([printscreen.reshape(WIDTH,HEIGHT,1)])[0]
            moves = np.argmax(prediction)
            
            if moves == 0:
                straight()
            elif moves == 1:
                attack()
            elif moves == 2:
                up()
            elif moves == 3:
                left()
            elif moves == 4:
                down()
            elif moves == 5:
                right()
            elif moves == 6:
                shield()
            else :
                ReleaseKey(W)
                ReleaseKey(S)
                ReleaseKey(I)
                ReleaseKey(J)
                ReleaseKey(K)
                ReleaseKey(L)
                
            shield()
            
            
        
        keys = key_check()
        if 'T' in keys:
            if paused:
                print("RestartRestartRestartRestartRestartRestartRestartRestartRestart")
                paused = False
                time.sleep(1)
            else:
                paused = True
                print("PausedPausedPausedPausedPausedPausedPausedPausedPausedPausedPaused")
                ReleaseKey(W)
                ReleaseKey(S)
                ReleaseKey(I)
                ReleaseKey(J)
                ReleaseKey(K)
                ReleaseKey(L)
                ReleaseKey(ONE)
                time.sleep(1)
            
                      
main()