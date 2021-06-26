import pyttsx3
from pygame import mixer 
import speech_recognition as sr
mixer.init()

mixer.music.set_volume(0.13)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def Take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        mixer.music.load('D:\\riddhi\\voices\\sound8.mp3')
        mixer.music.play()
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'''You are said: "{query}"\n''')
    except Exception as e:
        print("\nI could not recognize that, pls say that again")
        speak("I could not recognize that, please say that again")
        return "-"
    return query

