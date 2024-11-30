import pyttsx3 # text to voice
import speech_recognition as sr 
import webbrowser
import datetime
import pyjokes
import pyaudio
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")
# sptext()
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# speechtx("hello komal")
if __name__ == '__main__':

    if "hello komal" in sptext().lower():
        print("test")
    while True:
        data1=sptext().lower()
        if "your name" in data1:
            name = " my name is komal"
            speechtx(name)
        elif "how old are you" in data1:
             age="i m twenty five years old"
             speechtx(age)
        elif 'time' in data1:
             time = datetime.datetime.now().strftime("%I%M%p")
             speechtx(time)
        elif 'youtube' in data1:
             webbrowser.open("https://www.youtube.com/")
        elif 'web' in data1:
             webbrowser.open("https://kiit.ac.in/")
        elif "joke" in data1:
             joke_1 = pyjokes.get_joke(language="en",category="neutral")
             print(joke_1)
             speechtx(joke_1)
        elif 'play song' in  data1:
             add = r"C:\Users\KIIT0001\Music"
             listsong = os.listdir(add)
             print(listsong)
             os.startfile(os.path.join(add,listsong[0]))
        elif "exit" in data1:
            speechtx("Thank you")
            break
        # time.sleep(5)
    else:
       print("thanks")
