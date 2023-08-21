import speech_recognition as sr
import webbrowser

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a website name...")
        try:
            audio = recognizer.listen(source, timeout=5)
            website_name = recognizer.recognize_google(audio).lower()
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
