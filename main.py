import sys
import source.user as user

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Required argument: username" if len(sys.argv) == 1 else "Only one username can be parsed at a time")
    exit(1)


def main():
    target = sys.argv[1]
    personName = user.getName(target)
    print("Steam OSINT ####### created by Chris")
    print(f"Target: {personName}")
    printMenu()
    while True:
        answer = input("New command:")

        if answer == "user":
            target = changeUser()
        elif answer == "sum":
            print(user.summary(target))
        elif answer == "games":
            print(user.ownedGames(target))
        elif answer == "achie":
            print(user.achievements(target))
        elif answer == "friends":
            print(user.friends(target))
        elif answer == "recpl":
            print(user.recenlyPlayed(target))
        elif answer == "stats":
            print(user.statsGame(target))
        elif answer == "list":
            printMenu()
        elif answer == "exit":
            print("Ok, Bye!")
            exit(0)
        else:
            print("Unknown command")


def changeUser():
    answer = input("Enter target's steamID64:")
    # VERIFY USER EXISTS
    # IF INPUT IS USERS UNIQUE URL FIND STEAMID64 FROM IT
    return answer


def printMenu():
    print("[user] ---- Change target user")
    print("[sum] ----- Show target's summary")
    print("[games] --- Show target's owned games")
    print("[achie] --- Show target's achievements")
    print("[friends] - Show target's friends list")
    print("[recpl] --- Show target's recently played games")
    print("[stats] --- Show target's game stats (must provide game ID)")
    print("[list] ---- Show command list")
    print("[exit] ---- Exit the application\n")


if __name__ == '__main__':
    main()
