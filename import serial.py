import os
import time
import tkinter.messagebox
from datetime import datetime as dt
from os import getenv
from tkinter import *
from tkinter import font as tkFont

import cv2
import numpy as np
import PIL
import serial
from PIL import Image, ImageTk

Range = 300
MODEL = 'cnn'
TOLERANCE = 0.10

unlock1=True
video_capture = cv2.VideoCapture(0)
width, height = 700, 700
home_dir = getenv('HOME')
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit()) 
lmain = Label(root)
lmain.grid(row=0,column=0)



def show_frame():
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)
   

def printcamera():
        a=tkinter.messagebox.askyesno("Face Capture ","Camera will take a photo of your face to Lock locker 2, Do you want to Proceed ? ")
        print(a)
        global unlock1
        time.sleep(1.5)
        if a==True:

            print("capture picture")
            ret, frame = video_capture.read()
 
            if ret:
                 cv2.imwrite('hello.jpg',frame)

                
              
                
                 print("Fuck")

                 

                 update_button()
                 unlock1=False
                 
                 tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 2 will be Locked ")
                 label['text']="Capture Complete"
                 time.sleep(1.5)
                 label['text']="Locker Locked"
        



def Locker1():
    global unlock1
    global button3
    if  unlock1==True:
        
        printcamera()
        


def capture_image():
    '''
    Starts the camera, Captures the image, saves it & stops
    '''

    file_name = home_dir + '/image_captured/image_' + str(dt.now()) + '.jpg'

    video_capture.start()
    image = video_capture.get_image()
    cv2.image.save(image, file_name)
    video_capture.stop()
       
        

      
        



def update_button():
    button3['text']="Locker 2 Locked"

def update_button_UNlock():
    button3['text']="Vecant Locker 2"

helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)
    



label=Label(root,text="Vehicle",font=('Helvetica', '15'))

label.grid(row=3,column=0)


show_frame()
root.mainloop()
Arduino = serial.Serial('COM3',9600, timeout=10)

while True:
    if (Arduino.inWaiting()>0):
        myData = Arduino.readline()
        print(myData)

        try:
            myData = int(float(myData))

            if myData <= Range:
                capture_image()
                print(myData)

        except BaseException:
            print(Message)
       

    












