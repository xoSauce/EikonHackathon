import requests
import dfdb
from bs4 import BeautifulSoup
__author__ = 'xosauce'

def run():
    dfdb.db_connect()
    start_link = 'https://en.wikipedia.org/wiki/List_of_countries_by_natural_disaster_risk'
    r = requests.get(start_link)
    bs = BeautifulSoup(r.content)
    links = []
    for entry in bs.select('.wikitable'):
        for entry2 in entry.select('tr'):
            if len(entry2.select('td')) >1:
                links.append((entry2.select('td')[0].text.lower().strip(), float(entry2.select('td')[2].text.strip().strip('%'))))
    for entry in links:
        name = entry[0]
        value = entry[1]
        dfdb.insert("UPDATE countries SET natural_disaster_index=%s WHERE name=%s",(value,name))

if __name__ == '__main__':
    run()