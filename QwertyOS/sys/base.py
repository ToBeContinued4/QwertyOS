import os, time

os.system("cls")

def defaultIntro():
    print("Welcome to QwertyOS demo\n")
    time.sleep(1)
    print("(This is a demo version of Qwerty OS, new things and updates coming soon)\n")
    time.sleep(1)
    os.system("pause")
    consoleStart()

def consoleStart():
    os.system("cls")
    os.system("type titleascii.txt")
    print("\n")
    inputOS = str(input("] "))
    
    if inputOS == "help":
        os.system("cls")
        os.system("type commandlist.txt")
        time.sleep(1)
        print("\n")
        os.system("pause")
        consoleStart()

    if inputOS == "themes":
        themeMenu()

    if inputOS == "install":
        installMenu()
    
    if inputOS == "install-list":
        os.startfile("install-list.bat")
        consoleStart()
    
    if inputOS == "start":
        startMenu()
    
    if inputOS == "exit":
        exit(0)
    
    if inputOS == "":
        os.startfile("commandmissing.vbs")
        consoleStart()
    
    else:
        os.startfile("wrongcommand.vbs")
        consoleStart()

def themeMenu():
    os.system("cls")
    print("Color themes\n")
    print("- Hacker")
    print("- Setup\n")
    themeOS = str(input("] "))

    if themeOS == "hacker":
        os.system("color 0a")
        themeMenu()

    if themeOS == "setup":
        os.system("color 17")
        themeMenu()

    if themeOS == "reset":
        os.system("color 07")
        themeMenu()
    
    if themeOS == "exit":
        consoleStart()
    
    if themeOS == "":
        os.startfile("commandmissing.vbs")
        themeMenu()
    
    else:
        os.startfile("wrongcommand.vbs")
        themeMenu()

def installMenu():
    print("\n")
    installOS = input("Install ] ")

    if installOS == "exit":
        consoleStart()
    
    if installOS == "":
        os.startfile("commandmissing.vbs")
        installMenu()
    
    else:
        os.startfile("wrongcommand.vbs")
        installMenu()

    os.system("installprogram " + installOS)
    exit(0)

def startMenu():
    print("\n")
    startOS = input("Start ] ")

    if startOS == "exit":
        consoleStart()
    
    if startOS == "":
        os.startfile("commandmissing.vbs")
        startMenu()
    
    else:
        os.startfile("wrongcommand.vbs")
        startMenu()

    os.system("startprogram " + startOS)
    os.system("pause")
    consoleStart()

defaultIntro()
