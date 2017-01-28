import speech_recognition
import speech_recognition as sr
from os import system
from pprint import pprint
import requests
#implement "What is the weather?"

def main():
    r = sr.Recognizer()
    #system('Say Hello, what would you like to check today?')
    with sr.Microphone() as source:
        print ("1")
        audio = r.listen(source)
        print ("2")

    try:
        #Weather command
        StringValue = r.recognize_sphinx(audio)
        if (StringValue == "Weather"):
            #import weather
            #work in current location as a factor
        print("Sphinx thinks you said " + StringValue)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

main()
