import time
val = '+7 (917) -3066121'
start = time.time()



word = 'phon'
header = 'phone gg'
headers_alike = {}
headers_alike[0] = len(word) / len(header)

# cols_alike = {0: 9, 2: 11, 4: 15}
# for val in cols_alike:
#     cols_alike[val] = abs(11 - cols_alike[val])

cols_alike = {0: 2, 2: 0, 4: 4}
# cols_alike = {0: 11}
cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
print(cols_alike)

key = next(iter(cols_alike))
tmp = cols_alike[key]
if tmp == 11:
    tmp = 0
else:
    tmp = round(((11 - tmp) / 11) * 100)



print(tmp)

# print(PhoneCol)

print(headers_alike[0])



end = time.time() - start
print('\n' + str(end))


S1 = 2.32
S2 = 2.97
S3 = 3.12

price = 1130
print('Лист 1525*1525 - Цена за кв. м. ' + str(price / S1))
print('Лист 2440*1220 - Цена за кв. м. ' + str(price / S2))
print('Лист 2500*1250 - Цена за кв. м. ' + str(price / S3))


from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QObject, Signal, Slot

def Check_Arrays(MW):
    download = Signal(int)
    download.connect(MW.PW)

    download.emit(21)
    
