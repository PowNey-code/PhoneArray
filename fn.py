import chardet
import re

def get_encode_file_auto(FPath):
    with open(FPath, 'rb') as f:
        encode = chardet.detect(f.read(10000))['encoding']
        if encode in ['windows-1251', 'windows-1252', 'utf-8']:
            return encode
        else: return 'utf-8'
        # else: return 'latin'

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
    # преимущество в определении колонки с номером телефона
    # если + то преимущество будет у заголовка,
    # если минус то у содержимого колонки
    privilege = 10
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
            if type(val) == bool: continue
            elif type(val) == int:
                cols_alike[i] = abs(11 - len(str(val)))
            else:
                if re.search(r"^[\d\s\(\)\-+]{6,22}$", val):
                    cols_alike[i] = abs(11 - len(val))
        i += 1
    

    if len(cols_alike) > 0:
        if header_alike:
            if header_alike in cols_alike:
                PhoneCol = header_alike
            else:
                # Ищем ближайший к 11
                cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
                key = next(iter(cols_alike))
                tmp = cols_alike[key]
                if tmp == 11:
                    rate_col = 0
                else:
                    rate_col = round(((11 - tmp) / 11) * 100)

                rate_header = headers_alike[header_alike] * 100
                rate_header += privilege
                if rate_header >= rate_col:
                    PhoneCol = header_alike
                else:
                    PhoneCol = key
        else:
            # Ищем ближайший к 11
            cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
            PhoneCol = next(iter(cols_alike))
    else:
        PhoneCol = header_alike

    return PhoneCol

def format_digit(dig:int) -> str:
    round_dig = round(dig)
    return '{0:,}'.format(round_dig).replace(',', ' ')