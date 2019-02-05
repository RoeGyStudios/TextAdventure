import sys
import codecs
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
	#fileName = "./lang/" + lang + ".txt"
        raise SystemError("Unsupported System")
    #fileName =
    #file = open(fileName,"r")
    file = codecs.open(fileName, "r", "utf-8")
    content = file.readlines()
    file.close()
    #print(content)
   # print(len(content))
    out = {}
    linesI = 0
    for line in content:
        temp = line.split("=")
        try:
            temp[1] = temp[1][:len(temp[1])-2]
            out[temp[0]] = temp[1]
        except IndexError:
            linesI += 1
        
        
        #print(temp)
    tmp = "Ignored lines: "
    tmp += str(linesI)
    print(tmp)
    return(out)
