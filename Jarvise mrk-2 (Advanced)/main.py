import os
import random
import time
import webbrowser
from datetime import datetime
import pyautogui
import pyttsx3
import pywhatkit
import wikipedia
from pygame import mixer
from pywhatkit import playonyt
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour1 = int(datetime.now().hour)
    if hour1>=0 and hour1<12:
        speak("Good Morning Sir!")

    elif hour1>=12 and hour1<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening Sir!")  

print(wishme())

def sending():
    speak('for whom sir')
    a = input('for whom sir\n')
    speak('what message sir')
    b = input("what message sir\n")
    webbrowser.open('https://web.whatsapp.com/')
    time.sleep(40)
    pyautogui.click(211, 187)
    pyautogui.typewrite(a)
    time.sleep(3)
    pyautogui.click(168, 322)
    time.sleep(2)
    pyautogui.click(824, 662)
    pyautogui.typewrite(b)
    time.sleep(1)
    pyautogui.click(1242, 659)

def gameStone():
    while True:
        print("Press 's' for Stone\n")
        print("Press 'p' for Paper\n")
        print("Press 'sc' for Scissors\n")
        userChoice = input("Chose any above Options\n").lower()
        game = ["Stone", "Paper", "Scissors"]
        AI = random.choice(game)

        # Paper
        if AI == "Paper" and userChoice == "sc":
            speak("Congrats you won sir")
            print("Aakash has won")
            print(f"Jarvis chose {AI}")
        elif AI == "Paper" and userChoice == "s":
            speak("Huray, i won")
            print("Jarvis has won")
            print(f"Jarvis chose {AI}")
        elif AI == "Paper" and userChoice == "p":
            speak("Tie")
            print("Tie")
            print(f"Jarvis chose {AI}")

        # Stone
        elif AI == "Stone" and userChoice == "sc":
            speak("Huray, i won")
            print("Jarvis has won")
            print(f"Jarvis chose {AI}")
        elif AI == "Stone" and userChoice == "s":
            speak("Tie")
            print("Tie")
            print(f"Jarvis chose {AI}")
        elif AI == "Stone" and userChoice == "p":
            speak("Congrats you won sir")
            print("Aakash has won")
            print(f"Jarvis chose {AI}")
        # Scissors

        elif AI == "Scissors" and userChoice == "p":
            speak("Huray, i won")
            print("Jarvis has won")
            print(f"Jarvis chose {AI}")
        elif AI == "Scissors" and userChoice == "s":
            speak("Congrats you won sir")
            print(f"Jarvis chose {AI}")
            print("Aakash has won")
        elif AI == "Scissors" and userChoice == "sc":
            speak("Tie")
            print("Tie")
            print(f"Jarvis chose {AI}")
        else:
            print("Please input a valid input")
            gameStone()
        print("Do you want to play (y/n)")
        userIn = input().lower()
        if userIn == "y":
            gameStone()
        elif userIn == "n":
            break

def pause():
    pyautogui.click(418, 705)
    pyautogui.click(314, 401)

def reminder():
    speak("What hour do you want to set a reminder")
    userH = int(input("What hour do you want to set a reminder\n"))
    speak("What minute do you want to sea a reminder")
    userM = int(input("What minute do you want to sea a reminder\n"))
    speak("AM ,or PM sir")
    userAP = str(input("AM or PM\n"))
    print("Waiting...")
    speak("waiting...")
    if userAP == "PM":
        userH+=12
    else:
        print(userH)
    while True:
        if userH == datetime.now().hour and userM == datetime.now().minute and userAP == datetime.now().strftime("%p"):
            mixer.init()
            mixer.music.load('Alarm.mp3')
            mixer.music.play()
            final = input("Please press s to stop the alarm\n")
            if "s" in final:
                mixer.music.stop()
                break


def play():
    speak('what song you want to play sir')
    song = input("What song do you want to play sir\n")
    speak("ok sir")
    if "nothing" in song:
        "ok sir"
    else:
        pywhatkit.playonyt(song)
def favorite():
    while True:
        mixer.init()
        mixer.music.load('Best of kk.mp3')
        mixer.music.play()
        final = input("press s to stop")
        if final == 's':
            mixer.music.stop()
            break



