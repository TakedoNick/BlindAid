import speech_recognition as sr
import time

def speech():
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		audio = rec.listen(source)
	# time.sleep(duration)
	try:
		result = rec.recognize_google(audio)
		text = result.encode('utf-8')
		print(text)
		return text
	except:
		pass	

	

# if __name__ == '__main__':
# 	output = speech()
# 	print(output)