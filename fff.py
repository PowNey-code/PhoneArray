import chardet

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
    # print(Rows)
    if headIs:
        Variable_Word_Phone = ['телефон', 'номер', 'phon', 'number', 'telefon', 'telephon']
        headers_alike = {}
        i = 0
        for header in Rows:
            header = header.lower()
            for word in Variable_Word_Phone:
                if word in header:
                    headers_alike[i] = len(word) / len(header)
            i += 1

        headers_alike = dict(sorted(headers_alike.items(), reverse=True, key=lambda item: item[1]))
        header_alike = next(iter(headers_alike))
        print(header_alike)


    for el in Rows:
        print('\n' + el)
        col = Rows[el]
        for val in col:
            print(val)

            

    if headIs:
        pass
    else:
        pass

    # избавиться от нан и поискать буквы во всех столбцах, где букв нет там и номер
        # print(rr)
        # for r in Rows[rr]:
        #     print(r)
