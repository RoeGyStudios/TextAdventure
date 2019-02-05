 #-*- coding: utf-8 -*-
from szene import *
from playerClass import *
from langHandler import *
from logger import *
import startUmenu as sUm
import pickle

def myInput(prompt):
    try:
        temp = raw_input(prompt)
    except NameError:
        temp = input(prompt)
    return(temp)



def gamestart():
    

    langOb = initLang("DE_DE")
    inp = myInput("Was ist dein Name? > ")
    player1 = Person(inp,100,100,100,[])

    s0 = szeneStandart(langOb["haus1"],0,0,1,0,0,langOb["text1"], {},2,["off",langOb["M_treppe_runter"],"off","off"],{"raus gucken":cT.text1})
    s1 = szeneStandart(langOb["haus1_eg"],1,0,1,2,1,langOb["text3"] + "",{langOb["I_apfel"]:3},1,[langOb["M_treppe_hoch"],"off", langOb["T_z_door"] + " rausgehen","off"])
    s2 = szeneStandart(langOb["vorgarten"],2,20,1,2,3,langOb["text4"], {},1,[langOb["M_Auf_str"],"Durch die Tür reingehen","off","off"])
    sStr = szeneStandart(langOb["W_str"],20,4,2,3,8,"Du bist auf der Straße", {},1,[langOb["T_in"] + langOb["vorgarten_nachbar"] + langOb["T_go"],langOb["T_in"] + langOb["vorgarten"] + langOb["T_go"],langOb["T_goto_2"] + langOb["dorfplatz"] + langOb["T_go"],langOb["Route_311"]]) 
    s3 = szeneStandart(langOb["dorfplatz"],3,7,20,5,6,langOb["text5"],{},2,["Laden",langOb["M_Auf_str"],langOb["M_zu_resto"],langOb["T_goto"] + " " + langOb["apo"]])
    s4 = szeneStandart(langOb["vorgarten_nachbar"],4,4,20,4,4,langOb["text6"],{},0,["off",langOb["M_Auf_str"],"off","off"],{langOb["T_nachbar_ansp"]:cT.text2})
    s5 = szeneStandart(langOb["resto"],5,5,3,5,3,langOb["text7"],{},0,["off","off","off",langOb["M_resto_quit"]],{langOb["resto_karte"]:cT.karte})
    s6 = szeneStandart(langOb["apo"],6,6,6,3,6,langOb["text8"],{},0,["off","off",langOb["M_zum_Dorfplatz"],"off"],{})
    s7 = szeneStandart(langOb["M_laden"],7,9,3,9,9,langOb["text10"],{},0,["off",langOb["T_goto_2"] + langOb["dorfplatz"] + langOb["T_go"],"off","off"],{})
    s8 = szeneStandart(langOb["Route_311"],8,7,7,20,12,langOb["text9"],{},0,["off","off",langOb["M_Auf_str"],langOb["M_Auf_str-2"]],{}) 
    s9 = szeneStandart(langOb["dorfplatz"] + " 2",9,12,10,99,0,langOb["text12"],{},0,[langOb["M_Auf_str-2"],langOb["T_goto"] + langOb["bar"],"Zur Mine gehen","off"],{})
    s10 = szeneStandart(langOb["bar"],10,9,0,0,0,langOb["T_bar"],{},0,[langOb["M_dorfplatz"],"off","off","off"],{langOb["T_zum_tr"]:cT.barText})
    #s11 = szeneStandart("Mine)
    s12 = szeneStandart(langOb["W_str"] + " 2",12,9,0,12,8,langOb["textStr2"],{},0,[langOb["T_goto_2"] + langOb["dorfplatz"] + " 2 " + langOb["T_go"],"off",langOb["T_goto"] + langOb["Route_311"],"off"],{})
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
                 7 : s7,
                 8 : s8,
                 9 : s9,
                 10: s10,
                 12 : s12,
                 20 : sStr,
                 99: end}    #Szenen map
    startSzene = 0
    endSzene = 10
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
        if aktuSzene == -2:
            log("Info","Main Menu jump",True)
            sUm.showMenu()
        print(langOb["szeneChange"] + szenenMap[aktuSzene].getName() + "!")
        player1.aktualisieren()
        
        #player1.show()
        #print(szenenMap[aktuSzene])

if __name__=="__main__":
    gamestart()
