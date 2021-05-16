import requests
import json
from prettytable import PrettyTable
from bs4 import BeautifulSoup

key = "CBEBD2AF8F17879A8FEE29F695F6BD9A"


def ownedGames(user):
    response = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={user}&format=json&include_appinfo=true&76561198111662340")
    if response.status_code == 200:
        data = response.json()
        table = PrettyTable()
        table.field_names = ["App ID", "Name"]
        for i in data["response"]["games"]:
            table.add_row([i["appid"], i["name"]])
        with open("output\games.txt", "w", encoding="utf8") as f:
            f.write(str(table))
            f.writelines(f"\nGames of user:{user}")
            f.writelines("\nGames count:%s" % data["response"]["game_count"])
        print(table)
    else:
        print(f"Couldn't find user: {user}")


def achievements(user, game):
    response = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game}&key={key}&steamid={user}")


def summary(user):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={user}")


def friendList(user):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={user}&relationship=friend")


def statsGame(user, game):
    response = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game}&key={key}&steamid={user}")


def recenlyPlayed(user):
    response = requests.get(f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={key}&steamid={user}&format=json")
