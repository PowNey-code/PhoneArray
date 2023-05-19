# проверить размер файла на сервере
import urllib.request
import params
from datetime import datetime
prm = params.Params()



with urllib.request.urlopen('https://opendata.digital.gov.ru/downloads/') as response:
    if response.getcode() == 200:
        page = str(response.read())
    else:
        page = False

if page:
    Arrays_list = prm()['Auto_Update']['Arrays'].copy()
    for file in Arrays_list:
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
        
        print(type(tmp))
        print(tmp)





