from src import artwork
from src.steam import Steam
import argparse
import sys


def print_logo():
    print(artwork.ascii_art)
    print("Created by xriskon || Chris Konstantopoulos")
    print("https://github.com/xriskon\n")


def command_list():
    print("[propic]\tDownload profile picture")
    print("[info]\t\tDisplay summary of user")
    print("[friends]\tDisplay all friends")
    print("[recpl]\t\tDisplay recently played games")
    print("[games]\t\tDisplay all owned games")
    print("[list]\t\tShow command list")
    print("[quit]\t\tExit program")


def _quit():
    print("Bye!")
    sys.exit(1)


parser = argparse.ArgumentParser(description='Steam OSINT is a tool for gathering information about steam users')
parser.add_argument('id', type=str, help='username')
parser.add_argument('-o', '--output', help='output to file', action="store_true", required=False)
args = vars(parser.parse_args())

api = Steam(args.get("id"), args.get("output"))

commands = {
    'list':     command_list,
    'help':     command_list,
    'quit':     _quit,
    'exit':     _quit,
    'propic':   api.get_profile_picture,
    'info':     api.get_info,
    'friends':  api.get_friends_list,
    "recpl":    api.get_recently_played,
    'games':    api.get_owned_games
}


print_logo()
api.print_banner()
while True:
    cmd = input("New command:")
    _cmd = commands.get(cmd)

    if _cmd:
        _cmd()
    elif cmd.upper() == "FILE=Y":
        api.set_write_file(True)
    elif cmd.upper() == "FILE=Y":
        api.set_write_file(False)
    elif cmd == "":
        print("")
    else:
        print("Unknown command\n")
