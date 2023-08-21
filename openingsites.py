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
        # try:
        #     print("Listening...")
            audio = r.listen(source, timeout=2)
            query = r.recognize_google(audio, language="en-IN")
        #     print("user:")
        #     print(f"you said: {query}")
        #     return query.lower()
        # except Exception as e:
        #     return "some error occurred. Try again"

def main():
    r=sr.Recognizer()
    Speak("Hey there! Buddy here.\n How are you?")
    while True:
        query = Listen()

        with sr.Microphone() as source:
         print("Listening for a website name...")
        try:
            audio = r.listen(source, timeout=5)
            website_name = r.recognize_google(audio).lower()
            print(f"Recognized: {website_name}")

            # Modify the URL generation to retain the listen part's flexibility
            if "open" in website_name:
                website_name = website_name.replace("open", "").strip()
                url = f"https://www.{website_name}.com"
                webbrowser.open(url)
                print(f"Opening {website_name}...")
            else:
                print("No 'open' keyword detected.")
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")

if __name__ == "__main__":
    main()