from src import config
import xlsxwriter
import requests
import json
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
        # response = requests.get("")
        # if response.status_code != 200:
        #     print(f"Error contancting with steam API\nStatus Code: {response.status_code}")
        #     sys.exit(1)

        # workbook = xlsxwriter.Workbook("output/info.xlsx")
        # worksheet = workbook.add_worksheet()
        # worksheet.set_column('A:A', 20)
        # bold = workbook.add_format({'bold': True})
        # worksheet.write('A1', 'Hello')
        # worksheet.write('B2', 'World', bold)
        # worksheet.write(2, 0, 123)
        # worksheet.write(3, 0, 123.456)
        # workbook.close()

        # self.steamID = data["steamID"]
        # self.steamID64 = data["steamID64"]
        # self.is_private = data["is_private"]
        # self.write_file = write_file

    def __search_user(self, user):
        result = {
            "steamID": None,
            "steamID64": None,
            "is_private": True,
            "found": False
        }
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

    def set_target(self, target):
        _user = input("New target: ")
        data = self.__search_user(_user)
        if data.get("found"):
            self.steamID = data.get("steamID")
            self.steamID64 = data.get("steamID64")
            self.is_private = data.get("is_private")
        else:
            print(f'User "{_user}" not found')

    def set_write_file(self, flag):
        if flag:
            print("Write to File: ENABLED")
        else:
            print(r"Write to File: DISABLED")

        self.write_file = flag

    def get_info(self):
        pass

    def get_recently_played(self):
        pass

    def get_friends_list(self):
        pass

    def get_owned_games(self):
        pass

    def get_profile_picture(self):
        pass
