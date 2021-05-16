import os
import json
import requests
import user

apiKey = "CBEBD2AF8F17879A8FEE29F695F6BD9A"


def main():
    target = ''
    while True:
        print("Steam OSINT ####### created by Chris")

        # CHECK FOR USER
        if target == '':
            print("No valid user")
            answer = input("Please insert target user ID:")
            if requests.get(f"https://steamcommunity.com/id/{answer}").status_code != 200:
                continue
            else:
                target = answer

        print(f"Target: {target}")
        print("-user: Change target user")
        print("-sum: Show target's summary")
        print("-games: Show target's owned games")
        print("-achie: Show target's achievements")
        print("-friends: Show target's friends list")
        print("-recpl: Show target's recently played games")
        print("-stats: Show target's game stats (must provide game ID)")
        answer = input("New command:")
        if answer == "user":
            pass
        elif answer == "sum":
            user.summary(target)
        elif answer == "games":
            user.ownedGames(target)
        elif answer == "achie":
            user.achievements(target)
        elif answer == "friends":
            user.friendList(target)
        elif answer == "recpl":
            user.recenlyPlayed(target)
        elif answer == "stats":
            user.statsGame(target)


if __name__ == '__main__':
    main()
