import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import pyautogui 
import requests
import google.generativeai as genai
import os
import smtplib

# def send_email():
#     with sr.Microphone() as source:
#         sender_email = "your_email@gmail.com"  
#         sender_password = "your_password"      

#         speak("To whom should I send the email? Please speak the recipient's email address.")
#         recipient_email = r.listen(source, timeout=5, phrase_time_limit=5)

#         if recipient_email:
#             speak("What should the subject be?")
#             subject = r.listen(source, timeout=5, phrase_time_limit=5)

#             speak("What should I say in the email?")
#             body = r.listen(source, timeout=10, phrase_time_limit=10)

#             email_message = f"Subject: {subject}\n\n{body}"

#             try:
#                 with smtplib.SMTP('smtp.gmail.com', 587) as server:
#                     server.starttls()
#                     server.login(sender_email, sender_password)
#                     server.sendmail(sender_email, recipient_email, email_message)
#                     speak("The email has been sent successfully.")
#             except Exception as e:
#                 speak(f"Failed to send email. Error: {e}")
#         else:
#             speak("I couldn't understand the recipient's email address.")

genai.configure(api_key="AIzaSyCMgiY0TCu7lTtAewGe2SzvhqHqbmpjp0c")
def generate_ai_content(text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    print(response.text)
    speak(response.text)
    

r = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(s):
    engine.say(s)
    engine.runAndWait()

def output(text):
    text = text.lower()
    print(text)
    
    if text=="who are you" or text=="what is your name":
        print("I am ULTRON! How can i help you?")
        speak("I am ULTRON! How can i help you?")
    elif 'what can you do' in text:
        print("I can open various links like google, youtube, linkedin, gmail, github, news etc. I can play song or video of whatever you like. You can ask me what day or date is today. Seperately, open or close applications like chrome, notepad, camera, excel, word & take screenshot for you! or I can tell you a joke to make your day ")
        speak("I can open various links like google, youtube, linkedin, gmail, github, news etc. I can play song or video of whatever you like. You can ask me what day or date is today. Seperataly, open or close applications like chrome, notepad, camera, excel, word & take screenshot for you! or I can tell you a joke to make your day ")
    elif text == "open google":
        webbrowser.open("https://google.com")
        
    elif text in ["open gmail", "open mail","open email"]:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
    elif text == "open youtube":
        webbrowser.open("https://www.youtube.com/")
        
    elif text == "open linkedin":
        webbrowser.open("https://www.linkedin.com/feed/")
        
    elif text == "open github":
        webbrowser.open("https://github.com/")
        
    elif text in ["open leetcode", "open lead code"]:
        webbrowser.open("https://leetcode.com/")
        
    elif "open news" in text:
        webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
        
    elif any(keyword in text for keyword in ['shut down', 'shutdown']):
            speak("Ok , your pc will log off in 10 seconds, make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
    
    elif any(keyword in text for keyword in ["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('screen.png')
        info="screen shot captured!"
        print(info)
        speak(info)
    
    elif 'play'in text:
        song=text.replace('play','')
        speak('playing'+song)
        pywhatkit.playonyt(song)
        
    elif 'time' in text:
        time=datetime.datetime.now().strftime('%I:%M%p')
        print(time)
        speak('Currect timt is'+time)
        
    elif 'date' in text:
        date = datetime.datetime.now().strftime('%A, %d %B %Y')
        print(f"Today's date is: {date}")
        speak(f"Today's date is {date}")
        
    # elif any(keyword in text for keyword in ['find', '?', 'about', 'search','who']):
    #     person = text.replace('find', '').replace('about', '').replace('search', '').replace('who', '').strip()
    #     try:
    #         info = wikipedia.summary(text, sentences=2)
    #         print(info)
    #         speak(info)
    #     except :
    #         text = text.replace("search", "")
    #         text = text.replace(" for ", "")
    #         text = text.replace(' google', '')
    #         text = text.replace('google ', '')
    #         webbrowser.open(f'https://www.google.com/search?q={text}')
    #         print(f'\n\tSearching For "{text.title()}"')
    #         speak(f"Searching for {text}")
            
    elif 'joke' in text:
        a=pyjokes.get_joke()
        print(a)
        speak(a)
    
    elif 'date' in text:
        date = datetime.datetime.now().strftime('%A, %d %B %Y')
        print(f"Today's date is: {date}")
        speak(f"Today's date is {date}")
##################################################### 

    elif "open chrome" in text:
        speak("Opening Google Chrome")
        os.system("start chrome")
    elif "open calculator" in  text:
        speak("Opening Calculator")
        os.system("start calc")
    elif "open notepad" in  text:
        speak("Opening Notepad")
        os.system("start notepad")
    elif "open camera" in  text:
        speak("Opening Camera")
        os.system("start microsoft.windows.camera:")
    elif "open excel" in  text:
        speak("Opening Microsoft Excel")
        os.system("start excel")
    elif "open word" in  text:
        speak("Opening Microsoft Word")
        os.system("start winword")
    elif "open powerpoint" in  text:
        speak("Opening Microsoft PowerPoint")
        os.system("start powerpnt")
    elif "open calender" in  text:
        speak("Opening Calender")
        os.system("start outlookcal:")
    elif any(keyword in text for keyword in ["watch","clock"]):
        speak("Opening Alarms & Clock")
        os.system("start ms-clock:")
    elif "open store" in  text:
        speak("Opening Microsoft Store")
        os.system("start ms-windows-store:")
    elif "open photos" in  text:
        speak("Opening Photos")
        os.system("start ms-photos:")
    elif "open settings" in  text:
        speak("Opening Settings")
        os.system("start ms-settings:")
    elif "open security" in  text:
        speak("Opening Security Service")
        os.system("start windowsdefender:")
###############################################################
    elif 'close' in text:
        pyautogui.hotkey('alt','f4')
        speak("Window closed")
    else:
        generate_ai_content(f"Generate a helpful response in maximum 50-100 words: {text}")
        


def main():
    speak("Welcome back sir! How can i help you? ")
    print("Welcome back sir! How can i help you? ")
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                print("Processing...")
                text = r.recognize_google(audio)
                text=text.lower()
                
                if "stop listening" in text:
                    speak("Voice Assistant is stopping. Bye, Have a good day sir!")
                    print("Voice Assistant is stopping.")
                    break
                
                output(text)
                # print(f"Recognized: '{text}'")


            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak("Sorry, I'm having trouble connecting to the speech recognition service.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                speak("An unexpected error occurred.")

if __name__ == "__main__":
    main()
