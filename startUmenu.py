# -*- coding: UTF-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import time
import os
import sys
import game
try:
    from logger import *
except:
    print("[ERROR] logger not found")
    exit()

def myInput(prompt):
    try:
        temp = raw_input(prompt)
    except NameError:
        temp = input(prompt)
    return(temp)



run = True
run2 = True
exite = False
exitB = False
error = 0

try:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("")
        print("")
        print("-------------Help-------------")
        print("   --kiosk -k  --> Kioskmode")
        print("   --help -h   --> This help")
        print("   --check -c  --> Libarycheck")
        print("------------------------------")
        print("")
        print("")
        exite = True
    if sys.argv[1] == "--check" or sys.argv[1] == "-c":
        print("")
        print("")
        print("---Running libary check---")
        try:
            from colorama import init, Fore, Back, Style
            print("[OK] Colorama lib found!")
        except:
            error = error + 1
            print("[ERROR] Colorama lib not found!")
        try:
            from langHandler import *
            print("[OK] LangLib found!")
        except:
            error = error + 1
            print("[ERROR] LangLib not found!")
        try:
            from szene import *
            print("[OK] Scene lib found!")
        except:
            error = error + 1
            print("[ERROR] scene lib not found!")
            
        try:
            from playerClass import *
            print("[OK] Player lib found!")
        except:
            error = error + 1
            print("[ERROR] player lib not found!")
        try:
            player1 = Person("TestUSer",100,100,100,[])
            print("[OK] Player test")
        except:
            error = error + 1
            print("[ERROR] player test failed!")
        print("")
        print("-------------------")
        print("ERROR COUNT:" + str(error))
        print("-------------------")
        print("")
        print("")
        exite = True
    if sys.argv[1] == "--kiosk" or sys.argv[1] == "-k":
        try:
            fobj = open("passwd.cfg","r")
        except:
            log("Warn","passwd.cfg not found, creating",True)
            fobj = open("passwd.cfg","w")
            fobj.write("PIN=1234\n")
            fobj.write("user=admin")
            fobj.close()
        else:
            line = fobj.readlines()
            print(line)
            if line[0].startswith("PIN=") == False:
                log("Warn","passwd.cfg format fail, recreating",True)
                fobj.close()
                fobj = open("passwd.cfg","w")
                fobj.write("PIN=1234\n")
                fobj.write("user=admin")
                fobj.close()
            if line[1].startswith("user=") == False:
                #print("[WARN] passwd.cfg fail, recreating..")
                log("Warn","passwd.cfg format fail, recreating",True)
                fobj.close()
                fobj = open("passwd.cfg","w")
                fobj.write("PIN=1234\n")
                fobj.write("user=admin")
                fobj.close()
            fobj = open("passwd.cfg","r")
            line = fobj.readlines()
            pin = line[0][4:len(line[0])-1]
            print(pin)
            user = line[1][5:]
            print(user)
            if pin == "1234" and user == "admin":
                log("Warn","Standart user and PIN settings!",True)
                #print("[WARN] Standart user and PIN settings!")
            
            
                
except:
    print("")
if exite:
    exit()




def showMenu():
    global run
    global run2
    global exite
    global exitB
    global error

    
    


    while run == True:
        print(r"""
     _______        _               _                 _                
    |__   __|      | |     /\      | |               | |               
       | | _____  _| |_   /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
       | |/ _ \ \/ / __| / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \
       | |  __/>  <| |_ / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
       |_|\___/_/\_\\__/_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
         ----------------------------Menu--------------------------
                         1> Spielen
                         2> Einstellungen
                         3> Credits
                         4> Verlassen
        """)
        eingabe = myInput("-> ")
        details = "Niedrig"
        if eingabe == "1":
            game.gamestart()
            run = False
        elif eingabe == "2":
            run2 = True
            while run2 == True:
                print('''
                --------Einstellungen--------

                    **Grafik**
                        1> Details: Wenig
                    2> Verlassen

                ''')
                eingabe2 = myInput("-> ")
                if eingabe2 == "1":
                    print("Zurzeit nicht verfügbar");
                elif eingabe2 == "2":
                    run2 = False
        elif eingabe == "3":
            i = 0
            print('''
               _____ _____  ______ _____ _____ _______ _____ 
              / ____|  __ \|  ____|  __ \_   _|__   __/ ____|
             | |    | |__) | |__  | |  | || |    | | | (___  
             | |    |  _  /|  __| | |  | || |    | |  \___ \ 
             | |____| | \ \| |____| |__| || |_   | |  ____) |
              \_____|_|  \_\______|_____/_____|  |_| |_____/ 
                                                             
                                                             
            ''')
            #creditsT = ['I', 'd', 'e', 'e', ' ', 'f', 'ü', 'r', ' ', 'd', 'a', 's', ' ', 'T', 'e', 'x', 't', 'A', 'd', 'v', 'e', 'n', 't', 'u', 'r', 'e', ':', ' ', 'M', 'a', 't', 't', 'h', 'i', 'a', 's', ' ', 'H', 'e', 'm', 'i', 'n', 'g', '\n', 'F', 'r', 'a', 'm', 'e', 'w', 'o', 'r', 'k', ':', ' ', 'J', 'o', 's', 'h', 'u', 'a', ' ', 'Z', 'o', 'b', 'e', 'l', ' ', 'u', 'n', 'd', ' ', 'S', 'ö', 'r', 'e', 'n', ' ', 'O', 'e', 's', 't', 'e', 'r', 'w', 'i', 'n', 'd', '\n', 'S', 't', 'o', 'r', 'y', ':', ' ', 'J', 'o', 's', 'h', 'u', 'a', ' ', 'Z', 'o', 'b', 'e', 'l', '\n', 'T', 'e', 'x', 't', 'e', ':', ' ', 'S', 'ö', 'r', 'e', 'n', ' ', 'O', 'e', 's', 't', 'e', 'r', 'w', 'i', 'n', 'd', ' ', 'u', 'n', 'd', ' ', 'J', 'o', 's', 'h', 'u', 'a', ' ', 'Z', 'o', 'b', 'e', 'l', '\n']
            creditsT = "Idee für das TextAdventure: Matthias Heming \nFramework: Joshua Zobel und Sören Oesterwind\nStory: Joshua Zobel\nTexte: Sören Oesterwind und Joshua Zobel\n\n"
            for el in creditsT:
                print(el,end='')
                time.sleep(0.2)
            time.sleep(5)
    ##        time.sleep(5)
    ##        print("Idee für ein TextAdventure: Matthias Heming")
    ##        time.sleep(5)
    ##        print("Framework: Joshua Zobel und Sören Oesterwind")
    ##        time.sleep(5)
    ##        print("Story: Joshua Zobel")
    ##        time.sleep(5)
        elif eingabe == "4":
            exitB = True
            run = False

    if exitB == True:
        exit()

if __name__=="__main__":
    showMenu()
