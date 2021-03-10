import speech_recognition as sr
import numpy as np
import matplotlib.pyplot as plt
import cv2
from easygui import *
import os
from PIL import Image, ImageTk
from itertools import count
import tkinter as tk
import string
#import selecting
# obtain audio from the microphone
def func():
        r = sr.Recognizer()
        
        arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
        's','t','u','v','w','x','y','z']
        with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source) 
                i=0
                while True:
                        print('Say something')
                        audio = r.listen(source)

                                                        # recognize speech using Sphinx
                        try:
                                a=r.recognize_google(audio)
                                print("you said " + a.lower())
                                
                                for c in string.punctuation:
                                    a= a.replace(c,"")
                                    
                                if(a.lower()=='goodbye'):
                                        print("oops!Time To say good bye")
                                        break
                    
                                else:

                                    for i in range(len(a)):
                                                    #a[i]=a[i].lower()
                                                    if(a[i] in arr):
                                            
                                                            ImageAddress = 'letters/'+a[i]+'.jpg'
                                                            ImageItself = Image.open(ImageAddress)
                                                            ImageNumpyFormat = np.asarray(ImageItself)
                                                            plt.imshow(ImageNumpyFormat)
                                                            plt.draw()
                                                            plt.pause(0.8) # pause how many seconds
                                                            #plt.close()
                                                    else:
                                                            continue

                        except:
                               print("Could not listen")
                        plt.close()

#func()
while 1:
  image   = "signlang.png"
  msg="VOICE TRANSLATOR ASSISTANT- A Project By Manas GOkhale ,Yogita Khosla , Nidhi Kantekar"
  choices = ["Live Voice","All Done!"]
  reply   = buttonbox(msg,image=image,choices=choices)
  if reply ==choices[0]:
        func()
  if reply == choices[1]:
        quit()
  
