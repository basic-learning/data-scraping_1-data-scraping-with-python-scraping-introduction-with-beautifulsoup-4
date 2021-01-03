import bs4
import requests
url = 'https://jadwalsholat.pkpu.or.id/?id=293'
contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text,"html.parser")
data = response.find_all('tr','table_highlight')
data = data[0]

salat = {}
i = 0
for d in data:
    if i == 1:
        salat['Subuh'] = d.get_text()
    elif i == 2:
        salat['Zuhur'] = d.get_text()
    elif i == 3:
        salat['Asar'] = d.get_text()
    elif i == 4:
        salat['Magrib'] = d.get_text()
    elif i == 5:
        salat['Isya'] = d.get_text()
    i += 1
print(salat)
print(salat['Asar'])