from src import artwork
from src.steam import Steam
import argparse
import sys


def print_logo():
    print(artwork.ascii_art)
    print("Created by xriskon || Chris Konstantopoulos")
    print("https://github.com/xriskon\n")


def command_list():
    print("[target]\tchange target user")
    print("[info]\t\tdisplay summary of user")
    print("[friends]\tdisplay all friends")
    print("[games]\t\tdisplay all owned games")
    print("[list]\t\tshow command list")
    print("[quit]\t\texit program")
    print("[FILE=y]\tenable saving to file")
    print("[FILE=n]\tdisable saving to file")


def _quit():
    print("Bye!")
    sys.exit(1)


parser = argparse.ArgumentParser(description='Steam OSINT is a tool for gathering information about steam users')
parser.add_argument('id', type=str, help='username')
parser.add_argument('-o', '--output', help='output to file', action="store_true", required=False)
args = vars(parser.parse_args())

api = Steam(args.get("id"), args.get("output"))

commands = {
    'TARGET':   api.change_target,
    'LIST':     command_list,
    'HELP':     command_list,
    'QUIT':     _quit,
    'EXIT':     _quit,
    'INFO':     api.get_info,
    'FRIENDS':  api.get_friends_list,
    'GAMES':    api.get_owned_games
}


print_logo()
api.print_banner()
while True:
    cmd = input("New command:").upper()
    _cmd = commands.get(cmd)

    if _cmd:
        _cmd()
    elif cmd == "":
        print("")
    else:
        print("Unknown command\n")
