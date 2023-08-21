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
        # r.pause_threshold = 1
        audio = r.listen(source, timeout=2)
        try:
            print("Listening...")
            query = r.recognize_google(audio, language="en-IN")
            print("user: \n")
            print(f"you said : {query}")
            return query
        except Exception as e:
            return "some error occurred. Try again "

if __name__== ' main ':
    Speak(" Hey there! Buddy here /n How are you ?")
    while True:
        print("listening...")
        query=Listen()
        #sites that can be opened with this ai
        sites= [["Google","https://www.Google.com"]]
        for site in sites:
            if f"open{site[0]}".lower() in query.lower():
                Speak(f"opening {site[0]} sir..")
                webbrowser.open(site[1])


