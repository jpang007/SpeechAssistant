import speech_recognition
import speech_recognition as sr
import pyowm
from os import system
import time, requests, json, sys

#implement "What is the weather?"
# Weather first, Music Second
'''
def musicFunction(recognizedText):
    if (recognizedText == "Music"):
        #Work in playing music into program
'''

def getLocation():
    send_url = 'http://freegeoip.net/json'
    r = requests.get(send_url)
    j = json.loads(r.text)
    return {'lat': j['latitude'], 'long': j['longitude']}

def KelvinToFarenheit(temp):
    return (temp*9/5.0) - 459.67


def weatherFunction(recognizedText):
    owm = pyowm.OWM('')  # You MUST provide a valid API key
    location = getLocation()
    print location['lat']
    print location['long']

    obs = owm.weather_at_coords(location['lat'],location['long'])
    weatherObs = obs.get_weather()
    print(weatherObs)
    TempData = weatherObs.get_temperature()
    currentTemp = KelvinToFarenheit(TempData['temp'])
    system('Say The current temperature is {}'.format(int(currentTemp)) + 'degrees, farenheit')


def main():
    r = sr.Recognizer()
    #system('Say Hello, what would you like to check today?')
    while True:
        try:
            with sr.Microphone() as source:
                print ("1")
                audio = r.listen(source)
                print ("2")

            try:
                #Weather command
                StringValue = r.recognize_sphinx(audio)
                print StringValue
                StringValue = "Weather"
                print StringValue
                if (StringValue == "Weather"):
                    #system('Say Okay, let me get that for you')
                    #time.sleep(3)
                    weatherFunction(StringValue)

                #if (recognizedText == "Music"):
                #    musicFunction(StringValue)

                #if (StringValue == "Exit"):
                    #system('Say Okay, goodbye')
                    #sys.exit()

            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))
        except KeyboardInterrupt:
            # Or however you want to exit this loop
            print ('\nBye!')
            sys.exit()
            break
    pass

main()
