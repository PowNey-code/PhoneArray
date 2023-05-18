# проверить размер файла на сервере
import urllib.request
import params
from datetime import datetime, date
import time
import os

prm = params.Params()

def Download_file(filename):
    print('скачивание началось')

def Check_Update_Arrays():    
    Arrays = {}
    Arrays_list = prm()['Auto_Update']['Arrays'].copy()
    folder = prm()['Auto_Update']['folder']
    for file in Arrays_list:
        path = f'{params.P}{folder}\{file}.csv'
        
        size = os.path.getsize(path)

        dt_file = os.path.getmtime(path)
        tmp = time.ctime(dt_file)
        d = datetime.strptime(tmp, "%a %b %d %H:%M:%S %Y").date()

        Arrays[file] = {'size': size, 'date': d, 'downloaded':0}

    for file in Arrays:
        url = f"http://{prm()['Auto_Update']['URL_Update']}{file}.csv"
        server_file_size = urllib.request.urlopen(url).length
        if server_file_size != Arrays[file]['size']:
            Arrays[file]['downloaded'] = 1
            Download_file(file)



different_date = abs((date.today() - prm.last_Update).days)
if different_date >= prm.frequency:
    Check_Update_Arrays()