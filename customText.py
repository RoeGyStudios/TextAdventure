# -*- coding: cp1252 -*-
def myInput(prompt):
    try:
        temp = raw_input(prompt)
    except NameError:
        temp = input(prompt)
    return(temp)
from langHandler import *
from time import sleep

temp1 = 0

langD = initLang("DE_DE")

def barText(mySelf,player):
    print("Du gehst an den Bartresen, aber man schickt dich weg!")
    return(1)

def text1(mySelf,player):
    global temp1
    #global la
    if temp1 == 0:
        print(langD["text2"])
        temp1 +=1
        return(0)
    if temp1 == 1:
        print(langD["text2_p2"])
        return(1)
        temp1 +=1
def text2(mySelf,player):
    print(langD["T_nachbar_look"])
    print(langD["T_nachbar_1"])
    return(1)
    
def karte(mySelf,player):
    print('''
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ___  ____   | || |      __      | || |  _______     | || |  _________   | || |  _________   | |
| | |_  ||_  _|  | || |     /  \     | || | |_   __ \    | || | |  _   _  |  | || | |_   ___  |  | |
| |   | |_/ /    | || |    / /\ \    | || |   | |__) |   | || | |_/ | | \_|  | || |   | |_  \_|  | |
| |   |  __'.    | || |   / ____ \   | || |   |  __ /    | || |     | |      | || |   |  _|  _   | |
| |  _| |  \ \_  | || | _/ /    \ \_ | || |  _| |  \ \_  | || |    _| |_     | || |  _| |___/ |  | |
| | |____||____| | || ||____|  |____|| || | |____| |___| | || |   |_____|    | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 


    ---------Drinks---------

                               Coke             0,6L 1 Gold 
                                                1L   5 Gold (Ausverkauft)
                               Fanta            0,6L 2 Gold (Ausverkauft)
                                                1L   6 Gold (Ausverkauft)
                               Wasser           1L   1 Gold

    
     -------Gerichte--------


                                Brot            3 Gold
                                Apfel           1 Gold
                                SuperMeal       10 Gold (Ausverkauft)

    (1) Gehen

''')
    run = True
    print(langD["T_bedinung"])
    while run:
        temp = myInput(langD["Q_wasBest"])
        if temp == "Coke":
            if player.gold >= 1:
                print(langD["T_noProb"])
                sleep(5)
                player.gold - 1
                player.addItem("Cola 0,6L")
            else:
                print(langD["E_notEm"])
        elif temp == "Fanta":
                print(langD["I_ausverkauft"])
        elif temp == "Wasser":
            if player.gold >= 1:
                print(langD["T_noProb"])
                sleep(5)
                player.gold - 1
                player.addItem("Wasser 1L")
            else:
                print(langD["E_notEm"])
        elif temp == "Brot":
            if player.gold >= 3:
                print(langD["T_noProb"])
                sleep(5)
                player.gold - 3
                player.addItem("Brot")
            else:
                print(langD["E_notEm"])
        elif temp == "Apfel":
            if player.gold >= 1:
                print(langD["T_noProb"])
                sleep(5)
                player.gold - 2
                player.addItem("Apfel")
            else:
                print(langD["E_notEm"])
        elif temp == "SuperMeal":
            print(langD["I_ausverkauft"])
        elif temp == "1":
            run = False
        else:
            print(langD["I_unav"])
            print("Verfügbar ist: Cola, Fanta, Wasser, Brot, Apfel, SuperMeal")
    
        
def sz6(Mself,player):
    Mself.__

def empty(self,player):
    return(True)
