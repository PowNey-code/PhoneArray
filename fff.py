import chardet
import re

def get_encode_file_auto(FPath):
    with open(FPath, 'rb') as f:
        encode = chardet.detect(f.read(10000))['encoding']
        if encode in ['windows-1251', 'utf-8']:
            return encode
        else: return 'latin'

def find_separator(path, encode):
    separators = [',', ':', ';', '|']
    f = open(path, 'r', encoding=encode)
    while len(separators) > 1:
        line = f.readline()
        if not line: break
        line = line.strip()
        if line == '': continue
        for sep in separators[:]:
            if not sep in line:
                separators.remove(sep)

    f.close
    if len(separators) > 1:
        return False
    return separators[0]

def find_header(columns):
    for col in columns:
        if any(map(str.isdigit, str(col))):
            return False
    return True

def find_Col_w_Phone(Rows, headIs):
    # Если заголовок присутствует
    if headIs:
        Variable_Word_Phone = ['телефон', 'номер', 'phon', 'number', 'telefon', 'telephon']
        headers_alike = {}
        i = 0
        for header in Rows:
            header = header.lower()
            for word in Variable_Word_Phone:
                if word in header:
                    # проставляем коэффициент точности к номеру каждой колонке в которой найдено совпадение 
                    headers_alike[i] = len(word) / len(header)
            i += 1

        # сортируем все найденные значения коэффициентов по убыванию
        if len(headers_alike) > 0:
            headers_alike = dict(sorted(headers_alike.items(), reverse=True, key=lambda item: item[1]))
            header_alike = next(iter(headers_alike))
        else:
            header_alike = False

    # Поиск по содержимому колонок
    cols_alike = {}
    i = 0
    for header in Rows:
        col = Rows[header]
        for val in col:
            if type(val) == int:
                cols_alike[i] = len(str(val))
            else:
                if re.search(r"^[\d\s\(\)\-+]{6,22}$", val):
                    cols_alike[i] = len(val)
        i += 1
    
    if len(cols_alike) > 0:
        if header_alike:
            if header_alike in cols_alike:
                PhoneCol = header_alike
        else:
            # Ищем наиближайший к 11
            for val in cols_alike:
                cols_alike[val] = abs(11 - cols_alike[val])

            cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
            PhoneCol = next(iter(cols_alike))
    else:
        PhoneCol = header_alike

    return PhoneCol
