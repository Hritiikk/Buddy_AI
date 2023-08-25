import speech_recognition as sr
import openai
import os
import webbrowser
from win32com.client import Dispatch

Windows_Speak = Dispatch("SAPI.Spvoice")
def speak(word):
    Windows_Speak.Speak(word)
    
    
def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak(" Hey there! Buddy here. How are you ?")
        print("Listening for a website name...")
        try:
            audio = recognizer.listen(source, timeout=5)
            website_name = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {website_name}")

            if "open" in website_name:
                website_name = website_name.replace("open", "").strip()
                if any(ext in website_name for ext in [".com", ".net", ".org", ".io"]):
                    url = f"https://www.{website_name}"
                else:
                    url = f"https://www.{website_name}.com"
                    
                webbrowser.open(url)
                print(f"Opening {website_name}...")
                speak(f"Opening {website_name}...")
            else:
                print("No 'open' keyword detected.")
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")

if __name__ == "__main__":
    main()




