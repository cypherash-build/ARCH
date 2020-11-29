import speech_recognition as sr
import time
r = sr.Recognizer()

with sr.Microphone() as source:
    time.sleep(1)
    while[1]:

        print("************  SAY SOMETHING ************")
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(f''' HERE IS WHAT YOU SAID :-
                                
                                 
                                  {voice_data}
        
        
        
                                  ''')

        except sr.UnknownValueError:
            print("error")
