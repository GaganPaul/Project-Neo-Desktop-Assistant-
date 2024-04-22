import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import webbrowser as web
import bs4
import pyttsx3
import requests
import wolframalpha
import os
from pytube import YouTube
from pyautogui import click, hotkey
import pyperclip
from time import sleep




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("   ")

def GoogleSearch(term):
    query = term.replace("neo","")
    query = query.replace("what is","")
    query = query.replace("what is ","")
    query = query.replace("how to","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")
    writeab = str(query)

    with open("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\Text-Features\\Data.txt", "a") as file:
        file.write(writeab)

    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        pywhatkit.search(Query)
        search = wikipedia.summary(Query, 2)
        Speak(f": According to the Internet: {search}")


def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)

    Speak('This is what I found for your search')

    pywhatkit.playonyt(term)

    Speak('This may also help you')

def SpeedTest():

    os.startfile("C:\\Users\\Gagan\\Desktop\\BlackHole\\Complete NEO series\\DataBase\\Gui_Programs\\SpeedTestGui.py")

def WolfRam(query):

    
    api_key = '8WYQU6-4266QYW68L'

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:
        Answer = next(requested.results).text
        return Answer

    except:
        Speak("No Data Found.") 

def Calculator(query):

    Term = str(query)
    Term = Term.replace("neo","")
    Term = Term.replace("multiplied","*")
    Term = Term.replace("add","+")
    Term = Term.replace("substract","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("multiply","*")
    Term = Term.replace("divided","/")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Final = str(Term)

    try:
        result = WolfRam(Final)
        Speak(f"{result}")

    except:
        Speak("No Data Found.")    

def Temp(query):

    Term = str(query)

    Term = Term.replace("neo ","")
    Term = Term.replace("what is the ","")
    Term = Term.replace("temperature ","")
    Term = Term.replace("in ","")

    temp_query = str(Term)

    if 'outside' in temp_query:

        var1 = "temperature in Bengaluru"
        
        answer = WolfRam(var1)

        Speak(f"{var1} is {answer}")

    else:

        var2 = "temperature in " + temp_query

        ans = WolfRam(var2)

        Speak(f"{var2} is {ans}")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")
    Date = Date.replace(" zero ","0")
    Date = Date.replace(" one ","1")
    Date = Date.replace(" two ","2")
    Date = Date.replace(" two ","2")
    Date = Date.replace(" three ", " 3 ")
    Date = Date.replace(" four ", " 4 ")
    Date = Date.replace(" five ", " 5 ")
    Date = Date.replace(" six ", " 6 ")
    Date = Date.replace(" seven ", " 7 ")
    Date = Date.replace(" eight ", " 8 ")
    Date = Date.replace(" nine ", " 9 ")
    Date = Date.replace(" ten ", " 10 ")
    Date = Date.replace(" eleven ", " 11 ")
    Date = Date.replace(" twelve ", " 12 ")
    Date = Date.replace(" thirteen ", " 13 ")
    Date = Date.replace(" fourteen ", " 14 ")
    Date = Date.replace(" fifteen ", " 15 ")
    Date = Date.replace(" sixteen ", " 16 ")
    Date = Date.replace(" seventeen ", " 17 ")
    Date = Date.replace(" eighteen ", " 18 ")
    Date = Date.replace(" nineteen ", " 19 ")
    Date = Date.replace(" twenty ", " 20 ")
    Date = Date.replace(" twenty-one ", " 21 ")
    Date = Date.replace(" twenty-two ", " 22 ")
    Date = Date.replace(" twenty-three ", " 23 ")
    Date = Date.replace(" twenty-four ", " 24 ")
    Date = Date.replace(" twenty-five ", " 25 ")
    Date = Date.replace(" twenty-six ", " 26 ")
    Date = Date.replace(" twenty-seven ", " 27 ")
    Date = Date.replace(" twenty-eight ", " 28 ")
    Date = Date.replace(" twenty-nine ", " 29 ")
    Date = Date.replace(" thirty ", " 30 ")
    Date = Date.replace(" thirty-one ", " 31 ")
    Date = Date.replace("zero","0")
    Date = Date.replace("one","1")
    Date = Date.replace("two","2")
    Date = Date.replace("three", " 3 ")
    Date = Date.replace("four", " 4 ")
    Date = Date.replace("five", " 5 ")
    Date = Date.replace("six", " 6 ")
    Date = Date.replace("seven", " 7 ")
    Date = Date.replace("eight", " 8 ")
    Date = Date.replace("nine", " 9 ")
    Date = Date.replace("ten", " 10 ")
    Date = Date.replace("eleven", " 11 ")
    Date = Date.replace("twelve", " 12 ")
    Date = Date.replace("thirteen", " 13 ")
    Date = Date.replace("fourteen", " 14 ")
    Date = Date.replace("fifteen", " 15 ")
    Date = Date.replace("sixteen", " 16 ")
    Date = Date.replace("seventeen", " 17 ")
    Date = Date.replace("eighteen", " 18 ")
    Date = Date.replace("nineteen", " 19 ")
    Date = Date.replace("twenty", " 20 ")
    Date = Date.replace("twenty-one", " 21 ")
    Date = Date.replace("twenty-two", " 22 ")
    Date = Date.replace("twenty-three", " 23 ")
    Date = Date.replace("twenty-four", " 24 ")
    Date = Date.replace("twenty-five", " 25 ")
    Date = Date.replace("twenty-six", " 26 ")
    Date = Date.replace("twenty-seven", " 27 ")
    Date = Date.replace("twenty-eight", " 28 ")
    Date = Date.replace("twenty-nine", " 29 ")
    Date = Date.replace("thirty", " 30 ")
    Date = Date.replace("thirty-one", " 31 ")

    return str(Date) 







    




