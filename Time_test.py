import time


str = 'aaaa 123 bbb'
start = time.time()

# import re

# for i in range(0, 1000):
#     if re.search('\d+', str) is not None:
#         print(True)
#     else:
#         print(False)

# end = time.time() - start
# print(end)



tt = any(map(str.isdigit, str))
print(tt)

# for i in range(0, 1000):
#     if any(map(str.isdigit(), 'qwe1')):
#         print(True)
#     else:
#         print(False)

end = time.time() - start
print(end)