def query():
    print('Please input a command ')
    command = input().lower()
        
    if 'time' in command:
        time = datetime.now().strftime("%I:%M %p")
        speak(time)

    elif 'who is' in command:
        speak('Searching Wikipedia sir...')
        query = command.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=20)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in command:
        speak("ok sir")
        pywhatkit.search("www.youtube.com")

    elif 'open google' in command:
        speak("ok sir")
        pywhatkit.search("www.google.com")

    elif 'open stackoverflow' in command:
        speak("ok sir")
        pywhatkit.search("www.stackoverflow.com") 

    elif 'thank' in command:
        speak('Your Welcome Sir')

    elif 'water formula' in command:
        speak('Sir the Formula of water is H2O')
        print('Sir the Formula of water is H2O')
    elif 'water' in command:
        speak('Sir the Formula of water is H2O')
        print('Sir the Formula of water is H2O')

    elif 'copper sulphate formula' in command:
        speak('Sir the Formula of copper sulphate is CuSO4')
        print('Sir the Formula of copper sulphate is CuSO4')
    elif 'copper sulphate' in command:
        speak('Sir the Formula of copper sulphate is CuSO4')
        print('Sir the Formula of copper sulphate is CuSO4')

    elif 'calcium oxycloride formula' in command:
        speak('Sir the Formula of Calcium oxycloride is CaOCl2')
        print('Sir the Formula of Calcium oxycloride is CaOCl2')
    elif 'calcium oxycloride' in command:
        speak('Sir the Formula of Calcium oxycloride is CaOCl2')
        print('Sir the Formula of Calcium oxycloride is CaOCl2')

    elif 'chloroform formula' in command:
        speak('Sir the Formula of chloroform is CHCl3')
        print('Sir the Formula of chloroform is CHCl3')
    elif 'trichoro methane formula' in command:
        speak('Sir the Formula of trichoro methane is CHCl3')
        print('Sir the Formula of trichoro methane is CHCl3')
    
    elif 'marble formula' in command:
        speak('Sir the Formula of marble is CaCO3')
        print('Sir the Formula of marble is CaCO3')
    elif 'calcium carbonate formula' in command:
        speak('Sir the Formula of Calcium Carbonate is CaCO3')
        print('Sir the Formula of Calcium Carbonate is CaCO3')
    
    elif 'caustic potash formula' in command:
        speak('Sir the Formula of caustic potash is KOH')
        print('Sir the Formula of caustic potash is KOH')
    elif 'potassium hydroxide formula' in command:
        speak('Sir the Formula of potassium hydroxide is KOH')
        print('Sir the Formula of potassium hydroxide is KOH')
    
    elif 'caustic soda formula' in command:
        speak('Sir the Formula of Sodium Hydroxide is NaOH')
        print('Sir the Formula of Sodium Hydroxide is NaOH')

    elif 'epsom formula' in command:
        speak('Sir the Formula of Magnesium sulphate is MgSO4')
        print('Sir the Formula of Magnesium sulphate is MgSO4')
    
    elif 'magenesium sulphate formula' in command:
        speak('Sir the Formula of Magnesium sulphate is MgSO4')
        print('Sir the Formula of Magnesium sulphate is MgSO4')

    elif 'calcium sulphate formula' in command:
        speak('Sir the Formula of calcium sulphate is CaSO4')
        print('Sir the Formula of calcium sulphate is CaSO4')

    elif 'ferroas sulphate formula' in command:
        speak('Sir the Formula of ferroas sulphate is FeSO4')
        print('Sir the Formula of ferroas sulphate is FeSO4')

    elif 'heavy formula' in command:
        speak('Sir the Formula of Heavy Water is D2O')
        print('Sir the Formula of Heavy Water is D2O')
    elif 'Full form of D' in command:
        speak('Sir the full form of D is Deuterium oxide')
        print('Sir the full form of D is Deuterium oxide')
    elif 'acetic acid formula' in command:
        speak('Sir the Formula of acetic acid is CH3COOH')
        print('Sir the Formula of acetic acid is CH3COOH')
    elif 'sodium carbonate formula' in command:
        speak('Sir the Formula of sodium carbonate is Na2CO3')
        print('Sir the Formula of sodium carbonate is Na2CO3')
    elif 'calcium hydroxide formula' in command:
        speak('Sir the Formula of calcium hydroxide is CaOH2')
        print('Sir the Formula of calcium hydroxide is CaOH2')
    elif 'calcium oxide formula' in command:
        speak('Sir the Formula of calcium oxide is CaO')
        print('Sir the Formula of calcium oxide is CaO')
    elif 'zinc sulphate formula' in command:
        speak('Sir the Formula of zinc sulphate is ZnSO4')
        print('Sir the Formula of zinc sulphate is ZnSO4')
    elif 'methane formula' in command:
        speak('Sir the Formula of methane is CH4')
        print('Sir the Formula of methane is CH4')
    elif 'magnesium oxide formula' in command:
        speak('Sir the Formula of magnesium oxide is MgO')
        print('Sir the Formula of magnesium oxide is MgO')
    elif 'nitrous oxide formula' in command:
        speak('Sir the Formula of nitrous oxide is N2O')
        print('Sir the Formula of nitrous oxide is N2O')
    elif 'laughing gas formula' in command:
        speak('Sir the Formula of laughing gas is N2O')
        print('Sir the Formula of laughing gas is N2O')
    elif 'sugar formula' in command:
        speak('Sir the Formula of sugar is C12H22O11')
        print('Sir the Formula of sugar is C12H22O11')
    elif 'tnt formula' in command:
        speak('Sir the Formula of TNT is C7H5N3O6')
        print('Sir the Formula of TNT is C7H5N3O6')
    elif 'trinitro toluen formula' in command:
        speak('Sir the Formula of trinitro toluen is C7H5N3O6')
        print('Sir the Formula of trinitro toluen is C7H5N3O6')
    elif 'sand formula' in command:
        speak('Sir the Formula of sand is SiO2')
        print('Sir the Formula of sand is SiO2')
    elif 'silicon oxide formula' in command:
        speak('Sir the Formula of silicon oxide is SiO2')
        print('Sir the Formula of silicon oxide is SiO2')
    elif 'common salt formula' in command:
        speak('Sir the Formula of common salt is NaCl')
        print('Sir the Formula of common salt is NaCl')
    elif 'king of chemical formula' in command:
        speak('Sir the Formula of king of chemical is H2SO4')
        print('Sir the Formula of king of chemical is H2SO4')
    elif 'sulphuric acid formula' in command:
        speak('Sir the Formula of sulphuric acid is H2SO4')
        print('Sir the Formula of sulphuric acid is H2SO4')
    elif 'ozone formula' in command:
        speak('Sir the Formula of ozone is O3')
        print('Sir the Formula of ozone is O3')
    elif 'caustic soda formula' in command:
        speak('Sir the Formula of caustic soda is NaOH')
        print('Sir the Formula of caustic soda is NaOH')
    elif 'sodium hydroxide formula' in command:
        speak('Sir the Formula of sodium hydroxide is NaOH')
        print('Sir the Formula of sodium hydroxide is NaOH')
    elif 'acid rain formula' in command:
        speak('Sir the Formula of acid rain is SO4 + NO2')
        print('Sir the Formula of acid rain is SO4 + NO2')
    elif 'starch formula' in command:
        speak('Sir the Formula of starch is C6H10O5')
        print('Sir the Formula of starch is C6H10O5')
    elif 'hydrochloric acid formula' in command:
        speak('Sir the Formula of hydrochloric acid is HCL')
        print('Sir the Formula of hydrochloric acid is HCL')
    elif 'phosphoric acid formula' in command:
        speak('Sir the Formula of phosphoric acid is H3PO4')
        print('Sir the Formula of phosphoric acid is H3PO4')
    elif 'ascorbic acid formula' in command:
        speak('Sir the Formula of ascorbic acid is C6H8O6')
        print('Sir the Formula of ascorbic acid is C6H8O6')
    elif 'carbonic acid formula' in command:
        speak('Sir the Formula of carbonic acid is H2CO3')
        print('Sir the Formula of carbonic acid is H2CO3')
    elif 'hydrogen sulphide formula' in command:
        speak('Sir the Formula of hydrogen sulphide is H2S and ,this also smell like ,rotten eggs sir')
        print('Sir the Formula of hydrogen sulphide is H2S and ,this also smell like ,rotten eggs sir')
    elif 'who are you' in command:
        speak('I am jarvis sir ,your personal assistants')
    elif 'change to friday' in command:
        speak('ok sir, calling friday')
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices[1].id)
        speak("What help do you want from me sir")
    elif 'change to jarvis' in command:
        speak('ok sir, calling jarvis')
        voices = engine.getProperty('voices') 
        engine.setProperty('voice', voices[1].id)
        speak("What help do you want from me sir")
    elif 'reminder' in command:
        speak("ok sir")
        print(reminder())
    elif 'send' in command:
        speak("Ok sir")
        print(sending())
    elif 'play on yt' in command:
        speak('ok sir')
        print(play())
    elif 'play me a jukebox' in command:
        speak('ok sir, playing your favorite juke box')
        print(favorite())

    elif 'pause yt' in command:
        speak('ok sir')
        print(pause())
    elif 'resume yt' in command:
        speak('ok sir')
        print(pause())
    elif 'add' in command:
        speak("Please enter the first number sir, you want to add")
        userF = int(input("Please enter the first number sir, you want to add\n"))
        speak("Please enter the Second number sir, you want to add")
        userS = int(input("Please enter the Second number sir, you want to add\n"))
        final = ("The sum of",userF,", and",userS,"is", userF + userS)
        print(final)
        speak(final)
    elif 'substract' in command:
        userF = int(input("Please enter the first number sir, you want to Substract\n"))
        speak("Please enter the first number sir, you want to Substract")
        userS = int(input("Please enter the Second number sir\n"))
        speak("Please enter the Second number sir")
        final = ("The Substracted form of",userF,", and",userS,"is", userF - userS)
        print(final)
        speak(final)
    elif "search" in command:
        final = input('')
        speak("ok sir")
        pywhatkit.search(final)
        print("Searching...")
    elif "current working dir" in command:
        print(os.getcwd())
        speak(f"Our Current working directory is {os.getcwd()}")
    elif 'ok' in command:
        pass
    elif 'what is your name' in command:
        speak('My name is Jarvis')
    elif 'what is your favorite color' in command:
        speak("My favorite color is Red sir")
    elif 'do you have any girlfriend' in command:
        speak("No sir i don't have any girlfriend yet")
    elif 'open c' == command:
        speak('ok sir')
        print(os.startfile("C:"))

    elif 'open e' in command:
        speak('ok sir')
        print(os.startfile("E:"))

    elif 'open f' in command:
        speak('ok sir')
        print(os.startfile("F:"))
    elif 'open our current working dir' in command:
        speak('ok sir')
        print(os.startfile("E:\\Python Projects\\Jarvise mrk-2"))
    elif 'open code' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"))
    elif 'open chrome' in command:
        speak("ok sir")
        print(os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))

    elif 'open games' in command:
        speak("ok sir")
        print(os.startfile("F:\\Games"))
    elif 'open python projects' in command:
        speak("ok sir")
        print(os.startfile("E:\\Python Projects"))
    elif 'open websites folder' in command:
        speak("ok sir")
        print(os.startfile("E:\\Web Development\\Websites\\Websites"))
    elif 'open downloads' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Downloads"))
    elif 'open documents' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Documents"))
    elif 'open music' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Music"))
    elif 'open picture' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Pictures"))
    elif 'open videos' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Videos"))
    elif 'open desktop' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Desktop"))
    elif 'open desktop' in command:
        speak("ok sir")
        print(os.startfile("C:\\Users\\Aakash\\Desktop"))
    elif 'open songs' in command:
        speak("ok sir")
        print(os.startfile("F:\\Songs"))
    elif 'close code' in command:
        speak("ok sir")
        os.system('taskkill /f /im Code.exe')
    elif 'close chrome' in command:
        speak("ok sir")
        os.system('taskkill /f /im chrome.exe')
    elif 'good afternoon' in command:
        pass
    elif 'good morning' in command:
        pass
    elif 'good evening' in command:
        pass
    elif 'hi' in command:
        speak('Hello sir')
    elif 'aakash' in command:
        speak('Akash is a Intelligein, Smart, and he is also ,my god who maked me')
    elif 'aryan' in command:
        speak('Aryan is also a Smart boy')
    elif 'jarvis are you a padwa' in command:
        speak('Yes sir i am')
        speak('and you are also a padwa')
    elif 'stone paper' in command:
        speak("ok sir lets play")
        gameStone()
    elif 'wake up jarvis' in command:
        speak("as you wish sir.")
        speak("So what to do next sir")
    elif "wait" in command:
        speak("ok sir")
    elif "quite" in command:
        speak("ok sir, thank you for using me")
    else:
        speak("Sorry sir!, this command is not available in my Program")
        print("Sorry sir!, this command is not available in my Program")

while True:
    print(query())
        