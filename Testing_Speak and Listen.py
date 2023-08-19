from win32com.client import Dispatch
import speech_recognition as sr

Windows_Speak = Dispatch("SAPI.Spvoice")
Windows_Speak.Rate = 1.45


def Speak_AI(word):
    Windows_Speak.Speak(word)


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("listening ... .. .. ")
        audio = r.listen(source, timeout=2)
        query = r.recognize_google(audio, language="en-IN")
        print("Printing Whatver User said \n")
        print(f"Did you said : {query}")
        return query


Listened_string = Listen()
Speak_AI(Listened_string)
