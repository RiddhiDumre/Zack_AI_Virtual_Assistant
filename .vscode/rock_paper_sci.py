import random
from speachrec import Take
from speachrec import speak

gamelist = ['rock', 'paper', 'scissors']


def game(comp, player):

    if player not in gamelist:
        while True:
            speak("say a valid option")
            play=Take().lower()
            return game(comp,play)
                

    if(comp == player):
        return None
    if(comp == 'rock'):
        if(player == 'scissors'):
            return True
        else:
            return False
    if(comp == 'paper'):
        if(player == 'scissors'):
            return False
        else:
            return True
    if(comp == 'scissors'):
        if(player == 'paper'):
            return True
        else:
            return False

def play():
    print('''
    \t\t Game
    choose any one of the following:-
    - rock
    - paper 
    - scissors
    ''')
    speak('''
    \t
    choose any one of the following:-
    - rock
    - paper, or
    - scissors
    ''')

    comp = print("zack's Turn")
    speak("I am choosing now,")
    comp = random.choice(gamelist)
    print("Your Turn: ")
    speak("          Your Turn: ")
    player=Take().lower()

    a = game(comp, player)
    print(f"zack's choice: {comp}")
    speak(f"My choice: {comp}")


    if(a == None):

        print("\nIT'S A TIE!!")
        speak("\nIT'S A TIE!! dammm!")
    elif(a):

        print("\nI WON!!")
        speak("HAHAHA I Won!! [better luck next time]")
    else:

        print("\nYOU WON!!")
        speak("\nCongrats!! at least you won for once in your life!!")
