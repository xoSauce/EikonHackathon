import requests
import dfdb
from bs4 import BeautifulSoup
__author__ = 'xosauce'

def run():
    dfdb.db_connect()
    start_link = 'http://www.numbeo.com/pollution/rankings_by_country.jsp?title=2014-mid'
    r = requests.get(start_link)
    bs = BeautifulSoup(r.content)
    links = []
    for entry in bs.find('tbody').find_all('tr'):
        entry2 = entry.find_all('td')
        name = entry2[0].text.strip()
        pollutionIndex = -1
        try:
            pollutionIndex = float(entry2[1].text.strip())
        except:
            pollutionIndex = -1
        links.append((name, pollutionIndex))

    for entry in links:
        pollutionIndex = entry[1]
        name = entry[0].lower().strip()
        dfdb.insert("UPDATE countries SET pollution_index=%s WHERE name=%s",(pollutionIndex,name))
    dfdb.db_close()


if __name__ == '__main__':
    run()