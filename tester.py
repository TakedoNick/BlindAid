import subprocess
import commands

# # os.system("./darknet detector cfg/yolov2.cfg yolov2.weights data/horses.jpg")

# output = subprocess.check_output(["./darknet","detect","cfg/yolov2.cfg","yolov2.weights","data/horses.jpg"])

# print(output)



# output = commands.getstatusoutput('python3 darknet.py')

output = subprocess.Popen(["python3","darknet.py"], stdout=subprocess.PIPE)
out, err = output.communicate()

# output_proc = subprocess.check_output(["python3","darknet.py"])
# output = output_proc.decode("utf-8")
# # output = "[(b'bicycle', 0.8292059302330017, (344.4787292480469, 279.78228759765625, 449.60760498046875, 285.79168701171875)), (b'dog', 0.8134602904319763, (221.8997802734375, 369.119384765625, 197.4265594482422, 322.42303466796875)), (b'truck', 0.7448830008506775, (575.9268188476562, 128.1943359375, 258.155517578125, 91.25247192382812))]"
# output = output.decode("utf-8")
# objAccu = dict()
# objPos = dict()
# while True:
# 	if(output.find("(b'")==-1):
# 		break
# 	else:
# 		pos = output.find("(b'")
# 		output = output[pos + 3:]
		
# 		endPos = output.find("'")
# 		tempObject = output[:endPos]
# 		output = output[endPos + 3:]
		
# 		newEndPos = output.find(",")
# 		tempAccuracy = output[:newEndPos]
# 		output = output[newEndPos+1:]
		
# 		objAccu[tempObject] = float(tempAccuracy)*100

# 		pos = output.find("(")
# 		output = output[pos + 1:]
# 		endPos = output.find(",")
# 		tempX = output[:endPos]

# 		objPos[tempObject] = tempX

# print(objAccu)
# print(objPos)
# # print("\n\n")
# # print(output)


# from google.cloud import speech
# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile as wav
# import io

# # subprocess.call(['avconv', '-i', 'response.wav', '-y', '-ar', '48000', '-ac', '1', 'response.flac'])

# client = speech.SpeechClient()
# results = client.recognize(
# 	audio=speech.types.RecognitionAudio(
# 		uri='/home/nick/Documents/YOLO v2 - Darknet/darknet/response.flac',
# 	),
# 	config=speech.types.RecognitionConfig(
# 		encoding='LINEAR16',
# 		language_code='en-US',
# 		sample_rate_hertz=44100,
# 	),
# )

# for result in results:
# 	for alternatives in result.alternatives:
# 		print(alternative.transcript)
# 		break




# config = speech.types.RecognitionConfig(
# 	encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
# 	language_code='en-US',
# 	sample_rate_hertz=16000,
# )
# with io.open('response.wav', 'rb') as stream:
# 	content = stream.read()

# stream = [content]
# requests = (speech.types.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream)
# streaming_config = speech.types.StreamingRecognitionConfig(config=config)
# responses = client.streaming_recognize(streaming_config, requests)

# # results = sample.streaming_recognize(config=speech.types.StreamingRecognitionConfig(config=config), req)
# for response in responses:
# 	for result in response.results:
# 		print('Finished: {}'.format(result.is_final))
# 		print('Stability: {}'.format(result.stability))
# 		alternatives = result.alternatives
# 		# The alternatives are ordered from most likely to least.
# 		for alternative in alternatives:
# 			print('Confidence: {}'.format(alternative.confidence))
# 			print(u'Transcript: {}'.format(alternative.transcript))


