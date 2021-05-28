import requests
import json
import xmltodict
from prettytable import PrettyTable

key = "CBEBD2AF8F17879A8FEE29F695F6BD9A"
saveFile = True


class User:
    userID = None
    username = None

    def __init__(self):
        self.setUserID()

    def summary(self):
        global saveFile
        response = requests.get(f"https://steamcommunity.com/profiles/{self.userID}/?xml=1")
        data = xmltodict.parse(response.content)["profile"]
        if not ("customURL" in data):
            data["customURL"] = "None"
        if not ("realname" in data):
            data["realname"] = "None"
        if not ("location" in data):
            data["location"] = "None"
        if not ("memberSince" in data):
            data["memberSince"] = "None"
        result = f"SteamID64: {data['steamID64']}\nCustomURL: {data['customURL']}\nUsername: {data['steamID']}\nReal Name: {data['realname']}\n" \
                 f"Location: {data['location']}\nVac Ban: {data['vacBanned']}\nTrade Ban: {data['tradeBanState']}\nOnline State: {data['onlineState']}\n" \
                 f"Privacy State: {data['privacyState']}\nMemberSince: {data['memberSince']}"
        if saveFile:
            save(result, "summary", "TXT")
        return result

    def friendsList(self):
        global saveFile
        response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={self.userID}&relationship=friend")
        data = response.json()
        table = PrettyTable()
        table.field_names = ["Steam ID", "Custom URL", "Username", "Real Name", "Location", "VAC Ban", "Trade Ban", "Online State", "Privacy State", "Member Since"]
        for friend in data["friendslist"]["friends"]:
            steamID = friend["steamid"]
            response = requests.get(f"https://steamcommunity.com/profiles/{steamID}/?xml=1")
            data = xmltodict.parse(response.content)["profile"]
            if not("customURL" in data):
                data["customURL"] = "None"
            if not("realname" in data):
                data["realname"] = "None"
            if not("location" in data):
                data["location"] = "None"
            if not("memberSince" in data):
                data["memberSince"] = "None"
            table.add_row([data["steamID64"], data["customURL"], data["steamID"], data["realname"], data["location"],
                           data["vacBanned"], data["tradeBanState"], data["onlineState"], data["privacyState"], data["memberSince"]])
        if saveFile:
            save(table, "friends", "TXT")
        return table

    def recentlyPlayed(self):
        pass

    def ownedGames(self):
        pass

    def gameAchievements(self, appID):
        pass

    def gameStats(self, appID):
        pass

    def setUserID(self):
        while True:
            self.userID = input("Insert steamID64\n?")
            response = requests.get(f"https://steamcommunity.com/profiles/{self.userID}/?xml=1")
            data = xmltodict.parse(response.content)
            if "response" in data:
                self.username = self.userID
                response = requests.get(f"http://steamcommunity.com/id/{self.username}/?xml=1")
                data = xmltodict.parse(response.content)
                if not("response" in data):
                    self.userID = data["profile"]["steamID64"]
                    break
            else:
                self.username = data["profile"]["steamID"]
                break

    @staticmethod
    def setSaveFile(__saveFile):
        global saveFile
        saveFile = __saveFile


class App:
    appID = None

    def news(self, userID):
        pass

    def achievements(self):
        global saveFile
        if saveFile:
            save()

    def setAppID(self):
        while True:
            self.appID = None
            app = input("Insert appID or name\n?")
            response = requests.get("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
            data = response.json()
            for game in data["applist"]["apps"]:
                if app == game["appid"] or app == game["name"]:
                    self.appID = game["appid"]
                    break
            if self.appID is None:
                print("Game not found")
            else:
                break

    @staticmethod
    def setSaveFile(__saveFile):
        global saveFile
        saveFile = __saveFile


def save(data, fileName, fileType):
    if fileType == "JSON":
        with open("output\%s.json" % fileName, "w", encoding="utf8") as file:
            out = json.dumps(data, indent=4)
    elif fileType == "TXT":
        with open("output\%s.txt" % fileName, "w", encoding="utf8") as file:
            file.write(str(data))
