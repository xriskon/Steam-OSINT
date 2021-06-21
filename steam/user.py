from steam import apiKey
import requests
import xmltodict

invalidCharacters = ['/', '<', '>', ':', '"', '/', '\\', '|', '?', '*']


def friends():
    pass


def games():
    pass


def search(user):
    response = requests.get(f"https://steamcommunity.com/profiles/{user}/?xml=1")
    data = xmltodict.parse(response.content)
    if "response" in data:
        response = requests.get(f"http://steamcommunity.com/id/{user}/?xml=1")
        data = xmltodict.parse(response.content)
        if not ("response" in data):
            return True
        else:
            return False
    else:
        return True


def __validateName():
    pass
