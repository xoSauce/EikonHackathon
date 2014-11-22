import requests
import dfdb
from bs4 import BeautifulSoup
__author__ = 'xosauce'

def get_crime(entry):
    r = requests.get(entry)
    bs = BeautifulSoup(r.content)
    a = bs.find('table', class_='table_indices')
    val = a.find_all('tr')[1].findAll('td')[1].text.strip()
    try:
        index = float(val)
        return index
    except:
        return None



def run():

    dfdb.db_connect()
    start_link = 'http://www.numbeo.com/crime/'
    r = requests.get(start_link)
    bs = BeautifulSoup(r.content)
    links = []
    for entry in bs.find_all('a', href=True):
        link = entry.get('href')
        if link.startswith('country'):
            links.append((entry.text.strip().lower(),start_link+link))
    for entry in links:
        level_of_crime = get_crime(entry[1])
        name = entry[0]
        dfdb.insert("UPDATE countries SET crime_index = %s WHERE name = %s", (level_of_crime,name))
    dfdb.db_close()

if __name__ == '__main__':
    run()