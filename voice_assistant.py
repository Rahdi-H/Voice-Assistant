import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import pyaudio

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print('Recognizing....')
            data = recognizer.recognize_google(audio)
            if data == None:
                data = "xyz"
                return data
            return data
        except sr.UnknownValueError:
            print(" Not Understanding")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

speechtx("Hello Rahdi Sir")

if __name__ == '__main__':
    if sptext().lower() == 'jamal':
        while True:
            data = sptext().lower()
            if 'your name' in data:
                name = 'my name is jamal'
                speechtx(name)
            elif 'old are you' in data:
                age = 'im 1 day old'
                speechtx(age)
            elif 'time now' in data:
                time = datetime.datetime.now().strftime('%I%M%p')
                speechtx(time)
            elif 'youtube' in data:
                webbrowser.open('https://www.youtube.com')
            elif 'joke' in data:
                joke_1 = pyjokes.get_joke(language='en', category='neutral')
                speechtx(joke_1)
            elif 'play song' in data:
                add = '#'
                list_song = os.listdir(add)
                os.startfile(os.path.join(add, list_song[0]))
            elif 'go to sleep' in data:
                speechtx('Im going to sleeping mode rahdi sir')
                break
            elif 'xyz' in data:
                speechtx('tell me what should i do sir')
    else:
        print('thanks')
