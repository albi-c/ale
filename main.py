#!/usr/bin/python3

import os
import sys
import tkinter as tk

try:
    from appJar import gui
except ImportError:
    print("Cannot find appJar!")
    sys.exit(1)

scriptdir = os.path.dirname(os.path.realpath(__file__))

afile = None
text = ""
lsaved = ""
fullScreen = False

root = tk.Tk()
root.withdraw()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def checkStop():
    global text
    global lsaved
    text = app.getTextArea("textArea")
    if lsaved != text:
        return app.yesNoBox("Confirm exit", "Are you sure you want to exit?")
    else:
        return True

def pressFileMenu(btn):
    global afile
    global text
    global lsaved
    if btn == "Open":
        afile = app.openBox(title="Open", parent=None)
        if type(afile) == str:
            with open(afile, "r+") as f:
                text = f.read()
            lsaved = text
            app.clearTextArea("textArea", False)
            app.setTextArea("textArea", text)
    elif btn == "Save":
        if type(afile) == str:
            text = app.getTextArea("textArea")
            with open(afile, "w+") as f:
                f.write(text)
            lsaved = text
        else:
            pressFileMenu("Save as...")
    elif btn == "Save as...":
        afile = app.saveBox(title="Save as...", parent=None, fileExt="")
        text = app.getTextArea("textArea")
        if type(afile) == str:
            with open(afile, "w+") as f:
                f.write(text)
            lsaved = text
    elif btn == "Close":
        app.stop()

def pressScreenMenu(btn):
    global fullScreen
    if btn == "Toggle FullScreen":
        fullScreen = not fullScreen
        if fullScreen:
            app.setSize("fullscreen")
        else:
            app.setSize("{0}x{1}".format(width, height - 100))

def keyPress(key):
    if key == "<Control-o>":
        pressFileMenu("Open")
    elif key == "<Control-s>":
        pressFileMenu("Save")
    elif key == "<Control-Shift-S>":
        pressFileMenu("Save as...")
    elif key == "<Control-Escape>":
        pressFileMenu("Close")

app = gui("ALE", "{0}x{1}".format(width, height - 100))

app.addMenuList("File", ["Open", "Save", "Save as...", "-", "Close"], pressFileMenu)
app.addMenuList("Screen", ["Toggle FullScreen"], pressScreenMenu)

app.addScrolledTextArea("textArea")

app.bindKey("<Control-o>", keyPress)
app.bindKey("<Control-s>", keyPress)
app.bindKey("<Control-Shift-S>", keyPress)
app.bindKey("<Control-Escape>", keyPress)

app.setStopFunction(checkStop)

app.go()
