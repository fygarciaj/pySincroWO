import speech_recognition as sr
import pyttsx3


name = 'alexa'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

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
            print(rec)
            if name in rec:
                rec.replace(name, '')
                print(rec)
            return rec
    except sr.RequestError: 
        print(sr.RequestError)
    

def run():
    rec = listen()
    match rec:
        case 'reproduce':
            talk(rec)
            print('Reproducciendo')
        case 'llama':
            print('Llamando a...')
        case _:
            print('No entiendo...')


run()