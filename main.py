import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from ai import ask_ai
import pywhatkit
from datetime import datetime
from weather import get_weather
import subprocess
from config import newsapi


def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processcommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://Google.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://Facebook.com")
    elif "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://Youtube.com")
    elif "open instagram" in c.lower():
        speak("opening instagram")
        webbrowser.open("https://Instagram.com")
    elif "open linkedin" in c.lower():
        speak("opening linkedin")
        webbrowser.open("https://LinkedIn.com")
    elif "play" in command:
        song = command.replace("play", "").strip()

        speak(f"Playing {song}")

        pywhatkit.playonyt(song)

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")
    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
    elif "open paint" in command:
        speak("Opening Paint")
        subprocess.Popen("mspaint.exe")
    elif "open command prompt" in command:
        speak("Opening Command Prompt")
        subprocess.Popen("cmd.exe")
    elif "open file explorer" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer.exe")
    elif "open visual studio code" in command or "open vs code" in command:
        speak("Opening Visual Studio Code")
        subprocess.Popen("code")

    elif "news" in c.lower():
        speak("Here are today's top headlines")

        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"

        response = requests.get(url)
        data = response.json()

        articles = data["articles"]

        for article in articles[:5]:
            speak(article["title"])

    elif "weather" in command:

        city = command.lower()

        city = city.replace("what is the", "")
        city = city.replace("tell me", "")
        city = city.replace("weather", "")
        city = city.replace("in", "")
        city = city.strip()

        if city == "":
            city = "Lucknow"

        report = get_weather(city)

        print(report)
        speak(report)

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        print(current_time)
        speak(f"The current time is {current_time}")

    elif "exit" in command or "stop jarvis" in command or "close jarvis" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        exit()

    else:
        speak("Thinking...")

        answer = ask_ai(command)

        print(answer)
        speak(answer)

if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        # Initialize recognizer class (for recognizing the speech)
        r=sr.Recognizer()
        # Reading Microphone as source
        # listening the speech and store in audio_text variable

    # Recognize speech using Google Web Speech API
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio= r.listen(source,timeout=5,phrase_time_limit=5)
                
            word = r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                
                speak("Ya! how can i help you")
                
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio= r.listen(source)
                    command=r.recognize_google(audio)
                    print(command)

                    processcommand(command)

        except Exception as e:
            print("Error {0}".format(e))