from google.cloud import speech
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import io

def recording(duration):
	fs = 44100 #sampling frequency
	print("say something bitch")
	myRec = sd.rec(duration*fs, samplerate=fs, channels=2, dtype="float64")
	sd.wait()
	response = 'response.wav'
	wav.write(response, fs, myRec)

def recognize(audioFile):
	client = speech.SpeechClient()
	config = speech.types.RecognitionConfig(
		encoding=speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
		language_code='en-US',
		sample_rate_hertz=44100,
	)
	with io.open(audioFile, 'rb') as stream:
		content = stream.read()

	stream = [content]
	requests = (speech.types.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream)
	streaming_config = speech.types.StreamingRecognitionConfig(config=config)
	responses = client.streaming_recognize(streaming_config, requests)

	output=""
	# results = sample.streaming_recognize(config=speech.types.StreamingRecognitionConfig(config=config), req)
	for response in responses:
		for result in response.results:
			output = result.is_final
			print(output)
			break

	return output 

if __name__ == '__main__':
	recording(3)
	output = recognize('response.wav')
	print(output)
