import os, json

with open("scripts/settings.json", "r") as j: settings = json.load(j)

if settings["first_start"]: os.startfile("warning.vbs")
else: os.startfile("RussianCookie.exe")
