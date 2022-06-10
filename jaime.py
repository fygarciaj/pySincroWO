import speech_recognition as sr
import pyttsx3


name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            rec = rec.lower()
            if name in rec:
                print(rec)
    except: 
        pass
    return rec

def run():
    rec = listen()
    if 'reproduce' in rec:
        talk(rec)
        print('Reproducciendo')

run()