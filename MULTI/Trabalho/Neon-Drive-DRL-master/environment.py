# -*- coding: utf-8 -*-
''' Modules for installation -> torch, torchvision, numpy, keyboard, cv2, mss.
    Use pip3 install 'module'.
'''
from skimage.filters import threshold_triangle, threshold_sauvola, threshold_niblack
from skimage import img_as_ubyte
import torchvision.transforms as T
from cv2 import VideoCapture, VideoWriter
from PIL import Image
import numpy as np
import threading
import keyboard
import noise
import torch
import cv2
import time
import mss

CSTBinary = 25

resize = T.Compose([T.ToPILImage(),
                    T.Resize(40, interpolation=T.InterpolationMode.BILINEAR),
                    T.ToTensor()])

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def histogram(image):
    ''' Histogram generate function
    '''
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist


class env():
    def __init__(self, resolution, noise=False, noiseType='s&p'):
        self.w, self.h = resolution
        self.movements = ["a", "d", "w"]
        self.noise = noise
        self.noiseType = noiseType

        img = cv2.imread('gameover.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.hist_restart = histogram(img)

        imageCapture = threading.Thread(name='imageCapture', target=self.imageCapture)
        imageCapture.setDaemon(True)
        imageCapture.start()

        videoCapture = threading.Thread(name='videoCapture', target=self.videoCapture)
        videoCapture.setDaemon(True)
        videoCapture.start()

    def imageCapture(self):

        global CSTBinary

        monitor = {'left': 0, 'top': 0, 'width': self.w, 'height': self.h}
        with mss.mss() as sct:
            while True:
                sct_img = sct.grab(monitor)
                img_np = np.array(sct_img)
                if self.noise:
                    img_np = noise.noisy(img_np, self.noiseType)
                    img_np = cv2.normalize(img_np, None, 0, 255, cv2.NORM_MINMAX).astype('uint8')
                gray_frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
                cropped_bw_frame = gray_frame[int(7*(self.h/13.0)):int(self.h-(self.h/5)), int(self.w/5):int(self.w-(self.w/5))]
                threash_triangle = threshold_triangle(cropped_bw_frame)
                binary_triangle = cropped_bw_frame > threash_triangle
                #binary_triangle = gray_frame > 25
                binary_triangle = img_as_ubyte(binary_triangle)
                resized_bw_frame = cv2.resize(binary_triangle, (int(160), int(90)), interpolation=cv2.INTER_AREA)
                self.bw_frame = cv2.bitwise_not(resized_bw_frame)
                self.rgb_frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                self.cropped_bw_to_video = cropped_bw_frame
                _ = cv2.waitKey(1)

    def videoCapture(self):
        framesPSec = 60
        totalFrames = framesPSec*10
        timeSecFrames = 1/framesPSec

        # waits to select game
        time.sleep(5)

        h, w = self.bw_frame.shape
        outFrames = []

        # capture real time frames to create a video
        for _ in range(totalFrames):
            time.sleep(timeSecFrames)
            outFrames.append(self.cropped_bw_to_video)
        
        self.createVideo(threshold_triangle, 'threshold_triangle.mp4', outFrames, w, h)
    
    def createVideo(self, thresholdFunction, videoName, videoFrames, weight, height):

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        outVideo = VideoWriter(videoName, fourcc, 120.0, (weight, height))

        for frame in videoFrames:
            threashold_frame = thresholdFunction(frame)
            binary_frame = frame > threashold_frame
            #binary_frame = gray_frame > 25
            binary_frame = img_as_ubyte(binary_frame)
            resized_bw_frame = cv2.resize(binary_frame, (int(160), int(90)), interpolation=cv2.INTER_AREA)
            bw_frame = cv2.bitwise_not(resized_bw_frame)
            outVideo.write(cv2.cvtColor(bw_frame, cv2.COLOR_BGR2RGB))
        
        outVideo.release()

    def reset(self):
        time.sleep(0.4)
        #keyboard.send("enter")
        time.sleep(3.5)
        self.initial_time = time.time()

    def step(self, action):
        done = False
        #keyboard.send(self.movements[action])
        time.sleep(0.3)
        hist = histogram(self.rgb_frame)
        comparison = cv2.compareHist(self.hist_restart, hist, cv2.HISTCMP_BHATTACHARYYA)
        if comparison > 0.15:
            rew = 0
            multiplication = time.time() - self.initial_time
            if multiplication >= 2:
                rew = 1
        else:
            done = True
            rew = 0
        return [], rew, done, []

    def get_screen(self):
        return resize(self.bw_frame).unsqueeze(0).to(device)
