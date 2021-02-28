# PROJECT xravis 
#pip install -Iv pyttsx3==2.6 -U
#pip install speechRecognition
#pip install pipwin
#pip3 install pyaudio
#pip install wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #Mircrosoft speeach API to take voice 
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)






def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def wishMe():
  hour=int(datetime.datetime.now().hour)
  if hour>=0 and hour <12:
    speak("Good morning!")
    
    
  elif hour>=12 and hour <18:
    speak("Good Afternoon!")
    
  else:
    speak("Good Evening!")
  speak("I am xarvis Sir. Please tell me Sir how I may help you") 
  
 
def takeCommand():
  # It takes microphone input from the user and return string output
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listening.........")
    r.pause_threshold = 1
    audio = r.listen(source)
    
  try:
    print("Recognising....")
    query= r.recognize_google(audio, language='en-in')
    print(f"User said:{query}\n")
    
    
  except Exception as e:
    print(e)
    
    print("Say that again Please....")
    return "None"
  return query
  
  
  
def sendEmail(to,content):
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login('cahndsekarroy@gmail.com','xxxxxxxxxxx')
  server.sendmail('chandsekarroy@gmail.com',to,content)
  server.close()
  
 
if __name__ == "__main__":
  #speak("Tom is good boy")
  wishMe()
  while True:
  #logic for executing tasks based on query 
    query = takeCommand().lower()
    if 'wikipedia' in query:
      speak('Searching wikipedia')
      query=query.replace('wikipedia',"")
      results= wikipedia.summary(query,sentences=2)
      speak('Arcoding to wikipedia')
      speak(results)
    elif 'open youtube' in query:
      webbrowser.open("youtube.com")
      
    elif 'open google' in query:
      webbrowser.open("google.com")
      
    elif 'open stack overflow' in query:
      webbrowser.open("stackoverflow.com")
      
    # elif 'play music' in query:
      # music_dir = 'D:\\songs'
      # songs = os.listdir(music_dir)
      # print(songs)
      # os.startfile(os.path.join(music_dir,songs[0]))
             
    elif 'the time' in query:
      strTime= datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir, The time is {strTime}")

    elif 'open database' in query:
      print("This is test")
      dbpath = "C:\\Program Files (x86)\\DB Browser for SQLite\\DB Browser for SQLite.exe"
      os.startfile(dbpath)
      
    elif 'open outlook' in query:
      dbpath = "C:\\Program Files (x86)\Microsoft Office\\Office16\\OUTLOOK.EXE"
      os.startfile(dbpath)
      
    elif 'open skype' in query:
      dbpath = "C:\Program Files\WindowsApps\Microsoft.SkypeApp_15.68.96.0_x86__kzf8qxf38zg5c\Skype\Skype.exe"
      os.startfile(dbpath)
    
    
    elif 'bye bye jarvis' in query:
      speak("Bye Bye Chand")
      exit()

    elif 'email to tom' in query:
      try:
        speak("What should I say")
        content=takeCommand()
        to = 'chandsekarroy@gmail.com'
        sendEmail(to,content)
        speak("Email has been sent")      
      except Exception as e:
        print(e)
        speak("Sorry Tom I'm unable to send the email")  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  