import os
import pyttsx3
import speech_recognition as sr
import PyPDF2

def SpeakFromFile(folder_path):
   
    files = os.listdir(folder_path)

    print("Available files:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

    file_index = GetVoiceInput("Please say the number of the file you want to read.")

    try:
        file_index = int(file_index)
        if file_index < 1 or file_index > len(files):
            print("Invalid file index.")
            return

        file_name = files[file_index-1]
        file_path = os.path.join(folder_path, file_name)

        text = ReadPdf(file_path)
        if text:
            Speak(text)
            OpenFile(file_path)
            print(f"Currently reciting: {file_name}")
    except ValueError:
        print("Invalid file index.")
    except FileNotFoundError:
        print(f"File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def ReadPdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def Speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def GetVoiceInput(prompt):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(prompt)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")

        number_mapping = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
            "eleven": "11",
            "twelve": "12",
            "thirteen": "13",
            "fourteen": "14",
            "fifteen": "15",
            "sixteen": "16",
            "seventeen": "17",
            "eighteen": "18",
            "nineteen": "19",
            "twenty": "20"
        }

        if text.lower() in number_mapping:
            text = number_mapping[text.lower()]

        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't process your request. Please try again.")
        Speak("Sorry, I couldn't process your request. Please try again.")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")

    return ""


def OpenFile(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Unable to open the file: {e}")

def Stop():
    Speak("Stopping the program. Goodbye!")
    exit()

if __name__ == "__main__":
    folder_path = "add your path\\Speak\\ReadFiles\\"

    while True:
        command = GetVoiceInput("How can I assist you?")

        if "recite" in command:
            SpeakFromFile(folder_path)
        elif "stop" in command:
            Stop()
        else:
            print("Command not recognized. Please try again.")

