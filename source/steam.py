import requests
import json
from prettytable import PrettyTable

key = "CBEBD2AF8F17879A8FEE29F695F6BD9A"


def ownedGames(user):
    response = requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={user}&format=json&include_appinfo=true&76561198111662340")
    if userExists(user):
        data = response.json()["response"]
        with open("out.json", "w", encoding="utf8") as f:
            json.dump(data, fp=f, indent=4)
        table = PrettyTable()
        table.field_names = ["App ID", "Name", "Playtime"]
        for game in data["games"]:
            table.add_row([game["appid"], game["name"], str(round(game["playtime_forever"] / 60)) + " Hours"])
        with open("output\games.txt", "w", encoding="utf8") as f:
            f.write(str(table))
            f.writelines(f"\nGames of user: {getName(user)}")
            f.writelines("\nGames count: %s" % data["game_count"])
        return table
    else:
        print(f"User with steamID64: {user}, doesn't exist")


def achievements(user, game):
    response = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game}&key={key}&steamid={user}")

    with open("output\out.json", "w", encoding="utf8") as f:
        json.dump(response.json(), fp=f, indent=4)
    return 1


def summary(user):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={user}")


def friends(user):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={key}&steamid={user}&relationship=friend")
    if response.status_code == 200:
        data = response.json()
        table = PrettyTable()
        table.field_names = ["Steam ID", "Username", "Profile State", "Friends Since"]
        for friend in data["friendslist"]["friends"]:
            friendResponse = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (key, friend["steamid"]))
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
        return table


def statsGame(user, game):
    response = requests.get(f"http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid={game}&key={key}&steamid={user}")


def recenlyPlayed(user):
    response = requests.get(f"http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key={key}&steamid={user}&format=json")
    data = response.json()["response"]
    table = PrettyTable()
    table.field_names = ["AppID", "Name", "Playtime last 2 weeks", "All-time playtime"]
    for game in data["games"]:
        table.add_row([game["appid"], game["name"], str(round(game["playtime_2weeks"]/60, 1)) + " Hours", str(round(game["playtime_forever"]/60, 1)) + " Hours"])
    return table


def userExists(userID):
    response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={key}&steamids={userID}")
    if response.status_code != 200:
        return False
    else:
        return True


def getName(userID):
    response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (key, userID))
    user = response.json()
    return user["response"]["players"][0]["personaname"]
