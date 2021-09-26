@ECHO OFF
cls
title PY to EXE
color a
pyinstaller --onefile --windowed RussianCookie.py
pyinstaller --onefile --windowed "Russian Cookie.py"
rmdir /S /Q build
rmdir /S /Q __pycache__
del RussianCookie.spec
del Russian Cookie.spec