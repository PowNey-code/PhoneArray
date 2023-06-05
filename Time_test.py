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



out_D = 180
in_D = 155
h = 100
Len_on_circle_one_rebro = 8

out_D -= 2
in_D += 2
h -= 8

length_circle = 3.14 * out_D
print('Длина окружности: ' + str(length_circle))

total_reber = length_circle / Len_on_circle_one_rebro
print('Всего рёбер: ' + str(total_reber))

mm_one_rebro = (out_D - in_D) * 2
total_len_filter = total_reber * mm_one_rebro
square = round ((total_len_filter * h) / 100)
print('Общая площадь фильтрующего элемента: ' + str(square) + ' см')