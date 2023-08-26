#BIOME HOPPER 3000!!!!!

import requests,webbrowser,json,pyautogui,time,datetime,subprocess,os,keyboard
from PIL import Image

settings = None
with open("./settings.json","r",encoding="utf-8") as file:
    settings=json.load(file)
    print("yooooooo loaded! beginning in 2 seconds.")
    time.sleep(2)
#webhook = Webhook.from_url(settings["webhook"])
# send data:
def returnctime():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
def sendbywebhook(the):
    if settings["webhook"]=="None":
        return
    the["content"]=the["content"]+" ("+str(returnctime())+")"
    requests.post(settings["webhook"],the)
    #await webhook.send(content=the["content"],file=the["file"],files=the["files"], tts=the["tts"], embed=the["embed"], embeds=the["embeds"], delete_after=the["delete_after"], suppress_embeds=the["suppress_embeds"], silent=the["silent"])
data = {
    "content":"# SUPER BIOME HOPPER 😎😎😎 3000 STARTED"}
sendbywebhook(data)

def mathclamp(num,min,max):
    newnum = num
    if num>max:
        newnum=max
    elif num<min:
        newnum=min
    return newnum
def findimage(imagename,conf):
    return pyautogui.locateOnScreen("./images/"+imagename,confidence=conf)
skippablebosses={"paladin","fallen","machine","archmage","controller","steve","ripper"}
worthskipping = {#793,81 ; 795,328
"blizzard","flame","forest","irradiated","moon","pvc","star","storm","DIDNT_LOAD"
}
rarebiomes = {"hvuh","void","angel","cult","bene","asta"}
def finishfunc(key):
    data = {
        "content":"## PRESSED STOP KEY ("+(settings["keytopause"]).upper()+") STOPPING NOW",
    }
    sendbywebhook(data)
    os.kill(os.getppid(),9) #changing to 0 will error

keyboard.on_press_key(settings["keytopause"],finishfunc)
def unbreakablehumanspirit():
    timestried=0
    biomefound = False
    whichbiomefound = "None"
    while biomefound==False:
        loadedin = False
        whichbiomefound="None"
        data = {
        "content":"* opening the vip link now",
        }
        sendbywebhook(data)
        webbrowser.open_new_tab(settings["vip"])
        while loadedin==False:
            #craftingmenu.png
            time.sleep(1)
            if findimage("craftingmenu.png",.7)!=None:
                loadedin = True
        #close browser here so it doesnt eat your ram 🐏
        subprocess.call("TASKKILL /IM "+settings["browsertoclose"]+".exe /F",shell= True)
        screenshot = pyautogui.screenshot()
        screenshot.save("tempscreen.png")
        towait = mathclamp(settings["waitbeforerejoin"],20,120)
        #with open("tempscreen.png","rb") as fil:
            #scr = discord.file(fil)
        data = {
        "content":"## Roblox loaded!",
        #"file": scr
        }
        sendbywebhook(data)
        os.remove("tempscreen.png")
        #click once to focus in the window and then zoomout
        data = {
        "content":"* focusing into roblox.",
        }
        sendbywebhook(data)
        pyautogui.click(button="left",x=1600/2,y=900/2,clicks=15,interval=.1)
        time.sleep(2)
        #hold O for 2 seconds to zoom out
        for i in range(20):
            keyboard.press('o')
            time.sleep(0.1)
        keyboard.release('o')
        keyboard.press_and_release("tab")
        data = {
        "content":"* zoomed out.",
        }
        sendbywebhook(data)
        time.sleep(1)
        data = {
        "content":"* Waiting "+str(towait)+" seconds now.",
        }
        sendbywebhook(data)
        keyboard.press(mathclamp(settings["whichslottoequip"]+1,2,10))#equip item
        for i in range(1,towait,1):
            time.sleep(1)
            currentscreen = pyautogui.screenshot()
            pyautogui.click(button="left",x=1600/2,y=900/2)
            keyboard.press_and_release('z, x, c')#incase its an item
            #search for biome chat message
            yepifoundit = False
            nahskip = False
            #check rare first
            for biome in rarebiomes:
                #check 2 pixels #793,81 ; 795,328
                biomescreenshot = Image.open("./images/"+biome+".png")
                if currentscreen.getpixel((793,81))==biomescreenshot.getpixel((793,81)) and currentscreen.getpixel((793,328))==biomescreenshot.getpixel((793,328)):
                    yepifoundit=True
                    whichbiomefound=biome
                    break
            #no rare?
            if yepifoundit==False:
                for boss in skippablebosses:
                    if findimage(boss+".png",.9)!=None:
                        nahskip=True
                        whichbiomefound=boss
                        break
                for bad in worthskipping:
                    biomescreenshot = Image.open("./images/"+bad+".png")
                    if currentscreen.getpixel((793,81))==biomescreenshot.getpixel((793,81)) and currentscreen.getpixel((793,328))==biomescreenshot.getpixel((793,328)):
                        nahskip=True
                        whichbiomefound=bad
                        break

            data = {
            "content":"* "+str(i)+"/"+str(towait)+"s passed; good biome: "+str(yepifoundit)+", bad biome: "+str(nahskip)+", which: "+str(whichbiomefound),
            }
            sendbywebhook(data)
            if yepifoundit==True:
                biomefound=True
                break
            elif nahskip==True:
                break
        if biomefound==True:
            data = {
            "content":"# "+(whichbiomefound).upper()+" FOUND @everyone\n# "+settings["vip"]+"\nonly took "+str(timestried)+" tries!"}
            sendbywebhook(data)
        else:
            timestried+=1
            data = {
            "content":"* skipped "+whichbiomefound+". ["+settings["strugglemessage"]+"]("+settings["struggleattachment"]+") #"+str(timestried)}
            sendbywebhook(data)
            #close roblox here
            subprocess.call("TASKKILL /IM RobloxPlayerBeta.exe /F",shell= True)
        #loops until biome found
    # :zxczxczxc
    #print("ended")

unbreakablehumanspirit()