import sys
import requests
import xmltodict
import json
from xml.etree import ElementTree
from source.steam import User
from source.steam import App


def changeMode():
    global mode
    print("Choose mode")
    print("[1] User")
    print("[2] App")
    while True:
        _mode = input("?")
        if _mode == '1' or _mode == '2':
            mode = _mode
            break


with open("artwork.txt", "r", encoding="utf8") as artwork:
    print(artwork.read())
print("Created by Chris Konstantopoulos\n")
mode = ''
changeMode()


def main():
    global mode
    if mode == '1':
        user = User()

        userMenu()
        while True:
            command = input("New command: ")
            if command == "user":
                pass
            elif command == "summ":
                result = user.summary()
            elif command == "games":
                pass
            elif command == "achie":
                appID = input("Insert appID\n?")
            elif command == "friends":
                result = user.friendsList()
            elif command == "recpl":
                pass
            elif command == "stats":
                appID = input("Insert appID\n?")
            elif command == "FILE=y":
                pass
            elif command == "FILE=n":
                pass
            elif command == "list":
                pass
            elif command == "mode":
                changeMode()
                main()
            elif command == "exit":
                print("Ok, Bye!")
                exit(0)
            else:
                print("Unknown command")
                continue
            print(result)
    else:
        app = App()
        app.setAppID()
        appMenu()
        while True:
            command = input("New command: ")
            if command == "app":
                app.setAppID()
            elif command == "news":
                pass
            elif command == "achi":
                pass
            elif command == "FILE=y":
                pass
            elif command == "FILE=n":
                pass
            if command == "list":
                pass
            elif command == "mode":
                changeMode()
                main()
            elif command == "exit":
                print("Ok, Bye!")
                exit(0)
            else:
                print("Unknown command")


def userMenu():
    print("[user] Change target user")
    print("[summ] Show target's summary")
    print("[games] Show target's owned games")
    print("[achi] Show target's achievements")
    print("[friends] Show target's friends list")
    print("[recpl] Show target's recently played games")
    print("[stats] Show target's game stats (must provide game ID)")
    print("[FILE=y] Enable saving to output folder")
    print("[FILE=n] Disable saving to output folder")
    print("[list]  Show command list")
    print("[mode] Change mode")
    print("[exit] Exit the application\n")


def appMenu():
    print("[app] Change target app")
    print("[news] Get latest news")
    print("[achi] Get global achievements")
    print("[FILE=y] Enable saving to output folder")
    print("[FILE=n] Disable saving to output folder")
    print("[list] Show all commands")
    print("[mode] Change mode")
    print("[exit] Exit the application\n")


if __name__ == '__main__':
    main()
