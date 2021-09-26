import os, ctypes, sys
    

if ctypes.windll.shell32.IsUserAnAdmin():
    
    os.startfile("warning.vbs")

else: ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[0:]), None, 1)
