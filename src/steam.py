from src import config
from prettytable import PrettyTable
import xmltodict
# import xlsxwriter
import requests
import sys


class Steam:
    api = None
    steamID = None
    steamID64 = None
    is_private = True
    write_file = True

    def __init__(self, user, write_file):
        self.api = config.get_api_key()
        self.write_file = write_file
        data = self.__search_user(user)
        if not data["found"]:
            print("Error")
            sys.exit(1)

        self.steamID = data["steamID"]
        self.steamID64 = data["steamID64"]
        self.is_private = data["is_private"]
        self.write_file = write_file

    @staticmethod
    def __search_user(target):
        result = {
            "steamID": None,
            "steamID64": None,
            "is_private": True,
            "found": False
        }

        response = requests.get(f"https://steamcommunity.com/profiles/{target}/?xml=1")
        data = xmltodict.parse(response.content)
        if "response" in data:
            response = requests.get(f"http://steamcommunity.com/id/{target}/?xml=1")
            data = xmltodict.parse(response.content)
            if not ("response" in data):
                result["steamID"] = data["profile"]["steamID"]
                result["steamID64"] = data["profile"]["steamID64"]
                if data["profile"]['privacyState'] == "public":
                    result["is_private"] = False
                else:
                    result["is_private"] = True
                result["found"] = True
            else:
                result["found"] = False
        else:
            result["steamID"] = data["profile"]["steamID"]
            result["steamID64"] = data["profile"]["steamID64"]
            if data["profile"]['privacyState'] == "public":
                result["is_private"] = False
            else:
                result["is_private"] = True
            result["found"] = True

        return result

    def print_banner(self):
        if self.is_private:
            print(f'{self.steamID64} - {self.steamID} [PRIVATE ACCOUNT]')
        else:
            print(f'{self.steamID64} - {self.steamID} [PUBLIC ACCOUNT]')

    def change_target(self):
        _user = input("New target: ")
        data = self.__search_user(_user)
        if data.get("found"):
            self.set_target(data)
        else:
            print("User was not found")

    def set_target(self, data):
        self.steamID = data.get("steamID")
        self.steamID64 = data.get("steamID64")
        self.is_private = data.get("is_private")

    def get_info(self):
        response = requests.get(f"https://steamcommunity.com/profiles/{self.steamID64}/?xml=1")
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
        print(result)

    def get_friends_list(self):
        response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.api}&steamid={self.steamID64}&relationship=friend")
        data = response.json()
        table = PrettyTable()
        table.field_names = ["Steam ID", "Username", "Profile State", "Friends Since"]
        for friend in data["friendslist"]["friends"]:
            friendResponse = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (self.api, friend["steamid"]))
            _user = friendResponse.json()
            state = _user["response"]["players"][0]["personastate"]
            if state == 1:
                _user["response"]["players"][0]["personastate"] = "Online"
            elif state == 2:
                _user["response"]["players"][0]["personastate"] = "Invisible"
            elif state == 3:
                _user["response"]["players"][0]["personastate"] = "Away"
            else:
                _user["response"]["players"][0]["personastate"] = "Offline"

            table.add_row([friend["steamid"], _user["response"]["players"][0]["personaname"],
                           _user["response"]["players"][0]["personastate"], friend["friend_since"]])

        print(table)

    def get_owned_games(self):
        response = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api}&steamid={self.steamID64}&format=json&include_appinfo=true")
        data = response.json()["response"]["games"]
        table = PrettyTable()
        table.field_names = ["App ID", "Title", "Playtime"]
        for game in data:
            table.add_row([game["appid"], game["name"], game["playtime_forever"]])
        print(table)

    # TODO: ADD ABILITY TO EXPORT DATA IN EXCEL FILE
    # Sample code below
    # workbook = xlsxwriter.Workbook("output/info.xlsx")
    # worksheet = workbook.add_worksheet()
    # worksheet.set_column('A:A', 20)
    # bold = workbook.add_format({'bold': True})
    # worksheet.write('A1', 'Hello')
    # worksheet.write('B2', 'World', bold)
    # worksheet.write(2, 0, 123)
    # worksheet.write(3, 0, 123.456)
    # workbook.close()
