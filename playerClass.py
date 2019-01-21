# -*- coding: cp1252 -*-
from time import *
from colorama import init, Fore, Back, Style
import pickle

class Person():
    def __init__(self, name, gesundheit, hunger, gold,inv):
        self.__armor = {"head":"empty","chest":"empty","legs":"empty","feet":"empty"}
        self.gesundheit = gesundheit
        self.hunger = hunger
        self.gold = gold
        #self.inventar = ["1", "2", "lool1", "Item 1"]
        self.inventar = inv
        self.name = name
        self.sekunde = time()
        self.__tod = False
    def aktualisieren(self):
        self.sekunde2 = time()
        self.hunger = self.hunger-int(self.sekunde2-self.sekunde)
        self.sekunde = time()
        if self.hunger <= 0:
            self.__tod = True
            print("Du bist Tod!")
    def speichern(self):
        dateiobjekt = open("Daten.txt","w")
        dateiobjekt.write(str(self.name+"\n"))
        dateiobjekt.write(str(self.gesundheit)+"\n")
        dateiobjekt.write(str(self.hunger)+"\n")
        dateiobjekt.write(str(self.gold)+"\n")
        dateiobjekt.write(str(self.inventar)+"\n")
       # picklestring = pickle.dumps(self)
       # dateiobjekt.write(picklestring)
        dateiobjekt.close()
    def laden(self):
        Dateiobjekt = open("Daten.txt","r")
        #self = pickle.load(dateiobjekt.read())
        #dateiobjekt.close()
        dateiinhalt = dateiobjekt.read().split("\n")
        self.name = dateiinhalt[0]
        self.gesundheit = int(dateiinhalt[1])
        self.hunger = int(dateiinhalt[2])
        self.gold = int(dateiinhalt[3])
        self.inventar = []
        invstr = dateiinhalt[4]
        invstr = invstr.replace(" ","")
        invstr = invstr.replace("[","")
        invstr = invstr.replace("]","")
        invstr = invstr.replace("'","")
        invstrneu = invstr.split(",")
        for x in invstrneu:
           self.inventar.append(x)
    def addItem(self,newItem):
        self.inventar.append(newItem)

    def getGold(self):
        return(self.gold)
    def show(self):
        init()
        out = ""
        out += "Name        : " + str(self.name) + "\n"
        #out += "Gesundheit  : " + str(self.gesundheit) + " "
        out += "Gesundheit  : %3d "% (self.gesundheit)
        intTemp = int(self.gesundheit / 10)
        if intTemp == 100:
            out += " "
        elif intTemp > 9 and intTemp < 100:
            out += "  "
        else:
            out += "   "
        i = 1
        out += "["
        while i <= intTemp:
            if i <= 4:
                out += Back.RED + " " + Back.RESET
            if i == 5 or i == 6 or i == 7:
                out += Back.YELLOW + " " + Back.RESET
            if i == 8 or i == 9 or i == 10:
                out += Back.GREEN + " " + Back.RESET
            i += 1
        out += "] \n"
        intTemp = int(self.hunger / 10)
        
        #out += str(int(self.hunger / 10))
        #out += Back.GREEN + " " + Back.RED + " " + Back.RESET + "\n"
        #out += "Hunger      : " + str(self.hunger)
        out += "Hunger      : %3d"% (self.hunger)
        #if intTemp == 100:
        #   out += " "
        if intTemp > 9 and intTemp < 100:
            out += "  "
        else:
            out += "   "
        i = 1
        out += "["
        while i <= intTemp:
            if i <= 4:
                out += Back.RED + " " + Back.RESET
            if i == 5 or i == 6 or i == 7:
                out += Back.YELLOW + " " + Back.RESET
            if i == 8 or i == 9 or i == 10:
                out += Back.GREEN + " " + Back.RESET
            i += 1
        out += "] \n"
        out += "Gold        : " + str(self.gold) + "\n"
        out += "Inventar    : " + str(self.inventar)
        print(out)
        
