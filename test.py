# проверить размер файла на сервере
import params
import Excel
import fff as f
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

tmp = SrcContent.Get_x3()
f.find_Col_w_Phone(tmp)

# Src_LenAllCols = len(Src_ListAllCols)

# print('Всего '+ str(Src_LenAllCols) + ' колонок')



