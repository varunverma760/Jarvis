import pyttsx3
import webbrowser
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
from sqlalchemy import create_engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
                    speak("good morning !")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening!")


    speak(" Hello I am Jarvis Sir how may i help you ")


def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
             print("Listening...")
             r.pause_threshold = 1
             #seconds of non speaking audio phrases is considered to complete
             audio = r.listen(source)


        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said : {query}\n")


        except Exception as e:
            print(e)
            print("Say that again please.....")
            return "None"
        return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('varunverma7.r@gmail.com', 'password')
    server.sendmail('varunverma7.r@gmail.com', to, content)
    server.close()




if __name__ =='__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("seraching wikipedia.....")
            query = query.replace("wikipedia","")
            results =  wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube'in query:
                webbrowser.open("youtube.com")

        elif 'open google' in query:
                webbrowser.open("google.com")


        elif 'open gmail.com'in query:
                webbrowser.open("gmail.com")


        elif 'open amazon'in query:
                webbrowser.open("amazon.in")



        elif "play music" in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))



        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open  MS office" in query:
            MSofficePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(MSofficePath)

        elif 'open code' in query:

         codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe"


         os.startfile(codePath)


        elif 'email to varun' in query :

            try:

                speak("What should I say?")

                content = takeCommand()

                to = "varunverma7.r@gmail.com"

                sendEmail(to, content)

                speak("Email has been sent!")

            except Exception as e:

                print(e)

                speak("Sorry Mr varun . I am not able to send this email at this moment")




