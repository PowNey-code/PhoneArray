import time
val = ' '
start = time.time()



# for i in range(0, 100000):
#     if any(map(lambda s: s.isdigit(), val)):
#         print(True)
#     else:
#         print(False)


# if any(map(lambda s: s.isalpha() and not s.isdigit(), val)):
if not any(s.isalpha() and (not s.isdigit() or s.isspace()) for s in val):

    print('Цифра')
else:
    print('Буква')

end = time.time() - start
print(end)

