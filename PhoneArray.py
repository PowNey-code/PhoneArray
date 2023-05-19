# проверить размер файла на сервере
import urllib.request
import params
import Update as upd
from datetime import datetime, date
import time
import os

#! Надо проверить есть ли файлы вообще
prm = params.Params()

upd.Check_Arrays()
different_date = abs((date.today() - prm.last_Update).days)
if different_date >= prm.frequency:
    upd.Check_Update_Arrays()