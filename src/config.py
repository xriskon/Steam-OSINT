import sys

try:
    with open("config/key.txt", "r") as file:
        key = file.read()
except FileNotFoundError:
    print('Error: file "config/key.txt" not found!\n')
    sys.exit(1)
except Exception as e:
    print(f"Error: {format(e)}")
    sys.exit(1)


def get_api_key():
    return key
