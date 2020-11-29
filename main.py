import speech_recognition as sr
import webbrowser
import time
from time import ctime

r = sr.Recognizer()


def record_audio(ask=False):
    print("How may i help You?")
    with sr.Microphone() as source:
        if ask:
            print("what is it sir")
        audio = r.listen(source)
        voice_data = ' '
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("sorry , didn't catch that")
        except sr.RequestError as e:
            print("Failed".format(e))
        return voice_data


def respond(voice_data):
    if "name" in voice_data:
        print("Hello , sir . My name is ARCH ")
    if "time" in voice_data:
        print(ctime() + " , sir")
    if 'find' in voice_data:
        search = record_audio(ask=True)
        url = "https://google.com/search?q="+search
        webbrowser.get().open(url)
        print("Here's what I found for you....")
    if 'place' in voice_data:
        search = record_audio(ask=True)
        url = "https://google.com/maps/place/"+search+"/&amp;"
        webbrowser.get().open(url)
        print("Here's what I found for you....")

time.sleep(1)
print("I'm Listening")
while(1):
    voice_data = record_audio()
    respond(voice_data)




