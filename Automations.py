import time
import pyperclip
import pyautogui
import speech_recognition as sr
from datetime import datetime
import os
import pyttsx3

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


def speech_to_text():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            Speak("I am listening.")
            r.adjust_for_ambient_noise(source) 
            audio = r.listen(source, phrase_time_limit=5)  
            try:
                text = r.recognize_google(audio)
                print("You said:", text)
                return text
            except sr.UnknownValueError:
                Speak("Sorry, I couldn't process your request. Please try again.")
            except sr.RequestError as e:
                Speak("Sorry, an error occurred. {0}".format(e))


def automate_notepad():
  
    os.startfile("notepad.exe")
    time.sleep(1)

   
    text = speech_to_text()

    while text is not None:
        if text.lower() == "quit":
            break

        if text is not None:
            pyperclip.copy(text)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

       
        text = speech_to_text()

 
    current_time = datetime.now().strftime("%H-%M")
    filename = current_time + "-note.txt"
    save_path = # Replace with your desired folder path
    file_path = save_path + filename

    pyautogui.hotkey('ctrl', 's')
    time.sleep(1)
    pyautogui.typewrite(file_path)
    pyautogui.press('enter')


    pyautogui.hotkey('alt', 'f4')







