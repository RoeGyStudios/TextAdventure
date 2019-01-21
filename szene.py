# -*- coding: cp1252 -*-

def myInput(prompt):
    try:
        temp = raw_input(prompt)
    except NameError:
        temp = input(prompt)
    return(temp)


try:
    import customText as cT
except ImportError:
    raise ImportError("[ERROR] custom Text not found")

try:
    import time as ti
except ImportError:
    raise ImportError("[ERROR] time Lib not found")
    


class demoEnd():
    def __init__(self,name,szenenid):
        self.__name = name
        self.__szenenid = szenenid
    def play(self,player):
        print(u'''
*****Das Ende*****

Vielen Dank das Sie das TextAdventure von RöGy Studio durchgespielt haben! Leider ist das Spiel noch nicht fertig. Besuchen sie uns auf {webadresse}.
Es wird sich noch viel verändern. Also lohnt es sich, immer mal wieder vorbei zugucken! Wir wünschen ihnen noch einen schönen Tag. Sprechen sie uns doch
einfach mal an!
******************
Außerdem währe es nett, jetzt uns anzusprechen damit wir das Spiel neustarten.
''')
        ti.sleep(10)
        return(-1)
    


class szeneStandart():
    def __init__(self,name,szenenid,oben,unten,links,rechts,text,items,aufwand,Szname,customText={},runFunc=cT.empty,debug=False):
        self.__runFunc = runFunc
        self.__oben = oben
        self.__unten = unten
        self.__links = links
        self.__rechts = rechts
        self.__SZname = Szname
        self.__customText = customText
        self.__pause=False
        #self.__wege = {"oben" : self.__oben,"unten" : self.__unten,"links" : self.__links,"rechts" : self.__rechts}
        self.__aktiveWege = []
        self.__wege = {}
        i=0
        self.__commands = {}
        #print(" -- ")
        #print(Szname)
        while i <= 3:
            
            if Szname[i] == "off":
                self.__aktiveWege.append(False)
            else:
                #self.__wege.append(Szname[i]) = self.__
                self.__aktiveWege.append(True)
                #print("APPEND ->",end='')
                #print(Szname[i])
                self.__commands[Szname[i]] = self.gehen
            i = i + 1
        
        self.__wege[Szname[0]] = self.__oben
        self.__wege[Szname[1]] = self.__unten
        self.__wege[Szname[2]] = self.__links
        self.__wege[Szname[3]] = self.__rechts
        
        self.__name = name
        self.__besucht = False #Ob die Szene schon besucht wurde ( Boolean )
        self.__debug = debug
        self.__hungerAufwand = aufwand
        self.__items = items
        #self.__items = {"glas" : 1,"wasser" : 1} # value = anzahl noch vorhandener
            #self.__commands = {"nach oben" : self.gehen,"nach unten" : self.gehen,"nach links" : self.gehen,"nach rechts" : self.gehen,"glas nehmen" : self.take,"wasser nehmen" : self.take}
        
        #self.__commands = {Szname[0] : self.gehen,Szname[1] : self.gehen,Szname[2] : self.gehen,Szname[3] : self.gehen,"inventar anzeigen":self.showInv}
        self.__commands["inventar anzeigen"] = self.showInv
        for entry in self.__customText:
            #print(entry)
            self.__commands[entry] = self.__customText[entry]
       # self.__commands
        self.__run = True
        #Style
        self.__boarder = True
        self.__text = text
        #self.__text = "Ein toller Beispiel Text! Irgendetwas spannendes wird sicher passieren!"
        

        
    def take(self,item):
       # print("Glas genommen")
        temp = item[:item.find(" nehmen")]
        #print(temp)
        anzahl = self.__items[temp]
       # print(anzahl)
        if anzahl == 0:
            retval = False
            print("Du kannst " + temp + " nicht mehr nehmen! Es ist nichts mehr da!")
        else:
            print("Du hast " + temp + " genommen!")
            self.__items[temp] = self.__items[temp] - 1
            self.__player.addItem(temp)
            retval = True
        return(retval)
    def empty(self,arg2):
        return(True)
    
    def showInv(self,myIn):
        if len(self.__player.inventar) == 0:
            print("Du hast keine Items!")
        
        
        else:
            print("Du hast folgende Items: "),
            for item in self.__player.inventar:
                print(item),
                print(", "),
            print("")
            
    def gehen(self,MyInput):
        
        if MyInput == "1" or MyInput == "2" or MyInput == "3" or MyInput == "4":
            temp = self.__SZname[int(MyInput)-1]
            print("-----")
            print(temp)
        else:
            temp = MyInput
        #temp = MyInput[5:]
        
        #print(temp)
        wegId = self.__wege[temp]
        #print(wegId)
        self.__ausgang = wegId
        self.__run = False
       # nameByID = szenenMap[wegId].getName()
        #print(nameByID)
        #print("Du brichts auf Richtung " + nameByID + "!")
        self.__run = False
    def play(self,player):
        
        self.__player = player
        self.__text = self.__text.replace("[NAME]" , self.__player.name)
        self.__run = True
        self.__besucht = True
        whI = 0
        if self.__runFunc != cT.empty:
            self.__runFunc(self,player)
        else:
            if self.__boarder == True:
                print("-----------------------------------") #Spaeter responsiv
            print(self.__text)
            
            if self.__boarder == True:
                print("-----------------------------------")
        
         
        while self.__run == True:
            print("")
            print("Du kannst folgendes tun: ")
            for item in self.__items:
                self.__commands[item + " nehmen"] = self.take
                #print(items)
            for elemnt in self.__commands:
                print(elemnt)
            whI = 0
            while whI <= 2:
                print("")
                whI += 1
            temp = myInput("Deine Eingabe > ")
            print("")
            print("")
            if temp in self.__customText:
                if self.__commands[temp](self,player) == 1:
                    del(self.__commands[temp])
            elif temp in self.__commands:
                
                
                self.__commands[temp](temp)
            elif temp == "1" or temp == "2" or temp == "3" or temp == "4":
                if self.__SZname[int(temp)-1] == "off":
                    print("Unbekannter Befehl")
                else:
                    self.gehen(temp)
            elif temp == "*menu*":
                self.__pause = True
                print('''

          __  __                  
         |  \/  |                 
         | \  / | ___ _ __  _   _ 
         | |\/| |/ _ \ '_ \| | | |
         | |  | |  __/ | | | |_| |
         |_|  |_|\___|_| |_|\__,_|
                          
                (1) Fortsetzen
                (2) Speichern
                (3) Beenden


''')
                tempRun = True
                while tempRun:
                    
                    tempIn = myInput("> ")
                
                    if tempIn == "1":
                        tempRun = False
                    elif tempIn == "2":
                        print("Speichere...")
                        player.speichern()
                    elif tempIn == "3":
                        print("Wirklich beenden? (y/n)")
                        temp2 = myInput("-> ")
                        if temp2 == "y":
                            exit()
                        else:
                            print("Nicht beenden.")
                    else:
                        print("Unbekannter Befehl")
                self.__pause = False
            else:
                print("Unbekannter Befehl")
        return(self.__ausgang)
    
    def getAufwand(self):
        return(self.__hungerAufwand)
    def getName(self):
        return(self.__name)
    def getText(self):
        return(self.__text)
    def setStyle(self,boarder,text):
        self.__text = text
        self.__boarder = boarder
    def __str__(self):
        retval = " Szenen name = "
        retval += self.__name+"\n"
        retval += " Wurde die Szene besucht? = "
        retval += str(self.__besucht) + "\n"
        retval += " Hungeraufwand der Szene = "
        retval += str(self.__hungerAufwand) + "\n"
        retval += " Verfuegbare Items in der Szene = "
        retval += str(self.__items) + "\n"
        retval += " Vefuegbare Kommandos = "
        retval += str(self.__commands) + "\n"
        retval += " Nachbar Info: \n  Nachbar oben = "
        retval += str(self.__oben) + "\n  Nachbar unten = "
        retval += str(self.__unten) + "\n  Nachbar links = "
        retval += str(self.__links) + "\n  Nachbar rechts = "
        retval += str(self.__rechts) + "\n"
        return(retval)






