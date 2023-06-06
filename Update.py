# проверить размер файла на сервере
import urllib.request
import params
from datetime import datetime
import time
import os

prm = params.Params()
Arrays_list = prm()['Auto_Update']['Arrays'].copy()
folder = prm()['Auto_Update']['folder']

def Check_Arrays():
    # i = 0
    for file in Arrays_list:
        path = f'{params.P}{folder}\{file}.csv'
        if os.path.isfile(path):
            size = os.path.getsize(path)
            if size == 0:
                Download_file(file)
            # else: i += 1
        else:
            Download_file(file)


def Download_file(filename):
    print('скачивание началось')

def Check_Update_Arrays():    
    Arrays = {}
    for file in Arrays_list:
        path = f'{params.P}{folder}\{file}.csv'
        size = os.path.getsize(path)

        dt_file = os.path.getmtime(path)
        tmp = time.ctime(dt_file)
        d = datetime.strptime(tmp, "%a %b %d %H:%M:%S %Y").date()

        Arrays[file] = {'size': size, 'date': d, 'downloaded':0}

    for file in Arrays:
        url = f"{prm()['Auto_Update']['URL_Update']}{file}.csv"
        server_file_size = urllib.request.urlopen('http://' + url).length
        if server_file_size != Arrays[file]['size']:
            Arrays[file]['downloaded'] = 1
            Download_file(file)
    
    with urllib.request.urlopen('https://' + prm()['Auto_Update']['URL_Update']) as response:
        if response.getcode() == 200:
            page = str(response.read())
        else:
            page = False

    if page:
        for file in Arrays:
            if Arrays[file]['downloaded'] == 1: continue
            Pos_s = page.find(file, 140)
            if Pos_s == -1: continue
            Pos_s = page.find('/a>', Pos_s) + 3
            if Pos_s == -1: continue
            Pos_e = page.find('\\r\\n', Pos_s)
            if Pos_s == -1: continue
            Pos_e = page.rfind(' ', Pos_s, Pos_e)
            if Pos_s == -1: continue
            tmp = page[Pos_s:Pos_e].strip()
            tmp = datetime.strptime(tmp, "%d-%b-%Y %H:%M").date()

            if tmp > Arrays[file]['date']:
                Arrays[file]['downloaded'] = 1
                Download_file(file)