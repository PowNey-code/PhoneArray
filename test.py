# проверить размер файла на сервере
import params
import Excel
import Update as upd
import fn
from datetime import datetime, date
prm = params.Params()


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