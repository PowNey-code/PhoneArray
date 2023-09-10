import json
import os
# import re
# import requests
from datetime import datetime as dt

P = os.path.dirname(os.path.abspath(__file__)) + '\\'

class Params:
    __instance = None
    __init = False
    NameFileParams = 'params.json'
    paramsDefault = {
        'Auto_Update': {
            'folder': 'Arrays',
            'update_frequency': 30,
            'last_Update': '06.08.2023',
            'URL_Update': 'opendata.digital.gov.ru/downloads/',
            'Arrays': ['DEF-9xx', 'ABC-8xx', 'ABC-4xx', 'ABC-3xx']
        },
        'SrcNew_cols_with_address': ['mesto_gitelstva', 'uehal'],
        'Prepare_Date': 'None'
    }

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Params, cls).__new__(cls)

        return cls.__instance

    def __del__(cls):
        cls.__instance = None

    def __init__(self):
        if not self.__init:
            self.__init = True

            self.prm = {}
            if os.path.isfile(P + self.NameFileParams):
                with open(P + self.NameFileParams) as File:
                    self.prm = json.load(File)

            if len(self.prm) < len(self.paramsDefault):
                self.prm = self.paramsDefault.copy()
                if self.writeParams(self.prm) == False:
                    print('Ошибка сохранения файла настроек')

    def get_default(self):
        return self.paramsDefault
        
    # ----- Получить/Установить дату последнего обновления номерных ёмкостей
    def get_last_Update(self):
        return dt.strptime(self.prm['Auto_Update']['last_Update'], '%d.%m.%Y').date()

    def set_last_Update(self, d):
        self.prm['Auto_Update']['last_Update'] = d
        return self.writeParams(self.prm)

    last_Update = property(get_last_Update, set_last_Update)
    # -----

    # ----- Получить/Установить интервал обновления номерных ёмкостей
    def get_update_frequency(self):
        return self.prm['Auto_Update']['update_frequency']

    def set_update_frequency(self, n):
        self.prm['Auto_Update']['update_frequency'] = n
        return self.writeParams(self.prm)

    update_frequency = property(get_update_frequency, set_update_frequency)
    # -----


    # def save_new_params(self, params):
    #     params['Yandex']['DeveloperCabinetKey'] = self.prm['Yandex']['DeveloperCabinetKey']
    #     params['Yandex']['ProjectId'] = self.prm['Yandex']['ProjectId']
    #     params['Yandex']['ServiceId'] = self.prm['Yandex']['ServiceId']
    #     params['Yandex']['LongCount'] = self.prm['Yandex']['LongCount']
    #     params['PathDB_Address'] = self.prm['PathDB_Address']
    #     params['BackUpDir'] = self.prm['BackUpDir']
    #     self.prm = params
    #     return self.writeParams(params)

    # Сохранение текущих настроек в файл
    def writeParams(self, params):
        try:
            with open(P + self.NameFileParams, 'w') as file:
                json.dump(params, file, ensure_ascii=False)
        except Exception: return False
        else: return True

    def __call__(self):
        return self.prm
 


