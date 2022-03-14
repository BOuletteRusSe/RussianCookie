from os import startfile
from json import load

with open("settings.json", "r") as j: settings = load(j)

if settings["first_start"]: startfile("warning.vbs")
else: startfile("RussianCookie.exe")
