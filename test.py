# проверить размер файла на сервере
import params
import Excel
import Update as upd
import fff as f
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

SrcContent = Excel.Read(path)
# sep = f.find_separator(path, encode)
# print('Разделитель: '+ sep)

# header = f.find_header(path, encode)
# print(header)

# SrcContent.Read_csv(sep, encode)
SrcContent.Read_xlx()
Src_ListAllCols = SrcContent.GetListAllCols()
print(Src_ListAllCols)

# header = f.find_header_csv(path, encode)
header = f.find_header(Src_ListAllCols)
if header:
    print('Заголовок найден')
else:
    print('Заголовок НЕ найден')

tmp = SrcContent.Get_First_20_Rows()
t = f.find_Col_w_Phone(tmp, header)
print(t)

# Src_LenAllCols = len(Src_ListAllCols)

# print('Всего '+ str(Src_LenAllCols) + ' колонок')



# is_db = upd.Check_Arrays()
# print(is_db)

# old_bases = upd.Check_Update_Arrays()
# print(old_bases)

bases = upd.Check_Update_Arrays_for_present('DEF-9xx')
print(type(bases))
print(bases)

if any([bases[file]['status'] == 'no_file' for file in bases]):
    print('нашли')
    fff = 'sdfsdf ' + bases['ABC-4xx']['local_date'].strftime('%m.%d.%Y')

    print(fff)
else:
    print('не нашли')
