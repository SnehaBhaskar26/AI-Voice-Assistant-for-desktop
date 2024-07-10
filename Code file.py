#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import times 
import speech_recognition as sr 
import pyttsx3 
import pywhatkit 
import datetime 
import wikipedia 
 
listener = sr.Recognizer() 
engine = pyttsx3.init() 
voices = engine.getProperty('voices') 
engine.setProperty('voices', voices[1].id) 
def talk(text): 
    engine.say(text) 
    engine.runAndWait() 
 
def take_command(): 
    try: 
        with sr.Microphone() as source: 
            print('listening...') 
            voice = listener.listen(source) 
            command = listener.recognize_google(voice) 
            command = command.lower() 
            if 'vector' in command: 
                command = command.replace('vector','') 
                print(command) 
    except: 
        pass 
    return command 
 
def run_vector(): 
    command = take_command() 
    if 'play' in command: 
        song = command.replace('play','') 
        talk('playing' + song) 
        pywhatkit.playonyt(song) 
    elif 'time' in command: 
        time = datetime.datetime.now().strftime('%I:%M %p') 
        print(time) 
        talk('current time is'+time) 
    elif 'say something about' in command: 
        person = command.replace('say something about','') 
        info = wikipedia.summary(person,2) 
        print(info) 
        talk(info) 
    elif 'founder' in command: 
        talk('akash and there project team created me using python') 
    elif 'open our college website' in command: 
        pywhatkit.search('https://www.vpkbiet.org/') 
    elif 'tell me about vidya pratishthan' in command: 
        talk('vidhya pratishthan is a best college in Baramati') 
        talk('my founders also studying in this college') 
    elif'colour' in command: 
        talk('i love all colours but mostly i like dark black') 
    elif'can you have emotions' in command: 
        talk('i am virtual assistant , i dont have any emotions like human ') 
 
run_vector() 


# In[ ]:




