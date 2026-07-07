import matplotlib.pyplot as plt
import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import os
speaker = pyttsx3.init()
mic = sr.Recognizer()   
speaker.say("welcome to Ai world ")
speaker.say("Good morning")
speaker.runAndWait()
with sr.Microphone() as source:
    print("start speaking..")
    voice = mic.listen(source)
    text = mic.recognize_google(voice)
    if "open Notepad" in text:
        print("opening notepad...")
        os.system("notepad")
    elif "send message " in text :
        print("sending message ...")
        #pywhatkit.sendwhatmsg_instantly("+917605060290", " hii karan")

    elif "open YouTube" in text:
        print("opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "open Google" in text:
        print("opening Google...")
        webbrowser.open("https://www.google.com")

    elif "play song" in text:
        print("playing song on YouTube...")
        pywhatkit.playonyt("your song name")
        
     