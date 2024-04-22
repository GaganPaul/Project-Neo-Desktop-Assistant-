import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def Pass(pass_inp):

       password = "shadow"

       passss  = str(password)

       if passss==str(pass_inp):

              Speak("Access Granted .")

              import Main

       else:
              Speak("Access Not Granted .")

if __name__ == "__main__" :

       Speak("I am Password Protected .")

       Speak("Kindly Provide The Password To Access .")

       passw = input(": Enter The Password: ")

       Pass(passw)

def TaskExe():

    while True:

        query = TakeCommand()

        if query is  ".":
            continue
        

        if 'google search' in query:

            GoogleSearch(query)

        elif 'youtube search' in query:

            Query = query.replace("neo","")

            query = Query.replace("youtube search","")

            from Features import YouTubeSearch

            YouTubeSearch(query)

        elif 'set alarm' in query:

            from Features import Alarm

            Alarm(query)

        elif 'download' in query:

            from Features import DownloadYouTube

            DownloadYouTube()
            
        elif 'speed test' in query:

            from Features import SpeedTest

            SpeedTest()
         
        elif 'temperature' in query:

            from Features import Temp

            Temp(query)

        elif 'calculate' in query:

            from Features import Calculator

            Calculator(query)

        elif 'wolfram' in query:

            from Features import WolfRam

            Result = WolfRam(query)

            Speak(Result) 

        elif 'chrome' in query:

            from Automations import ChromeAuto

            ChromeAuto(query)

        elif 'new tab' in query:

            press_and_release('ctrl + t')

        elif 'close tab' in query:

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

        elif 'switch tab' in query:

            tab = query.replace("switch tab ", "")
            Tab = tab.replace("to","")
            
            num = Tab

            bb = f'ctrl + {num}'

            press_and_release(bb)

        elif 'open' in query:

            name = query.replace("open ","")

            NameA = str(name)

            if 'youtube' in NameA:

                web.open("https://www.youtube.com/")

        
            else:

                string = "https://www." + NameA + ".com"

                string_2 = string.replace(" ","")

                web.open(string_2)
    
    
        elif 'youtube' in query:

            from Automations import YouTubeAuto

            YouTubeAuto(query)

        
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

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
                
        elif 'search' in query:

            click(x=616, y=133)

            Speak("What To Search ?")

            search = TakeCommand()

            write(search)

            sleep(0.8)

            press('enter')

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')    

        
            

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa_Api import NasaNews

            NasaNews(Value) 

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

            elif 'close' in query:
                
                break
TaskExe()