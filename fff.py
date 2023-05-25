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

def find_header_csv(path, encode):
    f = open(path, 'r', encoding=encode)
    line = f.readline()
    f.close
    return not any(map(str.isdigit, line))

def find_header_xls(path, encode):
    pass