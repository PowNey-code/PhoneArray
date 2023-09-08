# проверить размер файла на сервере
import urllib.request
from params import P, Params
from datetime import datetime
import time
import os

prm = Params()
Arrays_list = prm()['Auto_Update']['Arrays'].copy()
folder = prm()['Auto_Update']['folder']

def Check_Arrays():
    if not os.path.isdir(f'{P}{folder}'): return 'no_folder' # Папка с номерными ёмкостями не найдена

    i = 0
    no_files = ''
    for file in Arrays_list:
        path = f'{P}{folder}\{file}.csv'
        if os.path.isfile(path):
            size = os.path.getsize(path)
            if size < 5:
                os.remove(path)
                if i != 0: no_files += ','
                no_files += f'{file}'
                i += 1
        else:
            if i != 0: no_files += ','
            no_files += f'{file}'
            i += 1
        
    if no_files == '': return 'all_good'
    else: return no_files


def Download_file(filename):
    print('скачивание началось')

def Check_Update_Arrays(aa=Arrays_list):
    Arrays = {}
    for file in aa:
        path = f'{P}{folder}\{file}.csv'
        size = os.path.getsize(path)

        dt_file = os.path.getmtime(path)
        tmp = time.ctime(dt_file)
        d = datetime.strptime(tmp, "%a %b %d %H:%M:%S %Y").date()

        Arrays[file] = {'size': size, 'date': d, 'old':0}

    for file in Arrays:
        url = f"{prm()['Auto_Update']['URL_Update']}{file}.csv"
        server_file_size = urllib.request.urlopen('http://' + url).length
        if server_file_size != Arrays[file]['size']:
            Arrays[file]['old'] = 1
    
    with urllib.request.urlopen('https://' + prm()['Auto_Update']['URL_Update']) as response:
        if response.getcode() == 200:
            page = str(response.read())
        else:
            page = False

    if page:
        for file in Arrays:
            if Arrays[file]['old'] == 1: continue
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
                Arrays[file]['old'] = 1
    
    Resp = []
    for file in Arrays:
        if Arrays[file]['old'] == 1:
            Resp.append(file)

    if len(Resp) == 0:
        return 'all_updated'
    else: return Resp

def Check_Update_Arrays_for_present(absent_files):
    absent_array = absent_files.split(',')
    Resp = {}

    if len(absent_array) == len(Arrays_list):
        for file in Arrays_list:
            Resp[file] = {'status':'no_file'}

    else:
        Array_to_check = []
        for file in Arrays_list:
            if file in absent_array:
                Resp[file] = {'status':'no_file'}
            else:
                Array_to_check.append(file)

        tmp = Check_Update_Arrays(Array_to_check)
        if len(tmp) > 0:
            for file in tmp:
                Resp[file] = {'status':'old'}
    
    return Resp