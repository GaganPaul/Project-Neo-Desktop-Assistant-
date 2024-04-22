import random
import speech_recognition as sr
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


Hello = ('hello', 'hey', 'neo', 'hi')

reply_Hello = ('Hello, I am Neo.',
               "Hey, what's up?",
               "Hey, how are you?",
               "Hello, nice to meet you again.")

Bye = ('bye', 'exit', 'sleep', 'go', 'close')

reply_bye = ("It's okay.",
             "It was nice to meet you.",
             "Bye.",
             "Thanks.",
             "Okay.")

How_Are_You = ('how are you', 'are you fine')

reply_how = ('I am fine.',
             "Excellent.",
             "Absolutely fine.",
             "I'm fine.",
             "Thanks for asking.")

nice = ('nice', 'good', 'thanks')

reply_nice = ('Thanks.',
              "It's okay.",
              "Your welcome.") 

Functions = ['functions', 'abilities', 'what can you do', 'features', 'what are your features']

reply_Functions = ('I can perform many tasks or varieties of tasks. How can I help you?',
                   'Let me ask you first, how can I help you?',
                   'If you want me to tell my features, call: print features!')

sorry_reply = ("Sorry, that's beyond my abilities.",
               "Sorry, I can't do that.",
               "Sorry, that's above me.")

def ChatterBot(Text):
    Text = str(Text).lower()

    if any(word in Text for word in Hello):
        reply = random.choice(reply_Hello)
        return reply

    elif any(word in Text for word in Bye):
        reply = random.choice(reply_bye)
        return reply

    elif any(word in Text for word in How_Are_You):
        reply_ = random.choice(reply_how)
        return reply_

    elif any(word in Text for word in Functions):
        reply___ = random.choice(reply_Functions)
        return reply___

    elif any(word in Text for word in nice):
        reply__ = random.choice(reply_nice)
        return reply__    

    else:
        return random.choice(sorry_reply)

value = ChatterBot('hello')
Speak(value)
print(value)
 