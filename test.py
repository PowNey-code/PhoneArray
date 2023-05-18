# проверить размер файла на сервере
import urllib.request

# url = 'http://opendata.digital.gov.ru/downloads/DEF-9xx.csv'
# file = urllib.request.urlopen(url)
# print(file.length)


res = urllib.request.urlopen('https://opendata.digital.gov.ru/downloads/')
print(res.read())





