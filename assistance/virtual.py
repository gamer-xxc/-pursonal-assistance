import speech_recognition as sr
import pyttsx3
import datetime
import time
import json
import requests

CONFIG_FILE = 'config.json'

def get_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_config():
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def get_prefered_voice():
    config = get_config()
    if language  not in config:

        print("tell what language you comfortable with")
        language = input().strip()
        config['language'] = language
        save_config()
    return config['language']    





engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
audio=engine.getProperty('rate')
engine.setProperty('rate',200)
audio=engine.getProperty('volume')
engine.setProperty('volume',1.5)



def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hey,Good Morning karthik")
    
    elif hour>=12 and hour<18:
        speak("Hey,Good Afternoon karthik")
        
    else:
        speak("Hey,Good Evening karthik")
        

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


wishMe()
speak("cheppu!! eppudu nekosam nennu em cheyamantav")



if __name__=='__main__':


    while True:
        
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('ok neku inka emayina avasaram vuntey nenu vunna  ani matram ani marchipoku!! HAHAHAHA bye')
            break



time.sleep(3)












