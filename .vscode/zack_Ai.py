from urllib.parse import non_hierarchical
import PersonalQ as pq
import random
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
from wikipedia.wikipedia import search
from os import path
import os
import rock_paper_sci
from speachrec import Take
from speachrec import speak

x = True
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening")
        print("Good Evening")
    speak("I am zack! how may i help you")


def opensoft(query):
    if 'open code in computer' in query:
        codepath = "C:\\Users\\dumre\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    elif 'open spotify in computer' in query:
        codepath = "C:\\Users\\dumre\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(codepath)

def webSea(query):
    if 'in wikipedia' in query or 'on wikipedia' in query:
        speak('Searching...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif "open portal" in query:
        speak("opening your N M I M S student portal ")
        webbrowser.open_new_tab(f"https://portal.svkm.ac.in/MPSTME-NM-M/homepage")

    elif 'open' in query:
        query = query.replace("open ", "")
        webbrowser.open_new_tab(f"https://{query}.com")


def envi(query):
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")
    if 'day' in query:
        day = (datetime.datetime.today().weekday() + 1)
        if day in Day_dict:
            theday = Day_dict[day]
        speak(f"today is {theday}")


def NewsWeb(query):
    webbrowser.open_new_tab(
        "https://timesofindia.indiatimes.com//home//headlines")
    speak("Here are some headlines from the Times of India, Happy reading!!")


def seaGoog(query):
    query = query.replace("search", "")
    speak("I found this on google")
    webbrowser.open_new_tab("https://www.google.com/search?q="+query)



def idk(query):
    speak(f"I dont know what you mean by {query}, would you like me to do a google search?")
    a = Take().lower()
    ans=yn(a)
    if ans ==True:
        seaGoog(query)
    else:
        speak("Ok!, as you wish")
        return None


def yn(ans):

    if 'yes' in ans:
        return True
    elif "no" in ans:
        return False
    else:
        speak("please say a valid option")
        ans = Take().lower()
        return yn(ans)


def wher(query):

    query = query.replace("where is", "")
    loc = query
    speak(f"Locating {loc}")
    webbrowser.open(f"https://www.google.co.in/maps/place/{loc}")

def rock():

    rock_paper_sci.play()
    speak("play again?")
    print("play again?")
    while True:
        a=Take().lower()
        if a=='yes':
            speak("great!!, get ready to loose")
            rock()
        elif a=="no":
            speak("I think you got scared , hahaha, it's understandable")
            break
        else:
            speak("say that again dummy")
            continue

def pers(query):

        for i in pq.mylist:
            if i in query:
                speak(random.choice(pq.mylist[i]))
                return False
        else:
            return True

def jk():
    while True:
        speak(pyjokes.get_joke())
        speak(", hehee")
        print("want another one?")
        speak("want another one?,")
        a=Take().lower()
        ans=yn(a)
        if ans ==True:
            speak(",okay here you go,")
            True
        else:
            speak("Okay i'll keep all the jokes to myself then")
            break
def kkjoke(query):
    while True:
        intt=random.randint(0,20)
        speak("knock knock")
        a=Take().lower()
        if a == "who's there" or a== "who is there":
            x=list(pq.Kjokes.keys())[intt]
            print(x)
            speak(x)
            ans=Take().lower()
            # if ans == (x+" who"):
            v=list(pq.Kjokes.values())[intt]
            speak(v+"hehe, ")
            
        else:
            speak("just say 'who's there'")
            continue
        print("want another one?")
        speak("want another one?,")
        a=Take().lower()
        ans=yn(a)
        if ans ==True:
            speak(",okay here you go,")
            True
        else:
            speak("Okay i'll keep all the jokes to myself then")
            break
    



if __name__ == '__main__':
    greet()
    while True:
        x=True
        query = Take().lower()
        
        if query:
            x=pers(query)
            if x==True:
                if 'what time' in query or 'what day' in query:
                    envi(query)
                    x=False
                elif"what is" in query or "search" in query or "who is" in query or 'how to' in query or 'how is' in query or 'how are' in query:
                    seaGoog(query)
                    x = False
                elif "where is" in query:
                    wher(query)
                    x = False

        if "play a game" in query:
            rock()
            x = False

        if 'in computer' in query:
            opensoft(query)
            x = False
        elif 'open' in query or 'tell me' in query:
            webSea(query)
            x = False


        if "sleep" in query or"don't listen" in query or "stop listening" in query:
            speak(f"deafning myself for 20 seconds")
            time.sleep(20)
            x= False
        elif 'news' in query:
            NewsWeb(query)
            x = False

        if "what can you do" in query :
            speak("I can do all the stuff written bellow")
            f = open("D:\\riddhi\\Python learning\\.vscode\\todo.txt", "r")
            print(f.read())
            speak("I will be  sleeping for 30 seconds so that you can read")
            time.sleep(30)
            x=False

        if 'knock knock' in query:
            kkjoke(query)
            x=False

        elif 'joke' in query:
            jk()
            x = False

        if "-" == query:
            x = False

        if 'bye' == query or 'stop'== query or 'shut up' in query or 'off' in query :
            speak('okay, I hope I never see you again, goodbye!')
            exit(0)

        if x == True:
            idk(query)
