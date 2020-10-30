
from asaotdata import data
from asaotdata import url
from bs4 import BeautifulSoup
import requests

destination = 'יבנה'

destination_list = []
for i in range(1, 21):
    data["__EVENTARGUMENT"] = 'Page$' + str(i)

    x = requests.post(url, data=data)
    if x.status_code == 500:
        break
    else:
        soup = BeautifulSoup(x.content, 'lxml')

        table = soup.find("table")
        for tr in table.findChildren('tr'):
            x = tr.get_text()
            if x.find(destination) != -1 and x.find(destination) < 60:
                all_td = tr.findAll("td")
                for temp in all_td:
                    destination_list.append(temp.text)
                    
for i in range(0, len(destination_list)):
    print(destination_list[i])
    