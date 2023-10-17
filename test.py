# проверить размер файла на сервере
from params import P, Params
import Excel
import Update as upd
import fn
from urllib.request import urlopen
from datetime import datetime, date
prm = Params()


# разделители
#     пробел или ТАБ - '\s+'



path = 'members.csv'
# path = 'groupexport_b4ck4_2023-02-27.csv'
path = 'groupexport_b4ck4_2023-02-27.xlsx'

# encode = f.get_encode_file_auto(path)
# encode = 'latin'
# print('Кодировка: ' + encode)

# is_db = upd.Check_Arrays()
# print(is_db)

# old_bases = upd.Check_Update_Arrays()
# print(old_bases)


r = fn.format_digit(1651654.5654)
print(r)



# print(response.status_code)
# https://pythonassets.com/posts/download-file-with-progress-bar-pyqt-pyside/