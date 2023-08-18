import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("sapi.Spvoice")


def takecommand():  # for english
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="en-in")
        print("your input:", query)
        return query


def takecommand_hindi():  # for hindi part
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio, language="hi-IN")
        print("your input: ", query)
        return query


while True:
    print("enter the word you want to speak it out by computer")
    s = input()
    speaker.speak(s)
    print("listening...")
    text = takecommand_hindi()
    text = takecommand()
    speaker.speak(text)
    # try krke dekh kaam kr rha tere me ? mere me ek baar kra phir bnd hogya
    '''
    -> listening tak ja raha but input nahi le raha 
    Follow Up -> question ? -_- dono mei hi i.e takecommand_hindi() and takecommand() query wala part nhi le raha 
    and male voice aa rahi hai 
    ''' 
