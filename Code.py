from translate import Translator
from gtts import gTTS
import speech_recognition as spr
import os


cwd = os.getcwd()
print("the current directory is :{0}".format(cwd))
voice1=spr.Recognizer()
voice2=spr.Microphone()
with voice2 as source :
     print("Please speak hello to activate our translator\n")
     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
     voice1.adjust_for_ambient_noise(source,duration=0.6)
     voice3=voice1.listen(source)
     RecText=voice1.recognize_google(voice3)
     RecText=RecText.lower()
if 'hello' in RecText:
    with voice2 as source:
        print("Please speak a sentance")
        voice1.adjust_for_ambient_noise(source,duration=0.6)
        voice3=voice1.listen(source)
        framesentance1=voice1.recognize_google(voice3)
        translator=Translator(to_lang="Hindi",from_lang="English")
        trans=translator.translate(framesentance1)
        print(trans)
        speak=gTTS(text=trans,lang='hi',slow=False)
        speak.save("captured_voice.mp3")
        os.system("start captured_voice.mp3")
  
