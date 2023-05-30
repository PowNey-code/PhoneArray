import time
val = '+7 (917) -3066121'
start = time.time()
import re

if re.search(r"^[\d\s\(\)\-+]{6,22}$", val):
    print('Подходит')
else:
    print('нет')    

# if any(map(lambda s: s.isalpha() and not s.isdigit(), val)):
# if not any(s.isalpha() and (not s.isdigit() or s.isspace()) for s in val):

#     print('Цифра')
# else:
#     print('Буква')

end = time.time() - start
print(end)

cols_alike = {0: 9, 2: 11}
for val in cols_alike:
    cols_alike[val] = abs(11 - cols_alike[val])

cols_alike = dict(sorted(cols_alike.items(), key=lambda item: item[1]))
print(cols_alike)
PhoneCol = next(iter(cols_alike))
print(PhoneCol)