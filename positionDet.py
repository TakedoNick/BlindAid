#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 2018

@author: nick
"""

import cv2
import time

def camCapture():
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	cv2.imwrite("cam.jpg", frame)
	# time.sleep(2)
	cap.release()

# def objectPosition(img):
# 	cv2.imread("predictions.jpg")

