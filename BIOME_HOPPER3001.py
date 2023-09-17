#BIOME HOPPER 3000!!!!!

import discord_webhook,webbrowser,json,pyautogui,time,datetime,subprocess,os,keyboard,random
from PIL import Image

settings = None
with open("./settings.json","r",encoding="utf-8") as file:
    settings=json.load(file)
    print("yooooooo loaded! beginning in 2 seconds.")
    time.sleep(2)

# send data:
def returnctime():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
def sendbywebhook(the):
    if settings["webhook"]=="None":
        return
    the["content"]=the["content"]+" ("+str(returnctime())+")"
    wh = discord_webhook.DiscordWebhook(url=settings["webhook"],content=the["content"])
    if ('file' in the):
        with open(the["file"],"rb") as f:
            wh.add_file(file=f.read(),filename=the["file"])
    wh.execute()
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
worthskipping = settings["skippablebiomes"]
rarebiomes = settings["rarebiomes"]
finishall = False
def finishfunc(key):
    global finishall
    finishall=True
    data = {
        "content":"## PRESSED STOP KEY ("+(settings["keytopause"]).upper()+") STOPPING NOW",
    }
    sendbywebhook(data)
    os.kill(os.getppid(),9) #changing to 0 will error

keyboard.on_press_key(settings["keytopause"],finishfunc)
def unbreakablehumanspirit():
    global finishall
    timestried=0
    biomefound = False
    whichbiomefound = "None"
    while biomefound==False:
        if finishall==True:
            break
        loadedin = False
        loadedtimeout = 0
        whichbiomefound="None"
        data = {
        "content":"* opening the vip link now",
        }
        sendbywebhook(data)
        if finishall==False:
            webbrowser.open_new_tab(settings["vip"])
        while loadedin==False and loadedtimeout<180:
            time.sleep(1)
            loadedtimeout+=1
            if findimage("craftingmenu.png",.7)!=None:
                loadedin = True
        #close browser here so it doesnt eat your ram 🐏
        subprocess.call("TASKKILL /IM "+settings["browsertoclose"]+".exe /F",shell= True)
        if loadedin==False:
            #timed out, wait a little then restart
            if finishall==False:
                subprocess.call("TASKKILL /IM RobloxPlayerBeta.exe /F",shell= True)
            time.sleep(5)
            data = {
            "content":"## ⚠ Roblox took too long to load! <@"+settings["userid"]+"> Restarting.",
            }
            sendbywebhook(data)
            continue
        screenshot = pyautogui.screenshot()
        screenshot.save("tempscreen.png")
        towait = mathclamp(settings["waitbeforerejoin"],20,120)
        data = {
        "content":"## Roblox loaded!"+(settings["resetuponload"]==True and "Resetting to fix camera." or ""),
        "file":"tempscreen.png",
        }
        sendbywebhook(data)
        #os.remove("tempscreen.png") gets overwritten anyways, shouldnt take up that much space
        #this is really inconsistent i should find a better way of checking if ur camera is the wrong way around
        if settings["resetuponload"]==True:
            keyboard.press_and_release("esc")
            time.sleep(.1)
            keyboard.press_and_release("r")
            time.sleep(.1)
            keyboard.press_and_release("enter")
        #click once to focus in the window and then zoomout
        data = {
        "content":"* focusing into roblox.",
        }
        sendbywebhook(data)
        pyautogui.click(button="left",x=1600/2,y=(900/2)+random.randint(-5,5),clicks=15,interval=.1)
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
        time.sleep(2)
        data = {
        "content":"* Waiting "+str(towait)+" seconds now.",
        }
        sendbywebhook(data)
        for i in range(1,towait,1):
            time.sleep(1)
            if finishall==True:
                break
            currentscreen = pyautogui.screenshot()
            keyboard.press_and_release(str(settings["whichslottoequip"]))#equip item
            pyautogui.click(button="left",x=1600/2,y=(900/2)+random.randint(-5,5))
            keyboard.press_and_release('z, x, c')#incase its an item
            if i%15==0:#reset every 15s for alignment
                keyboard.press_and_release("esc")
                time.sleep(.5)
                keyboard.press_and_release("r")
                time.sleep(.5)
                keyboard.press_and_release("enter")
            #search for biome pixels
            yepifoundit = False
            nahskip = False
            #check rare first
            for biome in rarebiomes:
                #check 2 pixels #793,81 ; 795,328
                biomescreenshot = Image.open("./images/"+biome+".png")
                if currentscreen.getpixel((793,81))==biomescreenshot.getpixel((793,81)) and currentscreen.getpixel((1222, 345))==biomescreenshot.getpixel((1222, 345)):
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
                    #1222, 345
                    if currentscreen.getpixel((793,81))==biomescreenshot.getpixel((793,81)) and currentscreen.getpixel((1222, 345))==biomescreenshot.getpixel((1222, 345)):
                        nahskip=True
                        whichbiomefound=bad
                        break

            data = {
            "content":"* "+str(i)+"/"+str(towait)+"s passed; good biome: "+str(yepifoundit)+", bad biome: "+str(nahskip)+", which: "+str(whichbiomefound),
            }
            if i%settings["screenshotstatusinterval"]==0:
                currentscreen.save("tempscreen.png")
                data["file"]="tempscreen.png"
            sendbywebhook(data)
            if yepifoundit==True:
                biomefound=True
                break
            elif nahskip==True:
                break
        if biomefound==True:
            data = {
            "content":"# "+(whichbiomefound).upper()+" FOUND "+(settings["pingeveryoneuponrare"]==True and "@everyone" or "<@"+settings["userid"])+">"+"\n# "+settings["vip"]+"\nonly took "+str(timestried)+" tries!"+(settings["afkfarm"]==True and "\n### AFK FARM IS ON, WILL CONTINUE RUNNING" or "")}
            sendbywebhook(data)
            if settings["afkfarm"]==True:
                #here we go
                biomefound=False #so that it doesnt stop after this is done
                rarebiomeended=False
                afktimeelapsed=0
                #start afk loop here
                while rarebiomeended==False:
                    if finishall==True:
                        break
                    time.sleep(1)
                    afktimeelapsed+=1
                    keyboard.press_and_release(str(settings["slottoafkfarm"]))#equip item
                    pyautogui.click(button="left",x=1600/2,y=(900/2)+random.randint(-5,5))
                    keyboard.press_and_release('z, x, c')#incase its an item
                    if afktimeelapsed%20==0:
                        keyboard.press_and_release("esc")
                        time.sleep(.5)
                        keyboard.press_and_release("r")
                        time.sleep(.5)
                        keyboard.press_and_release("enter")

                    currentscreen = pyautogui.screenshot()
                    biomescreenshot = Image.open("./images/normal.png")
                    if currentscreen.getpixel((793,81))==biomescreenshot.getpixel((793,81)) and currentscreen.getpixel((1222, 345))==biomescreenshot.getpixel((1222, 345)):
                        rarebiomeended=True

                    if rarebiomeended==True:
                        screenshot = pyautogui.screenshot()
                        screenshot.save("tempscreen.png")
                        timestried=0
                        data = {
                        "content":"## "+(whichbiomefound).upper()+" ended in "+str(afktimeelapsed)+"s!\nmacro will continue running as normal.",
                        "file":"tempscreen.png"}
                        sendbywebhook(data)

                        if finishall==False:
                            subprocess.call("TASKKILL /IM RobloxPlayerBeta.exe /F",shell= True)
                    else:
                        data = {
                        "content":"* "+(whichbiomefound).upper()+" has been going for "+str(afktimeelapsed)+"s."}
                        if afktimeelapsed%settings["screenshotstatusinterval"]==0:
                            currentscreen.save("tempscreen.png")
                            data["file"]="tempscreen.png"
                        sendbywebhook(data)
        else:
            timestried+=1
            data = {
            "content":"* skipped "+whichbiomefound+". ["+settings["strugglemessage"]+"]("+settings["struggleattachment"]+") #"+str(timestried)}
            sendbywebhook(data)
            #close roblox here
            if finishall==False:
                subprocess.call("TASKKILL /IM RobloxPlayerBeta.exe /F",shell= True)
        #loops until biome found
    #print("ended")

unbreakablehumanspirit()
os.remove("tempscreen.png") #clear tempscreen upon closing