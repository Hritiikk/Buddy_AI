import speech_recognition as sr
import webbrowser
import pywhatkit as kit
from win32com.client import Dispatch

Windows_Speak = Dispatch("SAPI.Spvoice")
def speak(word):
    Windows_Speak.Speak(word)

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        speak("Hey there! Buddy here. How can I assist you?")
        print("Listening for a request...")
        try:
            audio = recognizer.listen(source, timeout=5)
            request = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {request}")

            if "open" in request:
                website_name = request.replace("open", "").strip()
                if any(ext in website_name for ext in [".com", ".net", ".org", ".io"]):
                    url = f"https://www.{website_name}"
                else:
                    url = f"https://www.{website_name}.com"
                
                webbrowser.open(url)
                print(f"Opening {website_name}...")
                speak(f"Opening {website_name}...")
                #ye  code use krke yt pr play ho rha , try kiye the baaki site ka hogya har domain ka, song ka add krke dekho ab isme
            # elif "play" in request and "song" in request:
            #     song_name = request.replace("play", "").replace("song", "").strip()
            #     kit.playonyt(song_name)
            #     print(f"Playing {song_name} on YouTube...")
            #     speak(f"Playing {song_name} on YouTube...")
                
            else:
                print("No valid request keyword detected.")
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand audio.")

if __name__ == "__main__":
    main()
