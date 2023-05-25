# проверить размер файла на сервере
import urllib.request
import params
from datetime import datetime
import Excel
import fff as f
prm = params.Params()



# with urllib.request.urlopen('https://opendata.digital.gov.ru/downloads/') as response:
#     if response.getcode() == 200:
#         page = str(response.read())
#     else:
#         page = False

# if page:
#     Arrays_list = prm()['Auto_Update']['Arrays'].copy()
#     for file in Arrays_list:
#         Pos_s = page.find(file, 140)
#         if Pos_s == -1: continue
#         Pos_s = page.find('/a>', Pos_s) + 3
#         if Pos_s == -1: continue
#         Pos_e = page.find('\\r\\n', Pos_s)
#         if Pos_s == -1: continue
#         Pos_e = page.rfind(' ', Pos_s, Pos_e)
#         if Pos_s == -1: continue
#         tmp = page[Pos_s:Pos_e].strip()
#         tmp = datetime.strptime(tmp, "%d-%b-%Y %H:%M").date()
        
#         print(type(tmp))
#         print(tmp)


# разделители
#     пробел или ТАБ - '\s+'


# //*-- Находим разделитель в файле --
# $separators = [':', ';', '|'];
# while( count($separators) > 1 ){
#     if( ($row = fgets($file_l)) === FALSE) break;
#     $row = convert($row);
#     if( trim($row) == '' ) continue;
#     foreach($separators AS $key => $separator) {    
#         if(mb_strpos($row, $separator) === FALSE) unset($separators[$key]);
#     }
# }
# rewind($file_l);
# if(fgets($file_l, 4) !== "\xef\xbb\xbf") rewind($file_l);// Пропускаем *BOM





path = 'members.csv'
# path = 'groupexport_b4ck4_2023-02-27.csv'
# path = 'groupexport_b4ck4_2023-02-27.xlsx'

encode = f.get_encode_file_auto(path)
print(encode)

SrcContent = Excel.Read(path)
sep = f.find_separator(path, encode)
print(sep)

header = f.find_header(path, encode)
print(header)

SrcContent.Read_csv(sep)
Src_ListAllCols = SrcContent.GetListAllCols()
Src_LenAllCols = len(Src_ListAllCols)

print(Src_ListAllCols)
print(Src_LenAllCols)



