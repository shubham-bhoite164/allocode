
import pyttsx3
import speech_recognition as sr
import datetime
import random as r

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("My name is Friday. Lets play a game of rock paper and scissor. You first ")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=500
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__=="__main__":
    wishMe()
    
    
    while True:

        query=takeCommand().lower()
        a=["rock","paper","scissor"]
        b=r.randint(0,2)
        answer=a[b]

        if 'rock' in query:
            if b==0:
                print("Computer Move : ",answer)
                print("Its a Tie")
                speak(" Its a Tie")
            elif b==1:
                print("Computer Move : ",answer)
                print("You lost ")
                speak(" You lost ")
                
            elif b==2:
                print("Computer Move : ",answer)
                print("You won ")
                speak(" You won ")

        if 'paper' in query:
            if b==0:
                print("Computer Move : ",answer)
                print("You won ")
                speak(" You won ")
            elif b==1:
                print("Computer Move : ",answer)
                print("Its a Tie")
                speak(" Its a tie ")
            elif b==2:
                print("Computer Move : ",answer)
                print("You lost ")
                speak(" You lost ")

        if 'scissor' in query:
            if b==0:
                print("Computer Move : ",answer)
                print("You lost ")
                speak(" You lost ")
            elif b==1:
                print("Computer Move : ",answer)
                print("You won ")
                speak(" You won ")
            elif b==2:
                print("Computer Move : ",answer)
                print("Its a Tie")
                speak(" Its a tie ")

        