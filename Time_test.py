import time
val = '+7 (917) -3066121'
start = time.time()



word = 'phon'
header = 'phone gg'
headers_alike = {}
headers_alike[0] = len(word) / len(header)

cols_alike = {0: 9, 2: 11, 4: 15}
for val in cols_alike:
    cols_alike[val] = abs(11 - cols_alike[val])

cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
print(cols_alike)

# PhoneCol = next(iter(cols_alike))
# print(PhoneCol)

print(headers_alike[0])



end = time.time() - start
print('\n' + str(end))