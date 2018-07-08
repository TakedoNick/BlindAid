#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 2018

@author: nick
"""

# import commands
import subprocess
import time
import pyautogui
import cv2
import os
import psutil

import positionDet
import phraseGenerator
import speak
import speech_out


# import pyttsx
# def speechOutput(phrase):
# 	engine = pyttsx.init()
# 	engine.setProperty('rate', 125)
# 	# voices = engine.getProperty('voices')
# 	engine.setProperty('voice', 'english+f4')
# 	engine.say(phrase)
# 	engine.runAndWait()
# 	return engine.stop()

lang = 'en-GB'

while True:
	positionDet.camCapture()
	# output_proc = subprocess.check_output(["python3","darknet.py"])
	# output = output_proc.decode("utf-8")
	output_proc = subprocess.Popen(["python3","darknet.py"], stdout=subprocess.PIPE)
	# subprocessPID = output_proc.pid
	output, err = output_proc.communicate()
	objAccu = dict()
	objPos = dict()
	accuracy = list()
	position = list()
	objects = list()
	
	# String Manipulation
	while True:
		if(output.find("(b'")==-1):
			break
		else:
			pos = output.find("(b'")
			output = output[pos + 3:]
		
			endPos = output.find("'")
			tempObject = output[:endPos]
			output = output[endPos + 3:]
			# objects.append(tempObject)
		
			newEndPos = output.find(",")
			tempAccuracy = output[:newEndPos]
			output = output[newEndPos+1:]
			# accuracy.append(tempAccuracy)
		
			objAccu[tempObject] = float(tempAccuracy)*100

			pos = output.find("(")
			output = output[pos + 1:]
			endPos = output.find(",")
			tempX = float(output[:endPos])
			# position.append(tempX)
			objPos[tempObject] = tempX

	# output = commands.getstatusoutput('./darknet detector test cfg/coco.data cfg/yolov2.cfg yolov2.weights cam.jpg')
	# time.sleep(1.5)
	# pyautogui.press('q')
	xLengthImg = float(cv2.imread('cam.jpg').shape[1:2][0])
	divisor = xLengthImg/3
	objLocation = dict()
	for key in objPos.keys():
		if(objPos[key]<=divisor):
			objLocation[key]="left"
		elif(objPos[key]>=divisor*2):
			objLocation[key]="right"
		else:
			objLocation[key]="center"

	#Speech according to highest Accuracy Predicted
	positionKey = [0,0,0] #[0,0,1] - right
	for key in objAccu.keys():
		phrase = phraseGenerator.phraseGen(objLocation[key], key)
		posTemp = objLocation[key]
		if posTemp=='left':
			positionKey[0]=1
		elif posTemp=='center':
			positionKey[1]=1
		else:
			positionKey[2]=1
		print(phrase)
		speech_out.speech_output(phrase, lang)

		
		question = speak.speech()
		location = phraseGenerator.getInfo(question)
		objInLocation = ''
		for k in objLocation.keys():
			if location==objLocation[k]:
				objInLocation = str(k)
				break
			else:
				objInLocation='nothing'

		phrase = phraseGenerator.phraseGen(location, objInLocation)
		print(phrase)
		speech_out.speech_output(phrase, lang)

		positionKey = [0,0,0]
		#TODO put speech output here
		#time.sleep(2)

	# p = psutil.Process(subprocessPID+1)
	# p.terminate()
	
	



# obj = raw_input('Name your Object: (Example - dog): ')

# obj+=':'

# if obj in pred_names:
# 	execfile("results/sample.py")
# else:
# 	print("The object is not present in the given image.")
