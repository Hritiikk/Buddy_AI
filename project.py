import speech_recognition as sr
import win32com.client

speaker =win32com.client.Dispatch("zara.Spvoice")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio =r.listen(source)
        query= r.recognize_google(audio, language="en-in" )
        print("your input: {query}")



while 1:
    print("enter the word you want to speak it out by computer")
    s=input()
    speaker.speak(s)
    print("listening...")
    text= takecommand()
    speaker.speak(text)