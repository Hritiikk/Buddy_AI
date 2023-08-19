from win32com.client import Dispatch
import speech_recognition as sr
import webbrowser

Windows_Speak = Dispatch("SAPI.Spvoice")
Windows_Speak.Rate = 1.45

def Speak(word):
    Windows_Speak.Speak(word)

def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = r.listen(source, timeout=2)
            query = r.recognize_google(audio, language="en-IN")
            print("user:")
            print(f"you said: {query}")
            return query.lower()
        except Exception as e:
            return "some error occurred. Try again"

if __name__ == '__main__':
    Speak("Hey there! Buddy here.\n How are you?")
    while True:
        query = Listen()

        sites = [["Google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0].lower()}" in query:
                Speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
