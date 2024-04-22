from keyboard import press
from keyboard import press_and_release
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(": Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f': Your Command : {query}\n')
        return query.lower()

    except Exception as e:
        print(e)
        return ""


def WindowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        press_and_release('windows + m')

    elif 'mini' in query:

        press_and_release('windows + m')


    elif 'show start' in query:

        press('windows')

    elif 'settings' in query:

        press_and_release('windows + i')

    elif 'search' in query:

        press_and_release('windows + s')

    elif 'screenshot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')

    else:
        Speak("Sorry , No Command Found!")