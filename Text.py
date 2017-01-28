import speech_recognition
import speech_recognition as sr
from os import system

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
        print("Sphinx thinks you said " + StringValue)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

main()
