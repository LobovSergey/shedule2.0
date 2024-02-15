import os.path
import json


class SetSetting:

    def data_read(self, file_name):
        with open(os.path.abspath(file_name), 'r', encoding="utf-8") as file:
            data = json.load(file)
            return data
