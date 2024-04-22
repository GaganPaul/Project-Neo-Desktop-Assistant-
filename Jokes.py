import random
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

def query(user, query):
    query = query.replace("neo", "")


def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "I used to play piano by ear, but now I use my hands!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't some couples go to the gym? Because some relationships don't work out!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What's the best time to go to the dentist? Tooth hurty!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "How do you organize a space party? You planet!",
        "What do you call a fake noodle? An impasta!",
        "Why did the math book look sad? Because it had too many problems!"
    ]

    joke = random.choice(jokes)
    Speak(joke)


