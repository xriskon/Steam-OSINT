try:
    with open(r"config\key.txt", 'r') as file:
        apiKey = file.read()
    if apiKey == '':
        print("key.txt is empty")
        exit(1)
    __all__ = ["user", "app"]
except FileNotFoundError as e:
    print(e, "key.txt doesn't exist")
    exit(1)
