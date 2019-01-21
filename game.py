 #-*- coding: utf-8 -*-
from szene import *
from playerClass import *
from langHandler import *
from logger import *
import pickle
    
def gamestart():
    

    langOb = initLang("DE_DE")

    player1 = Person("Peter",100,100,100,[])

    s0 = szeneStandart(langOb["haus1"],0,0,1,0,0,langOb["text1"], {},2,["off","(2) " + langOb["M_treppe_runter"],"off","off"],{"raus gucken":cT.text1})
    s1 = szeneStandart(langOb["haus1_eg"],1,0,1,2,1,langOb["text3"],{langOb["I_apfel"]:3},1,["(1) " + langOb["M_treppe_hoch"],"off","(3) Zur Tür rausgehen","off"])
    s2 = szeneStandart(langOb["vorgarten"],2,7,3,2,3,langOb["text4"], {},1,["(1) " + langOb["M_Auf_str"],"(2) Durch die Tür reingehen","off","off"])
    sStr = szeneStandart(langOb["W_str"],7,4,2,3,8,"Du bist auf der Straße", {},1,["(1) " + langOb["T_in"] + langOb["vorgarten_nachbar"] + langOb["go"],"(2) " + langOb["T_in"] + langOb["vorgarten"] + langOb["T_go"],"(3) " + langOb["T_goto_2"] + langOb["dorfplatz"] + langOb["T_go"],"(4) " + langOb["Route_311"]]) 
    s3 = szeneStandart(langOb["dorfplatz"],3,9,7,5,3,langOb["text5"],{},2,["(1) Laden","(2) " + langOb["M_Auf_str"],"(3) " + langOb["M_zu_resto"],"(4) " + langOb["T_goto"] + " " + langOb["apo"]])
    s4 = szeneStandart(langOb["vorgarten_nachbar"],4,4,7,4,4,langOb["text6"],{},0,["off","(2) " + langOb["M_Auf_str"],"off","off"],{langOb["T_nachbar_ansp"]:cT.text2})
    s5 = szeneStandart(langOb["resto"],5,5,3,5,3,langOb["text7"],{},0,["off","off","off","(4) " + langOb["M_resto_quit"]],{langOb["resto_karte"]:cT.karte})
    s6 = szeneStandart(langOb["apo"],6,6,6,3,6,langOb["text8"],{},0,["off","off","(3) " + langOb["M_zum_Dorfplatz"],"off"],{})
    s7 = szeneStandart(langOb["Route_311"],8,8,8,7,9,langOb["text9"],{},0,["off","off","(3) " + langOb["M_Auf_str"],"(4) " + langOb["empty"]],{})
    s8 = szeneStandart(langOb["M_laden"],9,9,3,9,9,langOb["text10"],{},0,["off","(2) " + langOb["T_goto_2"] + langOb["dorfplatz"] + langOb["go"],"off","off"],{})


    end = demoEnd("Ende",99)
    #picklestring = pickle.dumps(s8)
    #print(picklestring)
    szenenMap = {0 : s0,
                 1 : s1,
                 2 : s2,
                 3 : s3,
                 4 : s4,
                 5 : s5,
                 6 : s6,
                 7 : sStr,
                 8 : s7,
                 9 : s8,
                 99: end}    #Szenen map
    startSzene = 0
    endSzene = 9
    aktuSzene = 0
    #print(szenenMap)
    i=0
    while i <= 50:
        print("")
        i = i + 1
    while True:
        aktuSzene = szenenMap[aktuSzene].play(player1)
        if aktuSzene == -1:
            log("Info","Szenenevent gesteuerter Exit",True)
            exit()
        print(langOb["szeneChange"] + szenenMap[aktuSzene].getName() + "!")
        player1.aktualisieren()
        
        player1.show()
        #print(szenenMap[aktuSzene])

if __name__=="__main__":
    gamestart()
