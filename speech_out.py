from gtts import gTTS
import commands
import time
import os
# from tempfile import TemporaryFile

def speech_output(text, lang):
	file = gTTS(text=text, lang=lang)
	filename = "temp.mp3"
	file.save(filename)
	commands.getstatusoutput('mpg123 -q temp.mp3')
	# p.kill()



# if __name__ == '__main__':
# 	speech_output('there is a person to your left', 'en')