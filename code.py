import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyautogui
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')   
engine.setProperty('rate', 100)    

# Register Brave as a browser
webbrowser.register('brave' , None, webbrowser.BackgroundBrowser("taget file path with escape sequence \\"))

# Dictionary to map names to email addresses
email_addresses = {
    'name1': 'name1's mail id',
    'name2': 'name2's mail id',
    'nam3e': 'name3's mail id',
    'Naveen' : 'Naveen123@gmail.com',
    # Add more names and email addresses as needed
}

# Web sites 
sites = [
    ['google' , 'https://www.google.com'],
    ['youtube' , 'https://www.youtube.com']
]

# apps / applcations 
apps = [
    ["chrome" , "taget file path with escape sequence \\"],
    ["brave" , "taget file path with escape sequence \\"] ,
    ["whatsapp" ,"taget file path with escape sequence \\"] ,
    ["vscode" , "taget file path with escape sequence \\"]
]

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("What is your good name")
    name = takeCommand()
    time = datetime.datetime.now()
    hour = time.hour
    print(time)
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning! have a nice day {name}")
    elif hour > 12 and hour <= 16:
        speak(f"Good Afternoon! {name}")
    else:
        speak(f"Good Evening! {name}")
    speak("I am Skyshot a Virtual Desktop Assistant. Please tell me how may I help you?")

def takeCommand():
    # It takes microphone input from the user and return string output
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            speak("Listening")
            r.pause_threshold = 0.5
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            # query = r.recognize_google(audio, language='te-IN')

            print(f"User said: {query} \n")
            return query
        except Exception as e:
            print("Say that again please...")
            speak("Say that again please")
            

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    speak("sucesfully cleared")

def stop_assistant():
    speak("Stopping virtual assistant...")
    sys.exit(0)   
    
def shuffle(songs):
    min_value = 0
    max_value = len(songs) - 1
    shuffled_index = random.randint(min_value, max_value)
    return shuffled_index

def play_music(music_dir, song):
    os.startfile(os.path.join(music_dir, song))
    time.sleep(2)  

def pause_music():
    pyautogui.press('space') 

def play_pause_toggle():
    pyautogui.press('space')  

def close():
    pyautogui.hotkey('alt', 'f4') 

def take_screenshot():
    pyautogui.hotkey("prt sc")
    time.sleep(1)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot saved as screenshot.png")

def send_email(to, subject, body, password):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "my-mail@gmail.com"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, to, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def take_name_command():
    speak("Please say the recipient's name.")
    name = takeCommand()
    return name

def take_subject_command():
    speak("Please say the subject of the email.")
    subject = takeCommand()
    return subject

def confirm_send():
    response = input("Do you want to send this email? (yes/no): ").lower()
    return response == 'yes'

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak('searching in wikipedia...')
            query = query.replace("wikipedia" , " ")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        for app in apps:
            if f"open {app[0]}".lower() in query:
                speak(f"Opening {app[0]}")
                os.startfile(app[1])

        # Opening sites 
        for site in sites:
            if f"open {site[0]}".lower() in query:
                speak(f"Opening {site[0]}")
                webbrowser.open(site[1]) 
        
        if 'play music' in query:
            music_dir = "P:\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            shuffled_index = shuffle(songs)
            selected_song = songs[shuffled_index]
            os.startfile(os.path.join(music_dir, selected_song))

        elif 'pause music' in query:
            pause_music()

        elif 'resume music' in query or 'play music' in query:
            play_pause_toggle()

        elif 'close' in query:
            close()
        
        elif 'take screenshot' in query:
            take_screenshot()
        
        elif 'send mail' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to_name = take_name_command()
                to_email = email_addresses.get(to_name.lower(), '')
                if not to_email: # Code to execute when to_email is None or falsy
                    speak(f"No email address found for {to_name}.")
                    continue
                
                speak("What should be the subject of the email?")
                subject = take_subject_command()

                password = getpass("Enter your email password: ")

                speak("Confirm sending the email?")
                if confirm_send():
                    send_email(to_email, subject, content, password)
                    speak('Email has been sent!')
                else:
                    speak("Email not sent. Confirmation denied.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'clean' in query or 'clear' in query:
            clear_terminal()
        
        elif 'stop' in query:
            stop_assistant()
            break

# For details see Info about Virtual Desktop Assistant.md file 
        
        

       
