import pyttsx3
from gtts import gTTS
import speech_recognition as sr
import webbrowser as web
from pyautogui import click
from keyboard import press_and_release, write, press
from datetime import datetime
from Features import GoogleSearch, YouTubeSearch, SpeedTest, Temp, Calculator, WolfRam, DateConverter
from DataBase.ChatBot.ChatBot import ChatterBot
from Nasa_Api import NasaNews
from time import sleep
from SpeakFromFile import SpeakFromFile 
from Jokes import tell_joke
from Automations import automate_notepad
from WindowAuto import WindowsAuto


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


def TaskExe():

    while True:

        try:
            query = TakeCommand()

            if query == "":
                continue

            if 'google search' in query:
                 Query = query.replace("neo", "")
                 query = Query.replace("google search", "")
                 GoogleSearch(query)

            elif 'youtube search' in query:
                Query = query.replace("neo", "")
                query = Query.replace("youtube search", "")
                YouTubeSearch(query)

            elif 'tell me a joke' in query:
                tell_joke()

            elif 'recite' in query:
                SpeakFromFile('add your path\\ReadFiles\\')

            elif 'speed test' in query:
                SpeedTest()

            elif 'temperature' in query:
                Temp(query)

            elif 'calculate' in query:
                Calculator(query)

            elif 'wolfram' in query:
                Result = WolfRam(query)
                Speak(Result)

            elif 'new tab' in query:
                press_and_release('ctrl + t')

            elif 'exit tab' in query:
                press_and_release('ctrl + w')

            elif 'new window' in query:
                press_and_release('ctrl + n')

            elif 'history' in query:
                press_and_release('ctrl + h')

            elif 'download' in query:
                press_and_release('ctrl + j')

            elif 'bookmark' in query:
                press_and_release('ctrl + d')
                press('enter')

            elif 'incognito' in query:
                press_and_release('Ctrl + Shift + n')

            elif 'open' in query:
                name = query.replace("open ", "")
                NameA = str(name)
                if 'youtube' in NameA:
                    web.open("https://www.youtube.com/")
                else:
                    string = "https://www." + NameA + ".com"
                    string_2 = string.replace(" ", "")
                    web.open(string_2)

            elif 'pause' in query:
                press('space bar')

            elif 'resume' in query:
                press('space bar')

            elif 'full screen' in query:
                press('f')

            elif 'film screen' in query:
                press('t')

            elif 'skip' in query:
                press('l')

            elif 'back' in query:
                press('j')

            elif 'previous' in query:
                press_and_release('SHIFT + p')

            elif 'next' in query:
                press_and_release('SHIFT + n')

            elif 'search' in query:
                click(x=616, y=133)
                Speak("What To Search?")
                search = TakeCommand()
                write(search)
                sleep(0.8)
                press('enter')

            elif 'mute' in query:
                press('m')

            elif 'unmute' in query:
                press('m')

            elif 'what is the time' in query:
                import datetime
                now = datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")
                statement = f"The current time is {current_time}"
                Speak(statement)      

            elif 'what is the date' in query:
                import datetime
                now = datetime.datetime.now()
                current_date = now.strftime("%Y-%m-%d")
                statement = f"The current date is {current_date}"
                Speak(statement)

            elif 'windows' in query:
                WindowsAuto(query)    
  
            elif 'take a note' in query:
                automate_notepad()

            elif 'space news' in query:
                Speak("Tell Me The Date For News Extracting.")
                Date = TakeCommand()
                Value = DateConverter(Date)
                NasaNews(Value)

            else:
                reply = ChatterBot(query)
                Speak(reply)

                if 'bye' in query or 'exit' in query or 'close' in query:
                    Speak("See you later!")
                    break
                

        except Exception as e:
            print(e)
            Speak("Sorry, I couldn't process your request. Please try again.")

def start_task_execution():
    Speak("How can I assist you today?")
    TaskExe()
