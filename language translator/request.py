import speech_recognition as sr

recognizer = sr.Recognizer()

''' recording the sound '''

with sr.Microphone() as source:
    print("Adjusting noise ")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Recording for 4 seconds")
    recorded_audio = recognizer.listen(source, timeout=4)
    print("Done recording")

''' Recognizing the Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)
    
from googletrans import Translator

translater= Translator()

out=translater.translate(text, dest="hi")

from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
text=out

language = 'en' #hindi
speech = gTTS(text = text, lang = language, slow = False)
speech.save('medium_hindi.wav')
#to play string in wav
os.system('start medium_hindi.wav')