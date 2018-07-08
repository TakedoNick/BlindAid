# Naive Assistant Phrase Generation
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 2018

@author: nick
"""

def phraseGen(position, obj):
	vowels = ['a','e','i','o','u']
	if obj=='nothing':
		if(position=='center'):
			text = 'There is nothing in front of you.'
		else:
			text = 'There is nothing to your ' + position
	else:
		if(position!="center"):
			if(obj[0] in vowels):
				text = "There is an " + obj + " on your " + position
			else:
				text = "There is a " + obj + " to your " + position
		else:
			if(obj[0] in vowels):
				text = "There is an " + obj + " in front of you"
			else:
				text = "There is a " + obj + " in front of you"
	return text


def getInfo(question):
	centerWords = ['front', 'proceed', 'forward']
	leftWords = ['left']
	rightWords = ['right']
	
	for i in centerWords:
		if (i in question):
			return 'center'

	for i in leftWords:
		if i in question:
			return 'left'

	for i in rightWords:
		if i in question:
			return 'right'