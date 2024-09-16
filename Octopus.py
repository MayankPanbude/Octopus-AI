import pyttsx3 
import speech_recognition as sr 
import subprocess as sp
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pywhatkit
import pyjokes
from datetime import date
import sys
from bs4 import BeautifulSoup
import requests
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Octopus. Please tell me how may I help you")       


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
          
        print("Say that again please...")  
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', '')
    server.sendmail('email', to, content)
    server.close()


def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def weather(city):
	city = city.replace(" ", "+")
	res = requests.get(
		f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
	print("Searching...\n")
	soup = BeautifulSoup(res.text, 'html.parser')
	location = soup.select('#wob_loc')[0].getText().strip()
	time = soup.select('#wob_dts')[0].getText().strip()
	info = soup.select('#wob_dc')[0].getText().strip()
	weather = soup.select('#wob_tm')[0].getText().strip()
	print(location)
	print(time) 
	print(info)  
	print(weather+"°C"),speak(location),speak(time),speak(info),speak(weather+"°C")    



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play' in query:
           song = query.replace('play', '')
           print('playing' + song)
           speak('playing ' + song)
           pywhatkit.playonyt(song)
        
        elif 'google ' in query:
            search = query.replace('google', '')
            print('searching' + search)
            speak('searching' + search)
            pywhatkit.search(search)
            
        elif 'open google' in query:
            webbrowser.open("google.com")
   
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)   
            speak(f"Sir, the time is {strTime}")

        elif 'tell me the date' in query:    
            strTime = date.today().strftime("%d/%m/%Y")
            print(strTime)
            speak(f"Today's date: {strTime}" )    
                
       

        elif 'email to vaishnav' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "email"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        
        elif 'open kalinga website' in query:
            webbrowser.open("https://kalingauniversity.ac.in")
        
        elif 'open student login' in query:
            webbrowser.open("https://kusis.kalingauniversity.edu.in")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")  

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com") 

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com") 

        elif 'twitter narendra modi' in query:
            webbrowser.open("https://twitter.com/narendramodi")

        elif "send attendance" in query:
            number = 
            speak("Today's attendence")
            message = takeCommand()
            send_whatsapp_message(number, message)
            speak("I've sent the attendence sir.")    
        
        elif 'tell me joke' in query:
            joke=(pyjokes.get_joke())
            print(joke)
            speak(joke)

        elif 'open camera' in query:
            open_camera()   

        elif 'weather report' in query:
            speak("say the city name")
            city = takeCommand()
            city = city+ 'weather'
            weather(city)
            print("Have a Nice Day:)")
            speak("Have a Nice Day:)")  

        elif 'how are you' in query:
             print("i'm fine. how are you sir?")
             speak("i'm fine. how are you sir?")
        
        elif "i am good" in query:
            print("Okay sir")
            speak("Okay sir") 

        elif 'quit' in query: 
            speak("thanks for using me sir, have a good day.")
            sys.exit()
        
        elif 'exit' in query: 
            speak("thanks for using me sir, have a good day.")
            sys.exit()
            
        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            os.system('shutdown /r /t 1')