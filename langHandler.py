import sys
def initLang(lang):
    #print(type(lang))
    if lang[2] != "_":
        raise NameError("LANG format wrong")
    if sys.platform.startswith("win"):
        print("[Info] Using Windows path")
        fileName = '.\lang\ '
        fileName = fileName[:7] + lang + ".txt"
    elif sys.platform.startswith("linux"):
        print("[Info] Using Linux path")
        fileName = "./lang/" + lang + ".txt"
    else:
        print("[Info] Unsupported System")
        raise SystemError("Unsupported System")
    #fileName =
    file = open(fileName,"r")
    content = file.readlines()
    file.close()
    #print(content)
   # print(len(content))
    out = {}
    for line in content:
        temp = line.split("=")
        temp[1] = temp[1][:len(temp[1])-1]
        out[temp[0]] = temp[1]
        
        #print(temp)
    
    return(out)
