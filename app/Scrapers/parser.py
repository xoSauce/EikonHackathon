__author__ = 'xosauce'

import dfdb

def run(file_name,column_name):
    dfdb.db_connect()
    with open(file_name,'r') as f:
        lines = f.readlines()
    for entry in lines:
        name,middle,end = entry.split('|')
        name = name.strip()
        middle = middle.strip()
        end = end.strip()
        if end != 'null':
            end = float(end)
        else:
            end = None
        dfdb.insert(''' UPDATE countries SET {0}=%s WHERE name=%s '''.format(column_name),(end, name))
    dfdb.db_close()

if __name__ == '__main__':
    run('../static/data/country.debt.value.txt','debt')
    run('../static/data/country.export.value.txt','export')
    run('../static/data/country.import.value.txt','import')
    run('../static/data/country.gdp.value.txt','gdp')